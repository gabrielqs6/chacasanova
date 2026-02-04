# 🗄️ Configurando PostgreSQL para Produção

## Por que PostgreSQL?

O SQLite usa um arquivo local (`casa_nova.db`) que é **apagado** a cada novo deploy no Railway. Para manter seus dados entre deploys, você precisa usar um banco de dados persistente como o PostgreSQL.

## ✅ Benefícios

- 🔒 **Dados permanentes** - Suas reservas não serão perdidas após atualizações
- 🚀 **Performance** - Melhor para produção
- 💚 **Gratuito no Railway** - Plano gratuito oferece PostgreSQL

---

## 📋 Passo a Passo: Configurar PostgreSQL no Railway

### 1️⃣ Adicionar PostgreSQL ao Projeto

1. Acesse seu projeto no Railway: https://railway.app/
2. Clique em **"New"** → **"Database"** → **"Add PostgreSQL"**
3. O Railway criará automaticamente um banco PostgreSQL

### 2️⃣ Conectar o App ao Banco de Dados

**O Railway faz isso automaticamente!** 

Ele cria uma variável de ambiente chamada `DATABASE_URL` que o app já está configurado para usar.

### 3️⃣ Fazer Deploy das Mudanças

1. Faça commit das alterações:
   ```bash
   git add .
   git commit -m "Adicionar suporte a PostgreSQL"
   git push
   ```

2. O Railway detectará automaticamente e fará o deploy

### 4️⃣ Verificar se Funcionou

1. Acesse seu app: `https://seu-app.up.railway.app/`
2. Vá ao admin: `https://seu-app.up.railway.app/admin?key=gabrielqueiroz2026`
3. Adicione um item de teste
4. Faça um novo deploy (push para git)
5. ✅ O item deve continuar lá!

---

## 🔍 Como Funciona

O código agora detecta automaticamente:

- **Local (desenvolvimento):** Usa SQLite (`casa_nova.db`)
  - ✅ Cria dados de exemplo automaticamente
  - ✅ Perfeito para testar

- **Produção (Railway):** Usa PostgreSQL
  - ✅ Banco de dados permanente
  - ✅ Não cria dados de exemplo
  - ✅ Seus dados ficam seguros

---

## 📊 Ver os Dados do PostgreSQL

### Opção 1: Usar o Railway Dashboard

1. No Railway, clique no serviço **PostgreSQL**
2. Vá em **"Data"**
3. Você verá todos os seus itens

### Opção 2: Conectar com Cliente PostgreSQL

No Railway, clique em PostgreSQL → **"Connect"** e copie as credenciais:

- Host
- Port
- Database
- Username
- Password

Use essas credenciais em um cliente como:
- [pgAdmin](https://www.pgadmin.org/)
- [DBeaver](https://dbeaver.io/)
- VS Code com extensão PostgreSQL

---

## 🧪 Testar Localmente com PostgreSQL (Opcional)

Se você quiser testar PostgreSQL localmente antes de fazer deploy:

1. Instale PostgreSQL: https://www.postgresql.org/download/
2. Crie um banco de dados local
3. Adicione a variável de ambiente:
   ```bash
   $env:DATABASE_URL="postgresql://usuario:senha@localhost:5432/casa_nova"
   ```
4. Execute o app:
   ```bash
   python app.py
   ```

---

## 🆘 Problemas Comuns

### Erro: "No module named 'psycopg2'"

**Solução:** Instale as dependências:
```bash
pip install -r requirements.txt
```

### Dados ainda desaparecem após deploy

**Verifique:**
1. PostgreSQL está rodando no Railway?
2. A variável `DATABASE_URL` está configurada?
3. Faça um novo deploy após adicionar o PostgreSQL

### "Connection refused" ou "Could not connect"

**Causa:** PostgreSQL não está acessível

**Solução:**
1. Certifique-se de que o serviço PostgreSQL está rodando no Railway
2. Verifique se a variável `DATABASE_URL` está correta

---

## 📝 Resumo

✅ **Antes:** SQLite → Dados apagados a cada deploy  
✅ **Agora:** PostgreSQL → Dados permanentes

**Próximos passos:**
1. Adicionar PostgreSQL no Railway
2. Fazer push do código atualizado
3. Pronto! Seus dados estarão seguros 🎉
