from fastapi import APIRouter, HTTPException, status, Query
from typing import List

from src.domain.entities import Separacao, Pedido
from src.domain.usecases.tiny_usecase import TinyUseCase
from src.adapters.tiny.tiny_adapter import TinyAdapter
from src.adapters.repositories.pedido_repository import PedidoRepository


tiny_adapter = TinyAdapter()
pedido_repository = PedidoRepository()
tiny_usecase = TinyUseCase(tiny_adapter, pedido_repository)

router = APIRouter(prefix="/tiny", tags=["Tiny ERP"])


@router.get("/separacoes", response_model=List[Separacao])
async def listar_separacoes(usar_mock: bool = Query(True, description="Usar dados mockados")):
    """
    Busca separações do Tiny ERP
    Por padrão retorna dados mockados para desenvolvimento
    """
    try:
        return await tiny_usecase.listar_separacoes(usar_mock=usar_mock)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar separações: {str(e)}"
        )


@router.get("/separacoes/{separacao_id}", response_model=Separacao)
async def buscar_separacao(
    separacao_id: str,
    usar_mock: bool = Query(True, description="Usar dados mockados")
):
    """Busca separação específica por ID"""
    separacao = await tiny_usecase.buscar_separacao(separacao_id, usar_mock=usar_mock)
    if not separacao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Separação {separacao_id} não encontrada"
        )
    return separacao


@router.post("/importar-separacoes", response_model=List[Pedido])
async def importar_separacoes(usar_mock: bool = Query(True, description="Usar dados mockados")):
    """Importa separações do Tiny ERP e converte para pedidos"""
    try:
        return await tiny_usecase.importar_separacoes(usar_mock=usar_mock)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao importar separações: {str(e)}"
        )


@router.get("/sync-status")
async def obter_status_sincronizacao(usar_mock: bool = Query(True, description="Usar dados mockados")):
    """Retorna status da sincronização com Tiny ERP"""
    return await tiny_usecase.obter_status_sincronizacao(usar_mock=usar_mock)