from fastapi import APIRouter, HTTPException, status
from typing import List
from pydantic import BaseModel

from src.domain.entities import Pedido, StatusPedido, DashboardMetrics
from src.domain.usecases.pedido_usecase import PedidoUseCase
from src.adapters.repositories.pedido_repository import PedidoRepository


class PedidoCreateRequest(BaseModel):
    sku: str
    codigo: str
    descricao: str
    status: StatusPedido = StatusPedido.PENDENTE


class PedidoUpdateRequest(BaseModel):
    status: StatusPedido


pedido_repository = PedidoRepository()
pedido_usecase = PedidoUseCase(pedido_repository)

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.get("/", response_model=List[Pedido])
async def listar_pedidos():
    """Lista todos os pedidos"""
    return pedido_usecase.listar_todos_pedidos()


@router.get("/metrics", response_model=DashboardMetrics)
async def obter_metricas():
    """Retorna métricas do dashboard"""
    return pedido_usecase.obter_metricas_dashboard()


@router.get("/status/{status_nome}", response_model=List[Pedido])
async def buscar_por_status(status_nome: str):
    """Busca pedidos por status"""
    try:
        status = StatusPedido(status_nome)
        return pedido_usecase.buscar_pedidos_por_status(status)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Status inválido: {status_nome}"
        )


@router.get("/{pedido_id}", response_model=Pedido)
async def buscar_pedido(pedido_id: int):
    """Busca pedido por ID"""
    pedido = pedido_usecase.buscar_pedido_por_id(pedido_id)
    if not pedido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pedido {pedido_id} não encontrado"
        )
    return pedido


@router.post("/", response_model=Pedido, status_code=status.HTTP_201_CREATED)
async def criar_pedido(request: PedidoCreateRequest):
    """Cria novo pedido"""
    return pedido_usecase.criar_pedido(
        sku=request.sku,
        codigo=request.codigo,
        descricao=request.descricao,
        status=request.status
    )


@router.patch("/{pedido_id}", response_model=Pedido)
async def atualizar_status(pedido_id: int, request: PedidoUpdateRequest):
    """Atualiza status do pedido"""
    pedido = pedido_usecase.atualizar_status_pedido(pedido_id, request.status)
    if not pedido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pedido {pedido_id} não encontrado"
        )
    return pedido


@router.delete("/{pedido_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remover_pedido(pedido_id: int):
    """Remove pedido"""
    if not pedido_usecase.remover_pedido(pedido_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pedido {pedido_id} não encontrado"
        )
    return None