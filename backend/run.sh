#!/bin/bash

echo "🏭 Mix Shop API - Iniciando..."
echo ""

# Verifica se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativa o ambiente virtual
echo "🔄 Ativando ambiente virtual..."
source venv/bin/activate

# Instala dependências
echo "📥 Instalando dependências..."
pip install -q -r requirements.txt

# Executa a aplicação
echo ""
echo "✅ Iniciando API em http://localhost:8000"
echo "📚 Documentação: http://localhost:8000/docs"
echo ""

uvicorn src.main:app --reload