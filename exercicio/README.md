# ✅ Testes da API de Tarefas

Este documento descreve os testes implementados para a API de gerenciamento de tarefas, incluindo os critérios de validação para cada endpoint.

---

## 📋 Listar Tarefas (`GET /tarefas`)

- [ ] Verifica se o código de status retornado é **200**
- [ ] Verifica se a resposta em JSON é uma **instância de lista**
- [ ] Verifica se a lista retornada possui **pelo menos um elemento**

---

## ➕ Criar Nova Tarefa (`POST /tarefas`)

- [ ] Verifica se o código de status retornado é **201**
- [ ] Verifica se o campo `id` no JSON **não é `None`**
- [ ] Verifica se o valor da chave `"tarefa"` no JSON é **igual ao enviado na requisição**

---

## 🔍 Obter Tarefa Existente (`GET /tarefas/<id>`)

- [ ] Verifica se o código de status retornado é **200**
- [ ] Verifica se o campo `"id"` no JSON é **igual ao ID requisitado**

---

## ❌ Obter Tarefa Inexistente (`GET /tarefas/<id>`)

- [ ] Verifica se o código de status retornado é **404**
- [ ] Verifica se o JSON retornado contém a chave `"erro"`

---

## ✏️ Atualizar Tarefa Existente (`PUT /tarefas/<id>`)

- [ ] Verifica se o código de status retornado é **200**
- [ ] Verifica se o valor da chave `"tarefa"` no JSON é **igual ao enviado**
- [ ] Verifica se o valor da chave `"feito"` no JSON é **igual ao enviado**

---

## 🚫 Atualizar Tarefa Inexistente (`PUT /tarefas/<id>`)

- [ ] Verifica se o código de status retornado é **404**
- [ ] Verifica se o JSON retornado contém a chave `"erro"`

---

## 🗑️ Remover Tarefa Existente (`DELETE /tarefas/<id>`)

- [ ] Verifica se o código de status retornado ao deletar é **200**
- [ ] Verifica se ao tentar obter a tarefa deletada, o retorno é **404**

---

## ❌ Remover Tarefa Inexistente (`DELETE /tarefas/<id>`)

- [ ] Verifica se o código de status retornado é **404**
- [ ] Verifica se o JSON retornado contém a chave `"erro"`

---

## ⚠️ Campos Obrigatórios na Criação (`POST /tarefas`)

- [ ] Verifica se o código de status retornado é **400**
- [ ] Verifica se o JSON retornado contém a chave `"erro"`

---

## 🧪 Validação de Tipos de Campo

- [ ] Verifica se o código de status retornado é **400**
- [ ] Verifica se o JSON retornado contém a chave `"erro"`
