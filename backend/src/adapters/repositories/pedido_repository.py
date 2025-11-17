from typing import List, Optional, Dict
from src.domain.entities import Pedido, StatusPedido, DashboardMetrics
from src.domain.interfaces.pedido_repository import IPedidoRepository


class PedidoRepository(IPedidoRepository):
    """Implementação do repositório de pedidos (Adapter)"""
    
    def __init__(self):
        self._pedidos: List[Pedido] = self._carregar_pedidos_mockados()
    
    def _carregar_pedidos_mockados(self) -> List[Pedido]:
        """Carrega pedidos mockados"""
        return [
            Pedido(
                id=1,
                sku="MIX-TSH-001-P",
                codigo="1001",
                descricao="Camiseta Lisa Preta -P",
                status=StatusPedido.PENDENTE,
            ),
            Pedido(
                id=2,
                sku="MIX-CAN-002-G",
                codigo="1002",
                descricao="Caneca Branca -G",
                status=StatusPedido.IMPRIMINDO,
            ),
            Pedido(
                id=3,
                sku="MIX-TSH-003-M",
                codigo="1003",
                descricao="Camiseta Lisa Branca -M",
                status=StatusPedido.CONCLUIDO,
            ),
            Pedido(
                id=4,
                sku="MIX-CAN-004-P",
                codigo="1004",
                descricao="Caneca Harry Potter -P",
                status=StatusPedido.EMBALADO,
            ),
            Pedido(
                id=5,
                sku="MIX-COP-009-M",
                codigo="1005",
                descricao="Copo de League Of Legends",
                status=StatusPedido.ENVIADO,
            ),
            Pedido(
                id=6,
                sku="MIX-TGR-004",
                codigo="1006",
                descricao="Teclado Gamer RGB",
                status=StatusPedido.PARCIAL,
            ),
        ]
    
    def get_all(self) -> List[Pedido]:
        """Retorna todos os pedidos"""
        return self._pedidos.copy()
    
    def get_by_id(self, pedido_id: int) -> Optional[Pedido]:
        """Busca pedido por ID"""
        return next((p for p in self._pedidos if p.id == pedido_id), None)
    
    def create(self, pedido: Pedido) -> Pedido:
        """Cria novo pedido"""
        self._pedidos.append(pedido)
        return pedido
    
    def update_status(self, pedido_id: int, status: StatusPedido) -> Optional[Pedido]:
        """Atualiza status do pedido"""
        pedido = self.get_by_id(pedido_id)
        if pedido:
            pedido.status = status
            return pedido
        return None
    
    def delete(self, pedido_id: int) -> bool:
        """Remove pedido"""
        pedido = self.get_by_id(pedido_id)
        if pedido:
            self._pedidos.remove(pedido)
            return True
        return False
    
    def get_by_status(self, status: StatusPedido) -> List[Pedido]:
        """Busca pedidos por status"""
        return [p for p in self._pedidos if p.status == status]
    
    def get_metrics(self) -> DashboardMetrics:
        """Retorna métricas do dashboard"""
        status_count: Dict[StatusPedido, int] = {
            StatusPedido.PENDENTE: 0,
            StatusPedido.IMPRIMINDO: 0,
            StatusPedido.PARCIAL: 0,
            StatusPedido.CONCLUIDO: 0,
            StatusPedido.EMBALADO: 0,
            StatusPedido.ENVIADO: 0,
        }
        
        for pedido in self._pedidos:
            status_count[pedido.status] += 1
        
        return DashboardMetrics(
            total=len(self._pedidos),
            pendente=status_count[StatusPedido.PENDENTE],
            imprimindo=status_count[StatusPedido.IMPRIMINDO],
            parcial=status_count[StatusPedido.PARCIAL],
            concluido=status_count[StatusPedido.CONCLUIDO],
            embalado=status_count[StatusPedido.EMBALADO],
            enviado=status_count[StatusPedido.ENVIADO],
        )