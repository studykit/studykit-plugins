export type Item = {
  id: string
  title: string
  detail?: string
  isDecision: boolean
}

export type Place = 'pane' | 'band'

declare module 'claude-code' {
  interface PluginState {
    agenda: { items: Item[]; start: number; focus: string; pending: string; place: Place; isHidden: boolean }
  }
  // The inputs of the tools the mod registers in session.start, kept in step with their inputSchema. Declared
  // here because the engine's generated MCP types list only the servers connected when they were written.
  interface McpToolInputs {
    mcp__agenda__agenda_add: { id: string; title: string; detail?: string; decision?: boolean }
    mcp__agenda__agenda_resolve: { id: string; answer: string }
    mcp__agenda__agenda_focus: { number: number }
    mcp__agenda__agenda_unfocus: {}
    mcp__agenda__agenda_list: {}
  }
}
