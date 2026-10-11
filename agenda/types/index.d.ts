export type Item = {
  id: string
  title: string
  detail?: string
  isDecision: boolean
}

declare module 'claude-code' {
  interface PluginState {
    agenda: { items: Item[]; start: number; focus: string }
  }
}
