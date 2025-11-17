# 🏭 Mix Shop API - Arquitetura Hexagonal

API de Gestão da Mix Shop - Sistema Integrado de Controle de Produção, Separação, Impressão 3D e Expedição.

## 📐 Arquitetura Hexagonal (Ports & Adapters)

Este projeto segue os princípios da **Arquitetura Hexagonal**, também conhecida como Ports & Adapters, garantindo:

- ✅ **Desacoplamento** total entre camadas
- ✅ **Testabilidade** facilitada
- ✅ **Manutenibilidade** e escalabilidade
- ✅ **Princípios SOLID** aplicados
- ✅ **Independência** de frameworks e bibliotecas externas

### 🎯 Camadas da Arquitetura

```
┌─────────────────────────────────────────────────┐
│              WEB (Controllers)                   │
│  ┌───────────────────────────────────────────┐  │
│  │  pedido_controller.py                     │  │
│  │  producao_controller.py                   │  │
│  │  tiny_controller.py                       │  │
│  └───────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────┘
                     │
         ┌───────────▼───────────┐
         │   DOMAIN (Núcleo)     │
         │  ┌─────────────────┐  │
         │  │   Use Cases     │  │
         │  ├─────────────────┤  │
         │  │   Interfaces    │  │ ◄── Portas (Ports)
         │  ├─────────────────┤  │
         │  │   Entities      │  │
         │  └─────────────────┘  │
         └───────────┬───────────┘
                     │
┌────────────────────▼────────────────────────────┐
│           ADAPTERS (Implementações)             │
│  ┌───────────────────────────────────────────┐  │
│  │  pedido_repository.py (Mockado)           │  │
│  │  tiny_adapter.py (Integração Tiny ERP)    │  │
│  └───────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

## 📁 Estrutura do Projeto

```
mix-shop-api/
├── src/
│   ├── config.py                    # Configurações da aplicação
│   ├── main.py                      # Aplicação FastAPI
│   │
│   ├── domain/                      # 🎯 DOMÍNIO (Regras de Negócio)
│   │   ├── entities.py              # Entidades do domínio
│   │   ├── interfaces/              # Portas (Interfaces/Contratos)
│   │   │   ├── pedido_repository.py
│   │   │   └── tiny_gateway.py
│   │   ├── usecases/                # Casos de Uso
│   │   │   ├── pedido_usecase.py
│   │   │   └── tiny_usecase.py
│   │   └── actions/                 # Actions (lógica adicional)
│   │       └── pedido_actions.py
│   │
│   ├── adapters/                    # 🔌 ADAPTADORES (Implementações)
│   │   ├── repositories/
│   │   │   └── pedido_repository.py # Implementação do repositório
│   │   └── tiny/
│   │       └── tiny_adapter.py      # Implementação gateway Tiny
│   │
│   └── web/                         # 🌐 WEB (Controllers)
│       ├── pedido_controller.py
│       ├── producao_controller.py
│       └── tiny_controller.py
│
├── requirements.txt
├── .env.example
└── README.md
```

## 🚀 Como Executar

### 1. Pré-requisitos

- Python 3.10+
- pip

### 2. Instalação

```bash
# Clone o repositório
git clone <seu-repo>
cd mix-shop-api

# Crie ambiente virtual
python -m venv venv

# Ative o ambiente
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

### 3. Configuração

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o .env com suas configurações (opcional)
```

### 4. Execute a API

```bash
# Modo desenvolvimento (com reload)
uvicorn src.main:app --reload

# ou diretamente
python src/main.py
```

A API estará disponível em: **http://localhost:8000**

## 📚 Documentação Interativa

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🎯 Endpoints Principais

### 📦 Pedidos

```
GET    /pedidos/                  # Lista todos os pedidos
GET    /pedidos/{id}              # Busca pedido por ID
GET    /pedidos/metrics           # Métricas do dashboard
GET    /pedidos/status/{status}   # Filtra por status
POST   /pedidos/                  # Cria novo pedido
PATCH  /pedidos/{id}              # Atualiza status
DELETE /pedidos/{id}              # Remove pedido
```

### 🏭 Produção

```
GET    /producao/fila                    # Fila de produção
GET    /producao/status-overview         # Visão geral dos status
GET    /producao/prioridades             # Pedidos prioritários
GET    /producao/em-andamento            # Pedidos em impressão
GET    /producao/prontos-embalar         # Prontos para embalar
GET    /producao/prontos-enviar          # Prontos para envio
```

### 🔗 Tiny ERP

```
GET    /tiny/separacoes                  # Lista separações do Tiny
GET    /tiny/separacoes/{id}             # Busca separação por ID
POST   /tiny/importar-separacoes         # Importa separações para pedidos
GET    /tiny/sync-status                 # Status da sincronização
```

## 📊 Dados Mockados

A API vem com dados mockados prontos para teste:

### Pedidos Iniciais

```json
[
  {
    "id": 1,
    "sku": "MIX-TSH-001-P",
    "codigo": "1001",
    "descricao": "Camiseta Lisa Preta -P",
    "status": "Pendente"
  },
  {
    "id": 2,
    "sku": "MIX-CAN-002-G",
    "codigo": "1002",
    "descricao": "Caneca Branca -G",
    "status": "Imprimindo"
  }
  // ... mais 4 pedidos
]
```

### Separações do Tiny ERP

5 separações mockadas com base nos dados reais fornecidos.

## 🧪 Testando a API

### Exemplo: Listar Pedidos

```bash
curl http://localhost:8000/pedidos/
```

### Exemplo: Obter Métricas

```bash
curl http://localhost:8000/pedidos/metrics
```

### Exemplo: Criar Pedido

```bash
curl -X POST http://localhost:8000/pedidos/ \
  -H "Content-Type: application/json" \
  -d '{
    "sku": "MIX-NEW-001",
    "codigo": "2001",
    "descricao": "Novo Produto",
    "status": "Pendente"
  }'
```

### Exemplo: Importar do Tiny

```bash
curl -X POST "http://localhost:8000/tiny/importar-separacoes?usar_mock=true"
```

## 🏗️ Arquitetura Hexagonal - Explicação

### 🎯 Domain (Núcleo)

O **domínio** contém as regras de negócio e é **independente** de qualquer framework ou biblioteca externa.

- **Entities**: Modelos de dados puros (`Pedido`, `Separacao`, `Item`)
- **Interfaces**: Contratos que definem **o que** precisa ser feito (Ports)
- **Use Cases**: Implementam as regras de negócio

### 🔌 Adapters (Implementações)

Os **adaptadores** implementam as interfaces definidas no domínio.

- **Repositories**: Implementam persistência de dados
- **Gateways**: Implementam integrações externas (Tiny ERP)

### 🌐 Web (Controllers)

A camada **web** é o ponto de entrada da aplicação.

- **Controllers**: Recebem requisições HTTP e chamam os Use Cases

### ✅ Benefícios

1. **Testabilidade**: Fácil criar mocks das interfaces
2. **Manutenibilidade**: Mudanças em uma camada não afetam as outras
3. **Escalabilidade**: Fácil adicionar novos adaptadores
4. **Independência**: O domínio não conhece frameworks

## 🔄 Status dos Pedidos

- `Pendente`: Pedido recém criado, aguardando impressão
- `Imprimindo`: Pedido em processo de impressão 3D
- `Parcial`: Parte do pedido concluída
- `Concluído`: Impressão finalizada
- `Embalado`: Pronto para expedição
- `Enviado`: Enviado para cliente

## 🚀 Próximos Passos (Fase 2+)

- [ ] Implementar banco de dados (Supabase)
- [ ] Adicionar autenticação JWT
- [ ] Implementar controle de impressoras 3D
- [ ] Adicionar gestão de estoque
- [ ] Criar módulo de expedição
- [ ] Implementar Business Intelligence

## 📝 Licença

MIT
