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
}
