import { expect, mock, test } from 'claude-code/testing'
import type { On } from 'claude-code'

// What the plugin calls beneath it: a session id, a store, a clock, the UI calls it does not await a drawing of.
// `open` answers `ui.open`, which a test replaces to see a pane wait undrawn.
const world = (on: On, open: unknown = undefined) => {
  on('session.id', async () => ({ value: 's1' }))
  mock.store(on)
  mock.clock(on)
  for (const ev of ['ui.status', 'ui.close'] as const) on(ev, async () => ({ value: undefined }) as never)
  on('ui.open', async () => ({ value: open }) as never)
}

const props = { title: '안건', isFocused: false, bodyColumns: 80, placement: 'dock', scroll: undefined } as never

test('lists an added item, marks a decision, and drops it once resolved', async ($, on) => {
  world(on)
  for (const surface of ['terminal', 'desktop'] as const) {
    const id = `d-${surface}`
    await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: `a-${surface}`, id, title: '로그 회전 한도', detail: '10MB / 50MB', decision: true } as never)
    const ui = await $.ui.mount({ plugin: 'agenda', surface, component: 'Pane', props, requestId: 'agenda' })
    expect(await ui.find({ text: /🚦 로그 회전 한도/ })).toBeDefined()
    await $.tool.call({ tool: 'mcp__agenda__agenda_resolve', tool_use_id: `r-${surface}`, id, answer: '50MB' } as never)
    expect(await ui.find({ text: /로그 회전 한도/ })).toBeUndefined()
    await ui.unmount()
  }
})

test('focuses a listed item by its number and shows it on top', async ($, on) => {
  world(on)
  await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: 'a', id: 'log', title: '로그 회전 한도' } as never)
  const added = await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: 'b', id: 'jira', title: 'Jira 쓰기 테스트' } as never)
  expect(JSON.stringify(added)).toContain('number 2')
  await $.tool.call({ tool: 'mcp__agenda__agenda_focus', tool_use_id: 'f', number: 2 } as never)
  const ui = await $.ui.mount({ plugin: 'agenda', surface: 'terminal', component: 'Pane', props, requestId: 'agenda' })
  expect(await ui.find({ text: /🎯 Jira 쓰기 테스트/ })).toBeDefined()
  await ui.unmount()
})

test('refuses to focus a number that is not listed', async ($, on) => {
  world(on)
  expect(JSON.stringify(await $.tool.call({ tool: 'mcp__agenda__agenda_focus', tool_use_id: 'e', number: 1 } as never))).toContain('agenda_add')
  await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: 'a', id: 'log', title: '로그 회전 한도' } as never)
  const r = await $.tool.call({ tool: 'mcp__agenda__agenda_focus', tool_use_id: 'f', number: 3 } as never)
  expect(JSON.stringify(r)).toContain('No item number 3')
  const ui = await $.ui.mount({ plugin: 'agenda', surface: 'terminal', component: 'Pane', props, requestId: 'agenda' })
  expect(await ui.find({ text: /🎯/ })).toBeUndefined()
  await ui.unmount()
})

test('agenda_unfocus clears the focus, and resolving the focused item clears it too', async ($, on) => {
  world(on)
  await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: 'a', id: 'log', title: '로그 회전 한도' } as never)
  await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: 'b', id: 'ci', title: 'CI 캐시' } as never)
  const ui = await $.ui.mount({ plugin: 'agenda', surface: 'terminal', component: 'Pane', props, requestId: 'agenda' })
  await $.tool.call({ tool: 'mcp__agenda__agenda_focus', tool_use_id: 'f1', number: 1 } as never)
  expect(await ui.find({ text: /🎯 로그 회전 한도/ })).toBeDefined()
  expect(JSON.stringify(await $.tool.call({ tool: 'mcp__agenda__agenda_unfocus', tool_use_id: 'u' } as never))).toContain('Focus cleared')
  expect(await ui.find({ text: /🎯/ })).toBeUndefined()
  await $.tool.call({ tool: 'mcp__agenda__agenda_focus', tool_use_id: 'f2', number: 2 } as never)
  const r = await $.tool.call({ tool: 'mcp__agenda__agenda_resolve', tool_use_id: 'r', id: 'ci', answer: '켬' } as never)
  expect(JSON.stringify(r)).toContain('focus is cleared')
  expect(await ui.find({ text: /🎯/ })).toBeUndefined()
  await ui.unmount()
})

test('/agenda unfocus clears the topic and tells the model', async ($, on) => {
  world(on)
  const rows = mock.session(on)
  expect(JSON.stringify(await $.command.run({ command: 'agenda', args: 'unfocus' } as never))).toContain('없습니다')
  await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: 'a', id: 'log', title: '로그 회전 한도' } as never)
  await $.tool.call({ tool: 'mcp__agenda__agenda_focus', tool_use_id: 'f', number: 1 } as never)
  expect(JSON.stringify(await $.command.run({ command: 'agenda', args: 'unfocus' } as never))).toContain('해제했습니다')
  expect(JSON.stringify(rows.appended().at(-1))).toContain('해제했습니다')
  const ui = await $.ui.mount({ plugin: 'agenda', surface: 'terminal', component: 'Pane', props, requestId: 'agenda' })
  expect(await ui.find({ text: /🎯/ })).toBeUndefined()
  await ui.unmount()
})

test('agenda_list reads the numbers, ids and focus without changing them', async ($, on) => {
  // A pane that waits undrawn: a call that opens it says so in its answer.
  world(on, { isPlaced: false, reason: 'unasked below 144 columns (80 now)' })
  expect(JSON.stringify(await $.tool.call({ tool: 'mcp__agenda__agenda_list', tool_use_id: 'l0' } as never))).toContain('The list is empty')
  await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: 'a', id: 'log', title: '로그 회전 한도', detail: '10MB / 50MB', decision: true } as never)
  await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: 'b', id: 'ci', title: 'CI 캐시' } as never)
  await $.tool.call({ tool: 'mcp__agenda__agenda_focus', tool_use_id: 'f', number: 2 } as never)
  const r = JSON.stringify(await $.tool.call({ tool: 'mcp__agenda__agenda_list', tool_use_id: 'l1' } as never))
  expect(r).toContain('1. 🚦 로그 회전 한도 (log) — 10MB / 50MB')
  expect(r).toContain('2. CI 캐시 (ci)\\nFocus: number 2.')
  expect(r).not.toContain('not drawn')
  await $.tool.call({ tool: 'mcp__agenda__agenda_unfocus', tool_use_id: 'u' } as never)
  expect(JSON.stringify(await $.tool.call({ tool: 'mcp__agenda__agenda_list', tool_use_id: 'l2' } as never))).toContain('Nothing is focused.')
  const ui = await $.ui.mount({ plugin: 'agenda', surface: 'terminal', component: 'Pane', props, requestId: 'agenda' })
  expect(await ui.find({ text: /🎯/ })).toBeUndefined()
  await ui.unmount()
})

test('refuses to resolve an unknown id', async ($, on) => {
  world(on)
  const r = await $.tool.call({ tool: 'mcp__agenda__agenda_resolve', tool_use_id: 'x', id: 'nope', answer: 'y' } as never)
  expect(JSON.stringify(r)).toContain('No item')
})

test('pages through more items than the body holds', async ($, on) => {
  world(on)
  for (let i = 1; i <= 12; i++) await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: `p${i}`, id: `p${i}`, title: `항목 ${i}`, detail: 'd' } as never)
  const small = { ...(props as object), scroll: { offset: 0, bodyRows: 7 } } as never
  const ui = await $.ui.mount({ plugin: 'agenda', surface: 'terminal', component: 'Pane', props: small, requestId: 'agenda' })
  expect(await ui.find({ text: /^항목 1$/ })).toBeDefined()
  expect(await ui.find({ text: /항목 4/ })).toBeUndefined()
  await ui.press({ key: 'next' })
  expect(await ui.find({ text: /^항목 4$/ })).toBeDefined()
  await ui.press({ key: 'prev' })
  expect(await ui.find({ text: /^항목 1$/ })).toBeDefined()
})

test('/agenda close closes the pane', async ($, on) => {
  world(on)
  const r = await $.command.run({ command: 'agenda', args: 'close' } as never)
  expect(JSON.stringify(r)).toContain('닫았습니다')
})

test('pressing an item asks first, then makes it the current topic and tells the model', async ($, on) => {
  world(on)
  on('ui.focus', async () => ({}) as never)
  const rows = mock.session(on)
  await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: 'a', id: 'log', title: '로그 회전 한도' } as never)
  await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: 'b', id: 'ci', title: 'CI 캐시' } as never)
  const ui = await $.ui.mount({ plugin: 'agenda', surface: 'terminal', component: 'Pane', props, requestId: 'agenda' })
  await ui.press({ key: 'pick-ci' })
  expect(await ui.find({ text: /CI 캐시"을\(를\) 지금 주제로/ })).toBeDefined()
  await ui.press({ key: 'cancel' })
  expect(await ui.find({ text: /지금 주제로/ })).toBeUndefined()
  expect(rows.appended()).toHaveLength(0)
  await ui.press({ key: 'pick-ci' })
  await ui.press({ key: 'confirm' })
  expect(await ui.find({ text: /🎯 CI 캐시/ })).toBeDefined()
  expect(JSON.stringify(rows.appended().at(-1))).toContain('CI 캐시')
  // The topic itself pressed again asks nothing and tells the model nothing more.
  await ui.press({ key: 'pick-ci' })
  expect(await ui.find({ text: /지금 주제로/ })).toBeUndefined()
  expect(rows.appended()).toHaveLength(1)
  await ui.unmount()
})

test('/agenda <number|id> picks an item without asking', async ($, on) => {
  world(on)
  const rows = mock.session(on)
  await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: 'a', id: 'log', title: '로그 회전 한도' } as never)
  await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: 'b', id: 'ci', title: 'CI 캐시' } as never)
  expect(JSON.stringify(await $.command.run({ command: 'agenda', args: '2' } as never))).toContain('CI 캐시')
  expect(JSON.stringify(await $.command.run({ command: 'agenda', args: 'log' } as never))).toContain('로그 회전 한도')
  expect(JSON.stringify(await $.command.run({ command: 'agenda', args: '9' } as never))).toContain('없습니다')
  expect(rows.appended()).toHaveLength(2)
  const ui = await $.ui.mount({ plugin: 'agenda', surface: 'terminal', component: 'Pane', props, requestId: 'agenda' })
  expect(await ui.find({ text: /🎯 로그 회전 한도/ })).toBeDefined()
  await ui.unmount()
})

test('tells the model when the pane waits undrawn', async ($, on) => {
  world(on, { isPlaced: false, reason: 'unasked below 144 columns (80 now)' })
  const r = await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: 'u', id: 'u', title: '안 보이는 안건' } as never)
  expect(JSON.stringify(r)).toContain('not drawn (unasked below 144 columns (80 now))')
  expect(JSON.stringify(r)).toContain('/agenda')
})

test('/agenda says when the pane it opened is not drawn', async ($, on) => {
  world(on, { isPlaced: false, reason: 'no attached surface places panes' })
  const r = await $.command.run({ command: 'agenda', args: '' } as never)
  expect(JSON.stringify(r)).toContain('그려지지 않았습니다: no attached surface places panes')
})
