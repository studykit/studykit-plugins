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
// The id of the listed item being discussed now; '' when none. Only a listed item can be the topic, and
// resolving it clears the topic.
const focus = atom({ plugin: 'agenda', key: 'focus' } as const, '')
// The item pressed and awaiting the person's yes before it becomes the topic; '' when none.
const pending = atom({ plugin: 'agenda', key: 'pending' } as const, '')
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
  }
  // Up to 0.3 the topic was free text, not an id: a title of a listed item becomes its id, any other is dropped.
  const list = await read($, items)
  await update($, focus, f => (list.some(d => d.id === f) ? f : (list.find(d => d.title === f)?.id ?? '')))
  if (!kept && !isSwitch) await save($)
  await update($, start, () => 0)
  await update($, pending, () => '')
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

// The item being discussed now, if any.
async function topic($: EngineInterface): Promise<Item | undefined> {
  const now = await read($, focus)
  return (await read($, items)).find(d => d.id === now)
}

async function showStatus($: EngineInterface): Promise<void> {
  const list = await read($, items)
  const decisions = list.filter(d => d.isDecision).length
  $.ui.status(list.length > 0 ? `📋${list.length}${decisions > 0 ? ` · 🚦${decisions}` : ''}` : undefined)
}

// Opens the pane unasked. Below the engine's width floor, or on a surface that places no panes, it waits
// undrawn; the answer is then a note for the model to pass on, since the person sees nothing.
async function show($: EngineInterface): Promise<string> {
  if ((await read($, place)) !== 'pane') return ''
  const opened = await $.ui.open({ id: PANE, title: TITLE, columns: COLUMNS }).catch(() => undefined)
  if (!opened || opened.isPlaced) return ''
  return ` The "${TITLE}" pane is not drawn (${opened.reason}); the user can open it with /agenda, or put the list above the prompt with /agenda band.`
}

// The person's own open: placed at any width, unless no attached surface places panes. Answers '' when drawn,
// else why not.
async function openAsked($: EngineInterface): Promise<string> {
  const opened = await $.ui.open({ id: PANE, title: TITLE, columns: COLUMNS })
  return opened.isPlaced ? '' : ` 다만 화면에 그려지지 않았습니다: ${opened.reason}`
}

async function moveTo($: EngineInterface, where: Place): Promise<string> {
  await update($, place, () => where)
  await $.store.set(PLACE_KEY, where)
  if (where === 'pane') return openAsked($)
  await $.ui.close({ id: PANE })
  return ''
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'agenda', description: '이 세션의 안건(지금 주제와 남은 항목)을 보여줍니다 (번호나 id: 지금 주제로 고르기, unfocus: 지금 주제 해제, band: prompt 위로, pane: pane으로, close: 닫기)', argumentHint: '[번호|id|unfocus|band|pane|close]' })
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
        'Mark the listed item the conversation is on right now, by its number in the "안건" pane; it shows at the top so the user ' +
        'can see what is being discussed. Focus an item only while it is being discussed: when the conversation moves to another ' +
        'listed item, focus that one; when it moves off the list, call agenda_unfocus (or agenda_add the new topic, then focus it). ' +
        'Resolving the focused item clears the focus.',
      inputSchema: {
        type: 'object',
        properties: { number: { type: 'integer', minimum: 1, description: 'The item\'s number in the list, from 1' } },
        required: ['number'],
      },
      isDeferred: false,
    })
    await $.tool.register({
      name: 'agenda_unfocus',
      description: 'Clear the focused item of the "안건" pane once the conversation is no longer on it.',
      inputSchema: { type: 'object', properties: {} },
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
    if (arg === 'unfocus') {
      const was = await topic($)
      if (!was) return { text: '지금 주제가 없습니다.' }
      await unfocus($)
      await $.session.append({
        message: { type: 'user', content: [{ type: 'text', text: `[안건] 사용자가 지금 주제 "${was.title}" (${was.id})를 해제했습니다.` }] },
      })
      return { text: `지금 주제를 해제했습니다: ${was.title}` }
    }
    await update($, isHidden, () => false)
    if (arg === 'band' || arg === 'pane') {
      const unplaced = await moveTo($, arg)
      return { text: arg === 'band' ? '안건을 prompt 위 band로 옮겼습니다. /agenda pane 으로 되돌립니다.' : `안건을 pane으로 옮겼습니다. /agenda band 로 prompt 위에 둡니다.${unplaced}` }
    }
    if (arg !== '') {
      // Typed out, the pick is deliberate: no yes to ask for, unlike a press.
      const open = await read($, items)
      const d = /^\d+$/.test(arg) ? open[Number(arg) - 1] : open.find(x => x.id === arg)
      if (!d) return { text: `"${arg}"에 해당하는 안건이 없습니다. 번호(1–${open.length})나 id로 고릅니다.` }
      if (d.id !== (await read($, focus))) await choose($, d)
      await show($)
      return { text: `지금 주제: ${d.title}` }
    }
    if ((await read($, place)) === 'band') return { text: '안건은 prompt 위 band에 있습니다.' }
    return { text: `안건 pane을 열었습니다.${await openAsked($)}` }
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
    const number = (await read($, items)).findIndex(d => d.id === id) + 1
    return { result: `Listed "${id}" as number ${number}.${await show($)}` }
  })

  on('tool.call', { tool: 'mcp__agenda__agenda_resolve' }, async ($, e) => {
    await sync($)
    const id = str(e.id)
    const answer = str(e.answer)
    if (!id || !answer) return { deny: 'id and answer are required.' }
    const list = await read($, items)
    const at = list.findIndex(d => d.id === id)
    if (at < 0) return { deny: `No item "${id}".` }
    const wasFocus = (await read($, focus)) === id
    await update($, items, l => l.filter(d => d.id !== id))
    await update($, pending, p => (p === id ? '' : p))
    if (wasFocus) await update($, focus, () => '')
    await save($)
    await showStatus($)
    const moved = at < list.length - 1 ? ` Items after number ${at + 1} moved up one number.` : ''
    return { result: `Resolved "${id}".${wasFocus ? ' It was the focus; the focus is cleared.' : ''}${moved}` }
  })

  on('tool.call', { tool: 'mcp__agenda__agenda_focus' }, async ($, e) => {
    await sync($)
    const list = await read($, items)
    // Typed a number, but a model may still send "2".
    const raw: unknown = e.number
    const n = typeof raw === 'number' ? raw : typeof raw === 'string' && /^\d+$/.test(raw.trim()) ? Number(raw) : NaN
    const d = Number.isInteger(n) ? list[n - 1] : undefined
    if (!d) {
      const listed = list.map((x, i) => `${i + 1}. ${x.title} (${x.id})`).join('; ')
      return { deny: list.length === 0 ? 'The list is empty: add the item with agenda_add first.' : `No item number ${String(e.number)}. Listed: ${listed}` }
    }
    await update($, focus, () => d.id)
    await update($, pending, () => '')
    await save($)
    return { result: `Focus: ${n}. ${d.title} (${d.id}).${await show($)}` }
  })

  on('tool.call', { tool: 'mcp__agenda__agenda_unfocus' }, async $ => {
    await sync($)
    const was = await topic($)
    if (!was) return { result: 'Nothing was focused.' }
    await unfocus($)
    return { result: `Focus cleared (was "${was.title}").` }
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    if (e.props.hasSurvey || (await read($, place)) !== 'band' || (await read($, isHidden))) return next(e)
    if ((await read($, items)).length === 0 && (await read($, focus)) === '') return next(e)
    // At most half the band's room, so the transcript keeps the rest.
    return body($, e, Math.max(3, Math.floor(e.props.maxRows / 2)), false, e.requestId)
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) =>
    body($, e, e.props.scroll?.bodyRows ?? e.viewport?.rows ?? 24, true, PANE),
  )
}

// The person makes an item the current topic by pressing it (a click, or Enter on it once the site has the
// keyboard (ctrl+x tab), or in the pane its digit) and then saying yes: a stray press must not tell the model
// the topic moved. Pressing the topic itself does nothing.
async function ask($: EngineInterface, d: Item, site: string): Promise<void> {
  if (d.id === (await read($, focus))) return
  await update($, pending, () => d.id)
  // Moves the ring onto the yes so Enter answers; a site not holding the keys refuses, and a click still works.
  await $.ui.focus({ requestId: site, key: 'confirm' }).catch(() => undefined)
}

// The model is told in a row it reads with the next request.
async function choose($: EngineInterface, d: Item): Promise<void> {
  await update($, pending, () => '')
  await update($, focus, () => d.id)
  await save($)
  await $.session.append({
    message: { type: 'user', content: [{ type: 'text', text: `[안건] 사용자가 "${d.title}" (${d.id})를 지금 다룰 주제로 골랐습니다.` }] },
  })
}

async function unfocus($: EngineInterface): Promise<void> {
  await update($, focus, () => '')
  await update($, pending, () => '')
  await save($)
}

// The focus line and a page of whole items that fits `room` rows, one row kept for the paging buttons. Digit
// hotkeys only in the pane: in the band a bare digit in an empty prompt would press them instead of typing.
async function body($: EngineInterface, e: Parameters<EngineInterface['ui']['resolve']>[0], room: number, hasDigits: boolean, site: string) {
  const { Box, Button, Text } = $.ui.resolve(e)
  const open = await read($, items)
  const focused = await read($, focus)
  const now = open.find(d => d.id === focused)?.title
  const asking = await read($, pending)
  const asked = open.find(d => d.id === asking)
  // A blank row under the topic sets it apart from the items to pick from.
  const head = now ? (
    <Box flexDirection="column">
      <Text color="cyan" bold>{`🎯 ${now}`}</Text>
      <Text> </Text>
    </Box>
  ) : null
  if (open.length === 0)
    return (
      <Box flexDirection="column">
        {head}
        <Text dimColor>남은 안건이 없습니다.</Text>
      </Box>
    )
  const rows = Math.max(1, room - 1 - (now ? 2 : 0) - (asked ? 2 : 0))
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
      {asked && (
        <Box flexDirection="column">
          <Text color="yellow">{`"${asked.title}"을(를) 지금 주제로 할까요?`}</Text>
          <Box>
            <Button key="confirm" label="선택 (y)" hotkey="y" variant="primary" onPress={() => choose($, asked)} />
            <Text> </Text>
            <Button key="cancel" label="취소 (n)" hotkey="n" onPress={() => update($, pending, () => '')} />
          </Box>
        </Box>
      )}
      {open.slice(first, last).map((d, i) => {
        // A plain Button draws its hotkey before the label (`1: `), which then stands in for the item's number.
        const hotkey = hasDigits && i < 9 ? String(i + 1) : undefined
        return (
          <Box flexDirection="column" key={`o-${d.id}`}>
            <Button key={`pick-${d.id}`} plain hotkey={hotkey} onPress={() => ask($, d, site)}>
              <Text bold color={d.id === focused ? 'cyan' : undefined}>
                {`${hotkey ? '' : `${first + i + 1}. `}${d.isDecision ? '🚦 ' : ''}${d.title}${d.id === focused ? ' ◀' : ''}`}
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
