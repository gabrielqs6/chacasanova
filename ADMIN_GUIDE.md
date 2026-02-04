# 🔧 Guia do Administrador - Chá de Casa Nova

## 🔐 Como Acessar o Painel Admin

### Passo 1: Acesse a URL do Admin

**Local (computador):**
```
http://localhost:5000/admin?key=gabrielqueiroz2026
```

**Produção (Railway):**
```
https://seu-app.up.railway.app/admin?key=gabrielqueiroz2026
```

⚠️ **IMPORTANTE:** Guarde este link com segurança! Qualquer pessoa com este link pode gerenciar a lista de presentes.

---

## 📋 O Que Você Pode Fazer no Admin

### 1️⃣ Ver Quem Reservou Cada Item

No painel admin, você verá uma lista completa de todos os itens com:
- ✅ Nome do item
- 📁 Categoria
- 🎯 Status atual (Disponível / Reservado / Já temos)
- 👤 **"Reservado por"** - Mostra o nome da pessoa que reservou

### 2️⃣ Adicionar Novos Itens

No topo da página admin, há um formulário "➕ Adicionar Novo Item":

1. **Nome do Item*** (obrigatório)
   - Ex: "Jogo de Panelas", "Toalhas de Banho"

2. **Categoria*** (obrigatório)
   - Escolha: Cozinha, Quarto, Banheiro, Limpeza, Lavanderia, Sala, Outros

3. **Notas / Descrição** (opcional)
   - Adicione detalhes como cor, tamanho, marca sugerida, etc.
   - Ex: "Preferência: cor azul ou branca"

4. **Link de Sugestão de Loja** (opcional)
   - Cole o link onde os convidados podem encontrar o produto
   - Ex: "https://www.magazineluiza.com.br/panelas"
   - 💡 Este link aparecerá na página de detalhes do item

5. Clique em **"Adicionar Item"**

✅ O item aparecerá imediatamente na lista pública!

### 3️⃣ Editar Itens Existentes

Para cada item na lista, você pode:
- 📝 Editar o nome
- 📁 Mudar a categoria
- ✏️ Adicionar/modificar notas
- � Adicionar/editar link de sugestão de loja
- �🔄 Alterar o status:
  - **Disponível** - Aparece na lista para reserva
  - **Reservado** - Alguém já reservou
  - **Já temos** - Vocês já compraram (aparece na página "Já temos 💚")

Clique em **"💾 Salvar"** para confirmar as mudanças.

### 4️⃣ Excluir Itens

Clique em **"🗑️ Excluir"** ao lado do item que deseja remover.

⚠️ **Atenção:** Esta ação não pode ser desfeita!

---

## 📊 Ver Todas as Reservas de Uma Vez

No painel admin, role para baixo até "📋 Todos os Itens". Lá você verá:

- **Itens Disponíveis:** Campo "Reservado por" mostra "N/A"
- **Itens Reservados:** Campo "Reservado por" mostra o nome da pessoa

### Exemplo:
```
Item: Conjunto de Panelas
Status: Reservado
Reservado por: Maria Silva
```

---

## 💡 Dicas Úteis

### ✅ Quando Alguém Reservar Fora do Sistema

Se alguém reservar um presente pessoalmente ou por WhatsApp:

1. Vá ao admin
2. Encontre o item
3. Mude o status para **"Reservado"**
4. Clique em "💾 Salvar"

**Nota:** O campo "Reservado por" só é preenchido automaticamente quando alguém reserva pelo site.

### ✅ Marcar Itens que Vocês Já Têm

1. Vá ao admin
2. Encontre o item
3. Mude o status para **"Já temos"**
4. Clique em "💾 Salvar"

O item sumirá da lista principal e aparecerá na página "Já temos 💚".

### ✅ Liberar um Item Reservado

Se alguém desistir da reserva:

1. Vá ao admin
2. Encontre o item
3. Mude o status para **"Disponível"**
4. Clique em "💾 Salvar"

O item voltará a aparecer como disponível para outros convidados.

---

## 🔗 Links Rápidos

### Para Convidados (compartilhar):
- **Página inicial:** `https://seu-app.up.railway.app/`
- **Lista de presentes:** `https://seu-app.up.railway.app/list`

### Para Você (NÃO compartilhar):
- **Admin:** `https://seu-app.up.railway.app/admin?key=gabrielqueiroz2026`

---

## 🆘 Problemas Comuns

### "Acesso negado. Chave de admin inválida"
- Certifique-se de que está usando `?key=gabrielqueiroz2026` no final da URL
- A chave é case-sensitive (maiúsculas/minúsculas importam)

### Não consigo ver as mudanças
- Atualize a página (F5 ou Ctrl+R)
- Limpe o cache do navegador

### Esqueci o link do admin
- O link está neste documento
- Você também pode acessar: `seu-site/admin?key=gabrielqueiroz2026`

---

## 📱 Acessando do Celular

O painel admin funciona perfeitamente no celular! Basta:
1. Abrir o navegador do celular
2. Digitar ou colar o link do admin
3. Usar normalmente

**Dica:** Salve o link nos favoritos do navegador para acesso rápido!

---

## 🔐 Segurança

### Alterar a Chave de Admin (Recomendado para produção)

Se você está usando Railway ou outro serviço de hospedagem:

1. Vá nas configurações do projeto
2. Adicione uma variável de ambiente:
   - Nome: `ADMIN_KEY`
   - Valor: `suaChaveSecretaAqui123!`
3. Salve e reinicie o app

Agora o link do admin será:
```
https://seu-app.up.railway.app/admin?key=suaChaveSecretaAqui123!
```

---

**Pronto! Agora vocês têm controle total sobre a lista de presentes! 🎉**
