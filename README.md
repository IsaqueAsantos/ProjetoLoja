# 🧾 Projeto Loja
### Sistema Desktop de Pedidos e Gestão de Itens

> Aplicação desktop desenvolvida em **Python + Tkinter**, focada em controle de pedidos, cadastro de produtos e fechamento de caixa, com interface moderna, modular e de fácil manutenção.

---

## ✨ Visão Geral

O **Projeto Loja** é um sistema pensado para atender rotinas comuns de um ponto de venda (PDV), oferecendo:

- navegação simples e intuitiva  
- organização visual consistente  
- persistência de dados via JSON  
- estrutura preparada para evolução futura  

---

## 🏠 Menu Principal

### 🔹 Funcionalidades

- **📦 Ir para Pedidos**  
  Acessa o menu de pedidos para registro e controle de vendas.

- **📋 Itens Registrados**  
  Exibe todos os produtos cadastrados no sistema.

- **➕ Cadastrar Novo Item**  
  Acessa o menu de cadastro de novos produtos.

- **🔐 Fechamento de Caixa**  
  Permite pesquisar notas fiscais já emitidas para reimpressão.  
  > ⚠️ **Menu protegido por senha.**

- **🖼️ Background Personalizado**  
  Permite definir uma imagem `.jpg` ou `.png` como plano de fundo da aplicação.

---

## ⚙️ Implementações Técnicas

- 🔄 **Atualização de DLLs via GitHub**  
  Botão dedicado para atualizar dependências diretamente do repositório.

- 🧩 Arquitetura modular (`views`)  
  Facilita manutenção, leitura e evolução do sistema.

- 🎨 Padronização visual  
  Fontes, cores e botões seguem identidade única em todo o app.

---

## 🆕 Menu — Cadastrar Novo Item

### 🔹 Funcionalidades

- **🏷️ Tipo de Produto**  
  Checkbox para seleção:
  - `Cigarros`
  - `Outros`

- **📝 Nome do Item**  
  - Entrada de texto  
  - Conversão automática para **letras maiúsculas**

- **💰 Valor da Unidade**  
  - Formatação monetária automática  
  - Exemplo: `R$ 2,00`

- **📦 Valor do Atacado**
  - Editável para produtos comuns  
  - Para **cigarros**:
    - campo bloqueado
    - cálculo automático (`valor da unidade × 10`)

- **🏷️ Aplicar Desconto**
  - Checklist:
    - `Sim`
    - `Não`

- **💾 Cadastrar**
  - Salva os dados em arquivo `.json`
  - Gera um **ID aleatório** para o item

- **⬅️ Menu**
  - Retorna ao menu principal

- **🖼️ Background Personalizado**
  - Suporte a imagens `.jpg` e `.png`

---

## 📋 Menu — Itens Registrados

### 🔹 Funcionalidades

- Leitura do arquivo `.json` com os itens cadastrados
- Exibição dos dados em uma **Treeview**

- **✏️ Editar Item**
  - Permite edição do item selecionado
  - Caso nenhum item esteja selecionado, o sistema exibe uma mensagem de aviso

- **🔄 Atualizar Lista**
  - Recarrega o `.json`
  - Atualiza a lista com novos itens cadastrados

- **⬅️ Menu**
  - Retorna ao menu principal

---

## 🛒 Menu — Pedidos

### 🔹 Funcionalidades

- **🔍 Nome do Item**
  - Campo com **autocomplete**
  - Filtra itens conforme a digitação

- **🔢 Quantidade**
  - Aceita **apenas valores numéricos**

- **➕ Adicionar ao Pedido**
  - Busca o item no `.json`
  - Calcula o valor (`Quantidade × Valor da Unidade`)
  - Adiciona o item à Treeview do pedido
  - Se o item possuir desconto:
    - aplica **5% de desconto** automaticamente

---

## 🗂️ Estrutura do Projeto

```text
ProjetoZake/
├── script.py
├── views/
│   ├── __init__.py
│   ├── home_view.py
│   ├── pedido_view.py
│   ├── novo_pedido_view.py
│   └── itens_view.py
├── data/
│   └── itens.json
├── .gitignore
└── README.md

usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--no-lazy-fetch]
           [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]
           [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>]    
           <command> [<args>]       

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)       
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   restore    Restore working tree files
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   diff       Show changes between commits, commit and working tree, etc
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   backfill   Download missing objects in a partial clone
   branch     List, create, or delete branches
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   reset      Reset current HEAD to the specified state
   switch     Switch branches
   tag        Create, list, delete or verify tags

collaborate (see also: git help workflows)
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects
