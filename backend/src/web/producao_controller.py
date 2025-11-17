from fastapi import APIRouter
from typing import List

from src.domain.entities import Pedido, StatusPedido
from src.domain.usecases.pedido_usecase import PedidoUseCase
from src.adapters.repositories.pedido_repository import PedidoRepository


pedido_repository = PedidoRepository()
pedido_usecase = PedidoUseCase(pedido_repository)

router = APIRouter(prefix="/producao", tags=["Produção"])


@router.get("/fila", response_model=List[Pedido])
async def obter_fila_producao():
    """Retorna fila de produção (pedidos pendentes e em impressão)"""
    return pedido_usecase.obter_fila_producao()


@router.get("/status-overview")
async def obter_visao_geral():
    """Retorna visão geral dos status de produção"""
    metrics = pedido_usecase.obter_metricas_dashboard()
    
    return {
        "total": metrics.total,
        "fila": {
            "pendente": metrics.pendente,
            "imprimindo": metrics.imprimindo,
            "parcial": metrics.parcial
        },
        "concluidos": {
            "concluido": metrics.concluido,
            "embalado": metrics.embalado,
            "enviado": metrics.enviado
        }
    }


@router.get("/prioridades", response_model=List[Pedido])
async def obter_pedidos_prioritarios():
    """Retorna pedidos prioritários (pendentes e parciais)"""
    return pedido_usecase.obter_pedidos_prioritarios()


@router.get("/em-andamento", response_model=List[Pedido])
async def obter_em_andamento():
    """Retorna pedidos em andamento (imprimindo)"""
    return pedido_usecase.buscar_pedidos_por_status(StatusPedido.IMPRIMINDO)


@router.get("/prontos-embalar", response_model=List[Pedido])
async def obter_prontos_embalar():
    """Retorna pedidos prontos para embalar"""
    return pedido_usecase.buscar_pedidos_por_status(StatusPedido.CONCLUIDO)


@router.get("/prontos-enviar", response_model=List[Pedido])
async def obter_prontos_enviar():
    """Retorna pedidos prontos para envio"""
    return pedido_usecase.buscar_pedidos_por_status(StatusPedido.EMBALADO)