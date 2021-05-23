inoremap <C-H> <Left>
inoremap <C-L> <Right>
inoremap <C-J> <Down>
inoremap <C-K> <Up>
noremap <S-BS> <C-W>

if has("nvim-0.5")
	inoremap <c-space> <C-N>
	inoremap <c-s-space> <C-P>
endif

let g:JollyTransparentBackground = 0
colo jolly

if exists('g:GuiLoaded')
	GuiTabline 0
	GuiPopupmenu 0
	GuiFont! Hack NF:h12
endif
