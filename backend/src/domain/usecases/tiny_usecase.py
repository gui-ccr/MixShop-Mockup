from typing import List, Optional
from src.domain.entities import Separacao, Pedido, StatusPedido
from src.domain.interfaces.tiny_gateway import ITinyGateway
from src.domain.interfaces.pedido_repository import IPedidoRepository


class TinyUseCase:
    """Use case para integração com Tiny ERP"""
    
    def __init__(self, tiny_gateway: ITinyGateway, pedido_repository: IPedidoRepository):
        self.tiny_gateway = tiny_gateway
        self.pedido_repository = pedido_repository
    
    async def listar_separacoes(self, usar_mock: bool = True) -> List[Separacao]:
        """Lista separações do Tiny ERP"""
        return await self.tiny_gateway.get_separacoes(usar_mock)
    
    async def buscar_separacao(self, separacao_id: str, usar_mock: bool = True) -> Optional[Separacao]:
        """Busca separação específica"""
        return await self.tiny_gateway.get_separacao_by_id(separacao_id, usar_mock)
    
    async def importar_separacoes(self, usar_mock: bool = True) -> List[Pedido]:
        """Importa separações do Tiny e converte em pedidos"""
        separacoes = await self.tiny_gateway.get_separacoes(usar_mock)
        pedidos_importados = []
        
        for separacao in separacoes:
            pedido = self._converter_separacao_para_pedido(separacao)
            pedido_criado = self.pedido_repository.create(pedido)
            pedidos_importados.append(pedido_criado)
        
        return pedidos_importados
    
    def _converter_separacao_para_pedido(self, separacao: Separacao) -> Pedido:
        """Converte Separacao do Tiny para Pedido"""
        if separacao.itens:
            item = separacao.itens[0]
            descricao = item.descricao
            codigo = item.codigo
            sku = f"MIX-{codigo}"
            quantidade = item.quantidade
        else:
            descricao = "Pedido sem itens"
            codigo = separacao.numero
            sku = f"MIX-{separacao.numero}"
            quantidade = "0"
        
        status = self._mapear_status_tiny(separacao.situacao, separacao.situacaoCheckout)

        todos_pedidos = self.pedido_repository.get_all()
        novo_id = max([p.id for p in todos_pedidos], default=0) + 1
        
        return Pedido(
            id=novo_id,
            sku=sku,
            codigo=codigo,
            descricao=descricao,
            status=status,
            numeroPedido=separacao.numeroPedidoEcommerce,
            destinatario=separacao.destinatario,
            dataCriacao=separacao.dataCriacao,
            quantidade=quantidade
        )
    
    def _mapear_status_tiny(self, situacao: str, situacao_checkout: str) -> StatusPedido:
        """Mapeia status do Tiny para status interno"""
        if situacao_checkout == "2":
            return StatusPedido.ENVIADO
        
        status_map = {
            "1": StatusPedido.PENDENTE,
            "2": StatusPedido.CONCLUIDO,
        }
        
        return status_map.get(situacao, StatusPedido.PENDENTE)
    
    async def obter_status_sincronizacao(self, usar_mock: bool = True) -> dict:
        """Retorna status da sincronização com Tiny"""
        separacoes = await self.tiny_gateway.get_separacoes(usar_mock)
        pedidos = self.pedido_repository.get_all()
        
        return {
            "tiny_separacoes": len(separacoes),
            "pedidos_sistema": len(pedidos),
            "mock_mode": usar_mock,
            "api_configured": True
        }