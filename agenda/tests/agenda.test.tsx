import { expect, test } from 'claude-code/testing'

const props = { title: '안건', isFocused: false, bodyColumns: 80, placement: 'dock', scroll: undefined } as never

test('lists an added item, marks a decision, and drops it once resolved', async $ => {
  for (const surface of ['terminal', 'desktop'] as const) {
    const id = `d-${surface}`
    await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: `a-${surface}`, id, title: '로그 회전 한도', detail: '10MB / 50MB', decision: true } as never)
    const ui = await $.ui.mount({ plugin: 'agenda', surface, component: 'Pane', props, requestId: 'agenda' })
    expect(await ui.find({ text: /\[결정\] 로그 회전 한도/ })).toBeDefined()
    await $.tool.call({ tool: 'mcp__agenda__agenda_resolve', tool_use_id: `r-${surface}`, id, answer: '50MB' } as never)
    expect(await ui.find({ text: /로그 회전 한도/ })).toBeUndefined()
    await ui.unmount()
  }
})

test('shows the current topic on top', async $ => {
  await $.tool.call({ tool: 'mcp__agenda__agenda_focus', tool_use_id: 'f', topic: 'Jira 쓰기 테스트' } as never)
  const ui = await $.ui.mount({ plugin: 'agenda', surface: 'terminal', component: 'Pane', props, requestId: 'agenda' })
  expect(await ui.find({ text: /지금: Jira 쓰기 테스트/ })).toBeDefined()
  await ui.unmount()
})

test('refuses to resolve an unknown id', async $ => {
  const r = await $.tool.call({ tool: 'mcp__agenda__agenda_resolve', tool_use_id: 'x', id: 'nope', answer: 'y' } as never)
  expect(JSON.stringify(r)).toContain('No item')
})

test('pages through more items than the body holds', async $ => {
  for (let i = 1; i <= 12; i++) await $.tool.call({ tool: 'mcp__agenda__agenda_add', tool_use_id: `p${i}`, id: `p${i}`, title: `항목 ${i}`, detail: 'd' } as never)
  const small = { ...(props as object), scroll: { offset: 0, bodyRows: 7 } } as never
  const ui = await $.ui.mount({ plugin: 'agenda', surface: 'terminal', component: 'Pane', props: small, requestId: 'agenda' })
  expect(await ui.find({ text: /^1\. 항목 1$/ })).toBeDefined()
  expect(await ui.find({ text: /항목 4/ })).toBeUndefined()
  await ui.press({ key: 'next' })
  expect(await ui.find({ text: /^4\. 항목 4$/ })).toBeDefined()
  await ui.press({ key: 'prev' })
  expect(await ui.find({ text: /^1\. 항목 1$/ })).toBeDefined()
})

test('/agenda close closes the pane', async $ => {
  const r = await $.command.run({ command: 'agenda', args: 'close' } as never)
  expect(JSON.stringify(r)).toContain('닫았습니다')
})
