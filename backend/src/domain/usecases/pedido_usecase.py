from typing import List, Optional
from src.domain.entities import Pedido, StatusPedido, DashboardMetrics
from src.domain.interfaces.pedido_repository import IPedidoRepository


class PedidoUseCase:
    """Use case para operações de pedidos"""
    
    def __init__(self, repository: IPedidoRepository):
        self.repository = repository
    
    def listar_todos_pedidos(self) -> List[Pedido]:
        """Lista todos os pedidos"""
        return self.repository.get_all()
    
    def buscar_pedido_por_id(self, pedido_id: int) -> Optional[Pedido]:
        """Busca pedido por ID"""
        return self.repository.get_by_id(pedido_id)
    
    def criar_pedido(self, sku: str, codigo: str, descricao: str, 
                     status: StatusPedido = StatusPedido.PENDENTE) -> Pedido:
        """Cria novo pedido"""
        # Gera novo ID
        todos_pedidos = self.repository.get_all()
        novo_id = max([p.id for p in todos_pedidos], default=0) + 1
        
        novo_pedido = Pedido(
            id=novo_id,
            sku=sku,
            codigo=codigo,
            descricao=descricao,
            status=status
        )
        return self.repository.create(novo_pedido)
    
    def atualizar_status_pedido(self, pedido_id: int, status: StatusPedido) -> Optional[Pedido]:
        """Atualiza status do pedido"""
        return self.repository.update_status(pedido_id, status)
    
    def remover_pedido(self, pedido_id: int) -> bool:
        """Remove pedido"""
        return self.repository.delete(pedido_id)
    
    def buscar_pedidos_por_status(self, status: StatusPedido) -> List[Pedido]:
        """Busca pedidos por status"""
        return self.repository.get_by_status(status)
    
    def obter_metricas_dashboard(self) -> DashboardMetrics:
        """Obtém métricas do dashboard"""
        return self.repository.get_metrics()
    
    def obter_fila_producao(self) -> List[Pedido]:
        """Retorna fila de produção (pendentes + imprimindo)"""
        pendentes = self.repository.get_by_status(StatusPedido.PENDENTE)
        imprimindo = self.repository.get_by_status(StatusPedido.IMPRIMINDO)
        return pendentes + imprimindo
    
    def obter_pedidos_prioritarios(self) -> List[Pedido]:
        """Retorna pedidos prioritários (pendentes + parciais)"""
        pendentes = self.repository.get_by_status(StatusPedido.PENDENTE)
        parciais = self.repository.get_by_status(StatusPedido.PARCIAL)
        return pendentes + parciais