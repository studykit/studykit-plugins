import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type { Item, Place } from '../types'

const PANE = 'agenda'
const TITLE = '안건'
// The dock's width beside a fullscreen transcript: a sidebar, not the default share. A width the person drags wins.
const COLUMNS = 44
const items = atom({ plugin: 'agenda', key: 'items' } as const, [])
const isHidden = atom({ plugin: 'agenda', key: 'isHidden' } as const, false)
const start = atom({ plugin: 'agenda', key: 'start' } as const, 0)
const focus = atom({ plugin: 'agenda', key: 'focus' } as const, '')
// Where the list shows: its own pane (the surface seats it, docked beside the transcript in fullscreen, else
// inline above the prompt) or the band right above the prompt. Kept across sessions in the store.
const place = atom({ plugin: 'agenda', key: 'place' } as const, 'pane')
const PLACE_KEY = 'place'
// Each session's list and topic are also kept in the store, under its id (the transcript's name), so a resumed
// session gets its agenda back and a reload that empties the state does not lose it. Entries untouched for
// KEEP_DAYS are dropped.
const SESSION_PREFIX = 'session:'
const KEEP_DAYS = 30
type Saved = { items: Item[]; focus: string; savedAt: number }
let loadedFor: string | undefined

async function save($: EngineInterface): Promise<void> {
  const id = await $.session.id()
  const list = await read($, items)
  const now = await read($, focus)
  if (list.length === 0 && now === '') await $.store.delete(SESSION_PREFIX + id)
  else await $.store.set(SESSION_PREFIX + id, { items: list, focus: now, savedAt: await $.clock.now() } satisfies Saved)
}

// Loads the session's saved agenda once per session id: on start, and when /clear or /resume switches the id
// under a running process. A session with nothing saved keeps what the state holds (an agenda from before
// this was saved), except after a switch, where the previous session's list must not carry over.
async function sync($: EngineInterface): Promise<void> {
  const id = await $.session.id()
  if (id === loadedFor) return
  const isSwitch = loadedFor !== undefined
  loadedFor = id
  const kept = (await $.store.get(SESSION_PREFIX + id)) as Saved | undefined
  if (kept) {
    await update($, items, () => kept.items)
    await update($, focus, () => kept.focus)
  } else if (isSwitch) {
    await update($, items, () => [])
    await update($, focus, () => '')
  } else await save($)
  await update($, start, () => 0)
  await showStatus($)
}

async function prune($: EngineInterface): Promise<void> {
  const cutoff = (await $.clock.now()) - KEEP_DAYS * 86_400_000
  for (const key of await $.store.keys()) {
    if (!key.startsWith(SESSION_PREFIX)) continue
    const v = (await $.store.get(key)) as Saved | undefined
    if (!v || v.savedAt < cutoff) await $.store.delete(key)
  }
}

const str = (v: unknown): string | undefined => (typeof v === 'string' && v.trim() !== '' ? v.trim() : undefined)

async function showStatus($: EngineInterface): Promise<void> {
  const list = await read($, items)
  const decisions = list.filter(d => d.isDecision).length
  $.ui.status(list.length > 0 ? `📋${list.length}${decisions > 0 ? ` · 🚦${decisions}` : ''}` : undefined)
}

async function show($: EngineInterface): Promise<void> {
  if ((await read($, place)) === 'pane') $.ui.open({ id: PANE, title: TITLE, columns: COLUMNS }).catch(() => undefined)
}

async function moveTo($: EngineInterface, where: Place): Promise<void> {
  await update($, place, () => where)
  await $.store.set(PLACE_KEY, where)
  if (where === 'band') await $.ui.close({ id: PANE })
  else await $.ui.open({ id: PANE, title: TITLE, columns: COLUMNS })
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'agenda', description: '이 세션의 안건(지금 주제와 남은 항목)을 보여줍니다 (band: prompt 위로, pane: pane으로, close: 닫기)', argumentHint: '[band|pane|close]' })
    const kept = await $.store.get(PLACE_KEY)
    if (kept === 'band' || kept === 'pane') await update($, place, () => kept)
    await $.tool.register({
      name: 'agenda_add',
      description:
        'Add or update an open item of this session in the user\'s "안건" pane: a topic raised and not yet finished, ' +
        'or (decision: true) a choice only the user can make. Same id updates it.',
      inputSchema: {
        type: 'object',
        properties: {
          id: { type: 'string', description: 'Short stable key, e.g. a TODO id' },
          title: { type: 'string', description: 'The item or question, one line, in the user\'s language' },
          detail: { type: 'string', description: 'Options or context, one or two lines' },
          decision: { type: 'boolean', description: 'True when the user must decide it' },
        },
        required: ['id', 'title'],
      },
      isDeferred: false,
    })
    await $.tool.register({
      name: 'agenda_resolve',
      description: 'Remove an item from the "안건" pane once it is finished or the user has decided it; the answer is for the record of the call.',
      inputSchema: {
        type: 'object',
        properties: { id: { type: 'string' }, answer: { type: 'string', description: 'What was decided or done, short' } },
        required: ['id', 'answer'],
      },
      isDeferred: false,
    })
    await $.tool.register({
      name: 'agenda_focus',
      description:
        'Set the topic being discussed now, shown at the top of the "안건" pane, so the user can see what the conversation is about. ' +
        'Call it when the topic changes; an empty topic clears it.',
      inputSchema: {
        type: 'object',
        properties: { topic: { type: 'string', description: 'One line, in the user\'s language' } },
        required: ['topic'],
      },
      isDeferred: false,
    })
    await sync($)
    await prune($)
    await showStatus($)
    if ((await read($, items)).length > 0 || (await read($, focus)) !== '') await show($)
    return next(e)
  })

  // /clear and /resume change the session id with no event of their own: the next prompt or call notices.
  on('prompt.submit', async ($, e, next) => {
    await sync($)
    return next(e)
  })

  on('command.run', { command: 'agenda' }, async ($, e) => {
    await sync($)
    const arg = e.args.trim()
    if (arg === 'close') {
      if ((await read($, place)) === 'band') await update($, isHidden, () => true)
      await $.ui.close({ id: PANE })
      return { text: '안건을 닫았습니다. /agenda 로 다시 엽니다.' }
    }
    await update($, isHidden, () => false)
    if (arg === 'band' || arg === 'pane') {
      await moveTo($, arg)
      return { text: arg === 'band' ? '안건을 prompt 위 band로 옮겼습니다. /agenda pane 으로 되돌립니다.' : '안건을 pane으로 옮겼습니다. /agenda band 로 prompt 위에 둡니다.' }
    }
    if ((await read($, place)) === 'band') return { text: '안건은 prompt 위 band에 있습니다.' }
    await $.ui.open({ id: PANE, title: TITLE, columns: COLUMNS })
    return { text: '안건 pane을 열었습니다.' }
  })

  on('tool.call', { tool: 'mcp__agenda__agenda_add' }, async ($, e) => {
    await sync($)
    const id = str(e.id)
    const title = str(e.title)
    if (!id || !title) return { deny: 'id and title are required.' }
    const one: Item = { id, title, detail: str(e.detail), isDecision: e.decision === true }
    await update($, items, list => (list.some(d => d.id === id) ? list.map(d => (d.id === id ? one : d)) : [...list, one]))
    await save($)
    await showStatus($)
    await update($, isHidden, () => false)
    await show($)
    return { result: `Listed "${id}".` }
  })

  on('tool.call', { tool: 'mcp__agenda__agenda_resolve' }, async ($, e) => {
    await sync($)
    const id = str(e.id)
    const answer = str(e.answer)
    if (!id || !answer) return { deny: 'id and answer are required.' }
    if (!(await read($, items)).some(d => d.id === id)) return { deny: `No item "${id}".` }
    await update($, items, list => list.filter(d => d.id !== id))
    await save($)
    await showStatus($)
    return { result: `Resolved "${id}".` }
  })

  on('tool.call', { tool: 'mcp__agenda__agenda_focus' }, async ($, e) => {
    await sync($)
    const topic = str(e.topic) ?? ''
    await update($, focus, () => topic)
    await save($)
    if (topic) await show($)
    return { result: topic ? `Focus: ${topic}` : 'Focus cleared.' }
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    if (e.props.hasSurvey || (await read($, place)) !== 'band' || (await read($, isHidden))) return next(e)
    if ((await read($, items)).length === 0 && (await read($, focus)) === '') return next(e)
    // At most half the band's room, so the transcript keeps the rest.
    return body($, e, Math.max(3, Math.floor(e.props.maxRows / 2)), false)
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) =>
    body($, e, e.props.scroll?.bodyRows ?? e.viewport?.rows ?? 24, true),
  )
}

// The person makes an item the current topic by pressing it: a click, or Enter on it once the site has the
// keyboard (ctrl+x tab), or in the pane its digit. The model is told in a row it reads with the next request.
async function choose($: EngineInterface, d: Item): Promise<void> {
  await update($, focus, () => d.title)
  await save($)
  await $.session.append({
    message: { type: 'user', content: [{ type: 'text', text: `[안건] 사용자가 "${d.title}" (${d.id})를 지금 다룰 주제로 골랐습니다.` }] },
  })
}

// The focus line and a page of whole items that fits `room` rows, one row kept for the paging buttons. Digit
// hotkeys only in the pane: in the band a bare digit in an empty prompt would press them instead of typing.
async function body($: EngineInterface, e: Parameters<EngineInterface['ui']['resolve']>[0], room: number, hasDigits: boolean) {
  const { Box, Button, Text } = $.ui.resolve(e)
  const now = await read($, focus)
  const open = await read($, items)
  const head = now ? <Text color="cyan" bold>{`▶ 지금: ${now}`}</Text> : null
  if (open.length === 0)
    return (
      <Box flexDirection="column">
        {head}
        <Text dimColor>남은 안건이 없습니다.</Text>
      </Box>
    )
  const rows = Math.max(1, room - 1 - (now ? 1 : 0))
  const height = (d: Item) => (d.detail ? 2 : 1)
  const first = Math.min(await read($, start), open.length - 1)
  let last = first
  let used = 0
  while (last < open.length && used + height(open[last]!) <= rows) used += height(open[last++]!)
  if (last === first) last = first + 1
  const prevStart = (() => {
    let i = first
    let h = 0
    while (i > 0 && h + height(open[i - 1]!) <= rows) h += height(open[--i]!)
    return i
  })()
  const isPaged = first > 0 || last < open.length
  return (
    <Box flexDirection="column">
      {head}
      {open.slice(first, last).map((d, i) => {
        // A plain Button draws its hotkey before the label (`1: `), which then stands in for the item's number.
        const hotkey = hasDigits && i < 9 ? String(i + 1) : undefined
        return (
          <Box flexDirection="column" key={`o-${d.id}`}>
            <Button key={`pick-${d.id}`} plain hotkey={hotkey} onPress={() => choose($, d)}>
              <Text bold color={d.title === now ? 'cyan' : undefined}>
                {`${hotkey ? '' : `${first + i + 1}. `}${d.isDecision ? '🚦 ' : ''}${d.title}${d.title === now ? ' ◀' : ''}`}
              </Text>
            </Button>
            {d.detail ? <Text dimColor>{`   ${d.id} · ${d.detail}`}</Text> : null}
          </Box>
        )
      })}
      {isPaged && (
        <Box>
          <Text dimColor>
            {first + 1}–{last} / {open.length}{' '}
          </Text>
          {first > 0 && <Button key="prev" label="↑ 이전 (k)" hotkey="k" onPress={() => update($, start, () => prevStart)} />}
          {last < open.length && <Button key="next" label="↓ 다음 (j)" hotkey="j" onPress={() => update($, start, () => last)} />}
        </Box>
      )}
    </Box>
  )
}
