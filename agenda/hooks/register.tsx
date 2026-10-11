import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type { Item } from '../types'

const PANE = 'agenda'
const TITLE = '안건'
const items = atom({ plugin: 'agenda', key: 'items' } as const, [])
const start = atom({ plugin: 'agenda', key: 'start' } as const, 0)
const focus = atom({ plugin: 'agenda', key: 'focus' } as const, '')

const str = (v: unknown): string | undefined => (typeof v === 'string' && v.trim() !== '' ? v.trim() : undefined)

async function showStatus($: EngineInterface): Promise<void> {
  const list = await read($, items)
  const decisions = list.filter(d => d.isDecision).length
  $.ui.status(list.length > 0 ? `안건 ${list.length}${decisions > 0 ? ` · 결정 ${decisions}` : ''}` : undefined)
}

function show($: EngineInterface): void {
  $.ui.open({ id: PANE, title: TITLE }).catch(() => undefined)
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'agenda', description: '이 세션의 안건(지금 주제와 남은 항목)을 pane으로 보여줍니다 (close: 닫기)', argumentHint: '[close]' })
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
    await showStatus($)
    if ((await read($, items)).length > 0 || (await read($, focus)) !== '') show($)
    return next(e)
  })

  on('command.run', { command: 'agenda' }, async ($, e) => {
    if (e.args.trim() === 'close') {
      await $.ui.close({ id: PANE })
      return { text: '안건 pane을 닫았습니다. /agenda 로 다시 엽니다.' }
    }
    await $.ui.open({ id: PANE, title: TITLE })
    return { text: '안건 pane을 열었습니다.' }
  })

  on('tool.call', { tool: 'mcp__agenda__agenda_add' }, async ($, e) => {
    const input = e as unknown as Record<string, unknown>
    const id = str(input.id)
    const title = str(input.title)
    if (!id || !title) return { deny: 'id and title are required.' }
    const one: Item = { id, title, detail: str(input.detail), isDecision: input.decision === true }
    await update($, items, list => (list.some(d => d.id === id) ? list.map(d => (d.id === id ? one : d)) : [...list, one]))
    await showStatus($)
    show($)
    return { result: `Listed "${id}".` }
  })

  on('tool.call', { tool: 'mcp__agenda__agenda_resolve' }, async ($, e) => {
    const input = e as unknown as Record<string, unknown>
    const id = str(input.id)
    const answer = str(input.answer)
    if (!id || !answer) return { deny: 'id and answer are required.' }
    if (!(await read($, items)).some(d => d.id === id)) return { deny: `No item "${id}".` }
    await update($, items, list => list.filter(d => d.id !== id))
    await showStatus($)
    return { result: `Resolved "${id}".` }
  })

  on('tool.call', { tool: 'mcp__agenda__agenda_focus' }, async ($, e) => {
    const topic = str((e as unknown as Record<string, unknown>).topic) ?? ''
    await update($, focus, () => topic)
    if (topic) show($)
    return { result: topic ? `Focus: ${topic}` : 'Focus cleared.' }
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
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
    // A page of whole items that fits the body, one row kept for the focus line and one for the paging buttons.
    const rows = Math.max(3, (e.props.scroll?.bodyRows ?? e.viewport?.rows ?? 24) - 1 - (now ? 1 : 0))
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
        {open.slice(first, last).map((d, i) => (
          <Box flexDirection="column" key={`o-${d.id}`}>
            <Text bold>
              {first + i + 1}. {d.isDecision ? '[결정] ' : ''}
              {d.title}
            </Text>
            {d.detail ? <Text dimColor>{`   ${d.id} · ${d.detail}`}</Text> : null}
          </Box>
        ))}
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
  })
}
