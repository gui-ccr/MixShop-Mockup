from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities import Pedido, StatusPedido, DashboardMetrics


class IPedidoRepository(ABC):
    """Interface do repositório de pedidos (Port)"""
    
    @abstractmethod
    def get_all(self) -> List[Pedido]:
        """Retorna todos os pedidos"""
        pass
    
    @abstractmethod
    def get_by_id(self, pedido_id: int) -> Optional[Pedido]:
        """Busca pedido por ID"""
        pass
    
    @abstractmethod
    def create(self, pedido: Pedido) -> Pedido:
        """Cria novo pedido"""
        pass
    
    @abstractmethod
    def update_status(self, pedido_id: int, status: StatusPedido) -> Optional[Pedido]:
        """Atualiza status do pedido"""
        pass
    
    @abstractmethod
    def delete(self, pedido_id: int) -> bool:
        """Remove pedido"""
        pass
    
    @abstractmethod
    def get_by_status(self, status: StatusPedido) -> List[Pedido]:
        """Busca pedidos por status"""
        pass
    
    @abstractmethod
    def get_metrics(self) -> DashboardMetrics:
        """Retorna métricas do dashboard"""
        pass