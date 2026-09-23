" A self-contained, read-only comparison inside the navigator popup.
set background=dark
syntax enable
set laststatus=2 noshowmode noruler mouse=a
set diffopt=filler,vertical
set shortmess+=IF
highlight Normal ctermfg=252 ctermbg=235 guifg=#cdd6f4 guibg=#1e1e2e
highlight LineNr ctermfg=243 ctermbg=235 guifg=#6c7086 guibg=#1e1e2e
highlight CursorLineNr ctermfg=117 ctermbg=235 guifg=#89dceb guibg=#1e1e2e
highlight DiffAdd ctermfg=157 ctermbg=22 guifg=#a6e3a1 guibg=#234132
highlight DiffDelete ctermfg=210 ctermbg=52 guifg=#f38ba8 guibg=#472b37
highlight DiffChange ctermfg=252 ctermbg=237 guifg=#cdd6f4 guibg=#313244
highlight DiffText ctermfg=235 ctermbg=180 guifg=#1e1e2e guibg=#f9e2af
highlight StatusLine cterm=bold ctermfg=235 ctermbg=117 gui=bold guifg=#1e1e2e guibg=#89dceb
highlight StatusLineNC cterm=NONE ctermfg=250 ctermbg=238 gui=NONE guifg=#bac2de guibg=#45475a
highlight VertSplit cterm=NONE ctermfg=243 ctermbg=235 gui=NONE guifg=#6c7086 guibg=#1e1e2e
highlight Folded ctermfg=147 ctermbg=236 guifg=#b4befe guibg=#181825
silent windo setlocal number nowrap readonly nomodifiable noswapfile cursorline
silent windo let &l:statusline = ' %f  [read-only]%=%l/%L  q:Return '
nnoremap <silent> q :qa!<CR>
nnoremap <silent> <Tab> <C-w>w
silent wincmd h
