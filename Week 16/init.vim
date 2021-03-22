call plug#begin(stdpath('data'))

Plug 'junegunn/fzf', { 'do': { -> fzf#install() }}
Plug 'junegunn/fzf.vim'
"TODO: write a better plugin for this
"NOTE: probably reconsider this
Plug 'jremmen/vim-ripgrep'
Plug 'preservim/nerdtree'
"TODO: delete this
Plug 'tyru/open-browser.vim'

if !has("nvim-0.5")
	Plug 'neoclide/coc.nvim', { 'branch': 'release' }
	Plug 'jackguo380/vim-lsp-cxx-highlight'
endif

"Pretty"
Plug 'vim-airline/vim-airline'
"TODO: delete this
Plug 'vim-airline/vim-airline-themes'
Plug 'ryanoasis/vim-devicons'
Plug 'DanDanCool/JollyTheme'
"TODO: delete this
Plug 'joshdick/onedark.vim'

"Syntax"
Plug 'tikhomirov/vim-glsl'

"TODO: move this out when 0.5 becomes stable
if has("nvim-0.5")
	Plug 'neovim/nvim-lspconfig'
	Plug 'nvim-lua/completion-nvim'
	Plug 'jiangmiao/auto-pairs'
endif

"meme
Plug 'doki-theme/doki-theme-vim'

call plug#end()

set number
set clipboard=unnamed
set backspace=indent,eol,start
set noswapfile

set noexpandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4

set autoindent
set smartindent

set foldmethod=indent
set foldlevelstart=5

set ignorecase

let mapleader = "-"

syntax keyword Todo TODO NOTE IMPORTANT

"Settings for nightly build
if has("nvim-0.5")
	"nvim-lspconfig"

lua << EOF
	local lspconfig = require'lspconfig'
	lspconfig.clangd.setup{
	on_attach=require'completion'.on_attach
	}

	vim.lsp.handlers["textDocument/publishDiagnostics"] = vim.lsp.with(
	vim.lsp.diagnostic.on_publish_diagnostics, {
			underline = false,
			virtual_text = false,
			signs = false,
			update_in_insert = false
		}
	)
EOF

	"completion-nvim"
	" Use <Tab> and <S-Tab> to navigate through popup menu
	inoremap <expr> <Tab>   pumvisible() ? "\<C-n>" : "\<Tab>"
	inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"
	" Set completeopt to have a better completion experience
	set completeopt=menuone,noinsert,noselect
	let g:completion_matching_strategy_list = ["exact", "substring", "fuzzy"]

	" Avoid showing message extra message when using completion
	set shortmess+=c

	let g:completion_enable_auto_popup = 0
endif "nightly build settings"

"JollyTheme
let g:JollyTransparentBackground = 1

"airline"
let g:airline_powerline_fonts = 1
let g:airline_theme = 'dark_minimal'
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#formatter = 'unique_tail'
let g:airline_section_z = 'Ln %l, Col %c   %L'
let g:airline#extensions#tabline#show_tab_count = 0
let g:airline#extensions#tabline#tab_nr_type = 1 " tab number
let g:airline#extensions#tabline#show_close_button = 0
let g:airline#extensions#tabline#show_buffers = 0
let g:airline#extensions#tabline#show_splits = 0
let g:airline#extensions#wordcount#enabled = 0

let g:airline_filetype_overrides = {
			\'help':  [ 'Help', '%f' ],
			\'vim-plug': [ 'Plugins', '' ],
			\'nerdtree': [ 'TREE', '' ],
			\}

nmap <leader>1 <Plug>AirlineSelectTab1
nmap <leader>2 <Plug>AirlineSelectTab2
nmap <leader>3 <Plug>AirlineSelectTab3
nmap <leader>4 <Plug>AirlineSelectTab4
nmap <leader>5 <Plug>AirlineSelectTab5
nmap <leader>6 <Plug>AirlineSelectTab6
nmap <leader>7 <Plug>AirlineSelectTab7
nmap <leader>8 <Plug>AirlineSelectTab8
nmap <leader>9 <Plug>AirlineSelectTab9
nmap <leader>0 <Plug>AirlineSelectTab0

"NerdTree"
nnoremap <C-N> :NERDTreeToggle<Return>
let NERDTreeMinimalUI			= 1
let NERDTreeAutoDeleteBuffer	= 1
let NERDTreeNaturalSort			= 1
let NERDTreeChDirMode			= 2
let NERDTreeMouseMode			= 2
let NERDTreeDirArrowExpandable	= "▸"
let NERDTreeDirArrowCollapsible = "▾"

"FZF"
nnoremap <C-F> :FZF<Return>
let g:fzf_action = {
	\ 'ctrl-t': 'tab split',
	\ 'ctrl-h': 'split',
	\ 'ctrl-v': 'vsplit' }


"TODO: delete this
"OpenBrowser.vim
let g:openbrowser_search_engines = extend(
	\ get(g:, 'openbrowser_search_engines', {}),
	\ {
	\   'msdn': 'https://docs.microsoft.com/en-us/search/?terms={query}&scope=Desktop',
	\   'cpp': 'https://www.cplusplus.com/search.do?q={query}',
	\	'vk': 'https://www.khronos.org/registry/vulkan/specs/1.2-extensions/html/vkspec.html#{query}',
	\	'gl': 'https://docs.gl/gl4/',
	\	'ddg': 'https://duckduckgo.com/?q={query}'
	\ },
	\ 'keep'
	\)

nnoremap <silent> <leader>msdn :call openbrowser#smart_search(expand('<cword>'), "msdn")<cr>
nnoremap <silent> <leader>cpp :call openbrowser#smart_search(expand('<cword>'), "cpp")<cr>
nnoremap <silent> <leader>vk :call openbrowser#smart_search(expand('<cword>'), "vk")<cr>
nnoremap <silent> <leader>gl :call openbrowser#smart_search(expand('<cword>'), "gl")<cr>
nnoremap <silent> <leader>ddg :call openbrowser#smart_search(expand('<cword>'), "ddg")<cr>

"Split navigation"
nnoremap <S-H> <C-W><C-H>
nnoremap <S-J> <C-W><C-J>
nnoremap <S-K> <C-W><C-K>
nnoremap <S-L> <C-W><C-L>

nnoremap gk K

inoremap <S-Del> <Esc>dda
inoremap <C-Del> <Esc>dei

inoremap <C-S> <Esc>:w<Return>a

inoremap <A-k> <Esc>ddkkp0i
inoremap <A-j> <Esc>ddp0i

nnoremap <A-k> ddkkp
nnoremap <A-j> ddp

inoremap <C-Return> <Esc><S-O>
inoremap <S-Return> <Esc>o

inoremap <C-E> <s-right>
inoremap <C-B> <s-left>
inoremap <C-A> <Esc><S-A>

"undo and redo"
inoremap <C-Z> <Esc>ui
inoremap <C-Y> <Esc><C-R>i

nnoremap <leader>vimrc :vsplit $MYVIMRC<Return>
nnoremap <leader>rvimrc :so $MYVIMRC<Return>
nnoremap <C-/> 0i//<Esc>0
nnoremap // :noh<Return>

augroup AutoCommands
	autocmd!
	autocmd FileType python :noremap <C-/> 0i#<Esc>0
	autocmd BufWritePre * %s/\s\+$//e
	autocmd BufWinEnter * silent NERDTreeMirror
augroup END

"Coc"
if !has("nvim-0.5")
	so $HOME/appdata/local/nvim/cocinit.vim
endif
