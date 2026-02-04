# 🔐 Guia de Acesso Administrativo

## Como Acessar o Painel Admin

### 1. URL de Acesso

**Local (desenvolvimento):**
```
http://localhost:5000/admin?key=gabrielqueiroz2026
```

**Produção (Railway):**
```
https://SEU-APP.up.railway.app/admin?key=gabrielqueiroz2026
```

> ⚠️ **Guarde este link com segurança!** Não compartilhe publicamente.

---

## 📊 O Que Você Pode Fazer no Admin

### 1. Ver Quem Reservou (Seção Principal) 🎁

Na parte superior do painel, você verá:
- **Lista de Reservas:** Mostra todos os itens reservados
- **Nome do Item** e categoria
- **Nome da Pessoa** que reservou

Exemplo:
```
🎁 Quem Reservou o Quê (2 itens reservados)

┌─────────────────────────────────────────────┐
│ Jogo de Lençóis King Size                   │
│ Quarto                         👤 Maria Silva│
└─────────────────────────────────────────────┘
```

### 2. Adicionar Novo Item ➕

Preencha o formulário:
- **Nome do Item** (obrigatório)
- **Categoria** (selecione: Cozinha, Quarto, Banheiro, etc.)
- **Notas/Descrição** (opcional - cor, tamanho, marca)

Clique em **"Adicionar Item"**

### 3. Editar Itens Existentes ✏️

Para cada item, você pode:
- Editar nome
- Mudar categoria
- Atualizar notas
- **Mudar status:**
  - `Disponível` - Aparece na lista para visitantes
  - `Reservado` - Marcado como reservado (ver quem reservou)
  - `Já temos` - Vai para página "Já temos 💚"

Clique em **"💾 Salvar"** para confirmar

### 4. Excluir Item 🗑️

Clique no botão **"🗑️ Excluir"** ao lado de qualquer item.

⚠️ **Atenção:** Esta ação não pode ser desfeita!

---

## 📋 Fluxo de Trabalho Comum

### Quando Alguém Reservar:
1. Visitante reserva um item no site
2. Acesse o painel admin
3. Veja a reserva na seção **"Quem Reservou o Quê"**
4. O item agora mostra status **"Reservado"** com o nome da pessoa

### Quando Você Comprar um Item:
1. Acesse o painel admin
2. Encontre o item na lista
3. Mude o status para **"Já temos"**
4. Salve
5. O item agora aparece na página "Já temos 💚"

### Para Liberar uma Reserva:
1. Acesse o painel admin
2. Encontre o item reservado
3. Mude o status para **"Disponível"**
4. Salve
5. O item volta a estar disponível para outros visitantes

---

## 💡 Dicas

### Organização
- Use categorias consistentes
- Adicione notas com cor, tamanho, marca sugerida
- Atualize o status assim que comprar algo

### Segurança
- Não compartilhe a URL do admin
- Use uma aba anônima se acessar em computador público
- Feche a aba após usar

### Para Visitantes
- Não precisa criar conta ou fazer login
- Reservam apenas digitando o nome
- Veem confirmação imediata

---

## 🔄 Mudando a Senha Admin

### Desenvolvimento (Local)

Edite o arquivo [app.py](../app.py) linha 7:
```python
ADMIN_KEY = os.environ.get('ADMIN_KEY', 'NOVA_SENHA_AQUI')
```

### Produção (Railway)

1. Acesse o painel do Railway
2. Vá em **Variables**
3. Mude o valor de `ADMIN_KEY`
4. Salve (app reinicia automaticamente)

---

## 📱 Acesso Mobile

O painel admin funciona perfeitamente em smartphones!

1. Abra o navegador no celular
2. Digite a URL com `?key=` sua senha
3. Gerencie tudo pelo celular

---

## ❓ Perguntas Frequentes

### Como sei quem reservou cada item?
Veja a seção **"Quem Reservou o Quê"** no topo do painel admin.

### Posso cancelar uma reserva?
Sim! Mude o status do item para **"Disponível"** e salve.

### Como adiciono vários itens de uma vez?
Use o formulário **"Adicionar Novo Item"** múltiplas vezes, preenchendo um de cada vez.

### O que acontece se eu excluir um item reservado?
O item será completamente removido do banco de dados. Use com cuidado!

### Posso ver o histórico de reservas?
Não no momento. O sistema mostra apenas o estado atual de cada item.

---

## 🆘 Suporte

Se você esqueceu a senha admin:
1. Acesse o servidor (Railway)
2. Veja as variáveis de ambiente
3. Ou edite o arquivo `app.py` localmente

---

**✅ Pronto para usar! Acesse agora:**

http://localhost:5000/admin?key=gabrielqueiroz2026

(ou substitua pela URL da produção)
