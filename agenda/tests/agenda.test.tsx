import { expect, mock, test } from 'claude-code/testing'
import type { On } from 'claude-code'

// What the plugin calls beneath it: a session id, a store, a clock, the UI calls it does not await a drawing of.
const world = (on: On) => {
  on('session.id', async () => ({ value: 's1' }))
  mock.store(on)
  mock.clock(on)
  for (const ev of ['ui.status', 'ui.open', 'ui.close'] as const) on(ev, async () => ({ value: undefined }) as never)
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

test('shows the current topic on top', async ($, on) => {
  world(on)
  await $.tool.call({ tool: 'mcp__agenda__agenda_focus', tool_use_id: 'f', topic: 'Jira 쓰기 테스트' } as never)
  const ui = await $.ui.mount({ plugin: 'agenda', surface: 'terminal', component: 'Pane', props, requestId: 'agenda' })
  expect(await ui.find({ text: /지금: Jira 쓰기 테스트/ })).toBeDefined()
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
  expect(await ui.find({ text: /지금: CI 캐시/ })).toBeDefined()
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
  expect(await ui.find({ text: /지금: 로그 회전 한도/ })).toBeDefined()
  await ui.unmount()
})
