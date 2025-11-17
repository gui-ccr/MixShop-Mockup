# 📁 Estrutura Completa do Projeto Mix Shop API

## Arquitetura Hexagonal (Ports & Adapters)

```
mix-shop-api/
│
├── 📄 requirements.txt              # Dependências do projeto
├── 📄 .env.example                  # Exemplo de variáveis de ambiente
├── 📄 README.md                     # Documentação completa
│
└── src/                             # Código fonte
    ├── 📄 config.py                 # Configurações da aplicação
    ├── 📄 main.py                   # Aplicação FastAPI (Entry Point)
    │
    ├── domain/                      # 🎯 DOMÍNIO (Core/Núcleo)
    │   ├── 📄 entities.py           # Entidades: Pedido, Separacao, Item, StatusPedido
    │   │
    │   ├── interfaces/              # 🔌 PORTAS (Interfaces/Contratos)
    │   │   ├── 📄 pedido_repository.py    # Interface IPedidoRepository
    │   │   └── 📄 tiny_gateway.py         # Interface ITinyGateway
    │   │
    │   ├── usecases/                # 💼 CASOS DE USO (Regras de Negócio)
    │   │   ├── 📄 pedido_usecase.py       # Use Case de Pedidos
    │   │   └── 📄 tiny_usecase.py         # Use Case Tiny ERP
    │   │
    │   └── actions/                 # ⚡ ACTIONS (Lógica adicional)
    │       └── 📄 pedido_actions.py
    │
    ├── adapters/                    # 🔧 ADAPTADORES (Implementações)
    │   ├── repositories/
    │   │   └── 📄 pedido_repository.py    # Implementação do repositório (mockado)
    │   │
    │   └── tiny/
    │       └── 📄 tiny_adapter.py         # Implementação gateway Tiny ERP
    │
    └── web/                         # 🌐 CAMADA WEB (Controllers/API)
        ├── 📄 pedido_controller.py        # Endpoints de pedidos
        ├── 📄 producao_controller.py      # Endpoints de produção
        └── 📄 tiny_controller.py          # Endpoints Tiny ERP
```

## 📊 Fluxo de Dados

```
┌─────────────┐
│   Cliente   │
│  (Frontend) │
└──────┬──────┘
       │ HTTP Request
       ▼
┌─────────────────────────────────┐
│  WEB LAYER (Controllers)        │
│  ┌───────────────────────────┐  │
│  │ pedido_controller.py      │  │
│  │ - GET /pedidos/           │  │
│  │ - POST /pedidos/          │  │
│  │ - PATCH /pedidos/{id}     │  │
│  └───────────────────────────┘  │
└──────────────┬──────────────────┘
               │ Chama Use Case
               ▼
┌─────────────────────────────────┐
│  DOMAIN LAYER (Use Cases)       │
│  ┌───────────────────────────┐  │
│  │ pedido_usecase.py         │  │
│  │ - listar_todos_pedidos()  │  │
│  │ - criar_pedido()          │  │
│  │ - atualizar_status()      │  │
│  └───────────────────────────┘  │
└──────────────┬──────────────────┘
               │ Usa Interface (Port)
               ▼
┌─────────────────────────────────┐
│  ADAPTERS (Implementações)      │
│  ┌───────────────────────────┐  │
│  │ pedido_repository.py      │  │
│  │ - get_all()               │  │
│  │ - create()                │  │
│  │ - update_status()         │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
```

## 🎯 Camadas e Responsabilidades

### 1️⃣ Domain (Núcleo)

**Responsabilidade**: Regras de negócio puras, independentes de frameworks

**Arquivos**:

- `entities.py`: Modelos de dados (Pedido, Separacao, Item)
- `interfaces/`: Contratos que definem "o que" fazer
- `usecases/`: Implementam as regras de negócio

**Características**:

- ✅ Sem dependências externas
- ✅ Fácil de testar
- ✅ Regras de negócio centralizadas

### 2️⃣ Adapters (Implementações)

**Responsabilidade**: Implementar as interfaces do domínio

**Arquivos**:

- `repositories/pedido_repository.py`: Persistência de dados (mockado)
- `tiny/tiny_adapter.py`: Integração com Tiny ERP

**Características**:

- ✅ Implementam as Ports (interfaces)
- ✅ Podem ser substituídos facilmente
- ✅ Isolam o domínio de detalhes técnicos

### 3️⃣ Web (Controllers)

**Responsabilidade**: Receber requisições HTTP e orquestrar Use Cases

**Arquivos**:

- `pedido_controller.py`: Endpoints de CRUD de pedidos
- `producao_controller.py`: Endpoints de produção
- `tiny_controller.py`: Endpoints de integração Tiny

**Características**:

- ✅ Validação de entrada
- ✅ Tratamento de erros HTTP
- ✅ Orquestração dos Use Cases

## 📦 Dados Mockados

### Pedidos (6 registros)

```python
# src/adapters/repositories/pedido_repository.py
- Camiseta Lisa Preta -P (Pendente)
- Caneca Branca -G (Imprimindo)
- Camiseta Lisa Branca -M (Concluído)
- Caneca Harry Potter -P (Embalado)
- Copo de League Of Legends (Enviado)
- Teclado Gamer RGB (Parcial)
```

### Separações Tiny ERP (5 registros)

```python
# src/adapters/tiny/tiny_adapter.py
- Suporte para Linhas e Barbantes
- Luminaria Mesa Abajur Led
- Kit Carimbo Marcador Brigadeiros
- Suporte Parede Vertical Roteador
- Carimbo Marcador Brigadeiros PERSONALIZAVEL
```

## 🚀 Como Executar

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Executar API
uvicorn src.main:app --reload

# 3. Acessar documentação
http://localhost:8000/docs
```

## 🧪 Endpoints para Testar

```bash
# Listar pedidos
GET http://localhost:8000/pedidos/

# Métricas dashboard
GET http://localhost:8000/pedidos/metrics

# Separações do Tiny (mockadas)
GET http://localhost:8000/tiny/separacoes

# Importar do Tiny para Pedidos
POST http://localhost:8000/tiny/importar-separacoes

# Status da sincronização
GET http://localhost:8000/tiny/sync-status
```

## ✨ Princípios SOLID Aplicados

- **S** - Single Responsibility: Cada classe tem uma única responsabilidade
- **O** - Open/Closed: Aberto para extensão, fechado para modificação
- **L** - Liskov Substitution: Interfaces podem ser substituídas
- **I** - Interface Segregation: Interfaces específicas e coesas
- **D** - Dependency Inversion: Dependências apontam para abstrações

## 🔄 Próximos Passos

1. Substituir dados mockados por banco de dados real
2. Implementar autenticação e autorização
3. Adicionar testes unitários e de integração
4. Implementar CI/CD
5. Adicionar documentação de API com exemplos
