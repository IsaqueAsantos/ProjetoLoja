# 🧾 Projeto Zake  
### Sistema Desktop de Pedidos e Gestão de Itens

> Aplicação desktop desenvolvida em **Python + Tkinter**, focada em controle de pedidos, cadastro de produtos e fechamento de caixa, com interface moderna, modular e de fácil manutenção.

---

## ✨ Visão Geral

O **Projeto Zake** é um sistema pensado para atender rotinas comuns de um ponto de venda (PDV), oferecendo:

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
│   ├── pedidos_view.py
│   ├── novo_pedido.py
│   └── itens_view.py
├── data/
│   └── itens.json
├── .gitignore
└── README.md
