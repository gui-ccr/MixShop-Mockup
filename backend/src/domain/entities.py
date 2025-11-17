from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class StatusPedido(str, Enum):
    PENDENTE = "Pendente"
    IMPRIMINDO = "Imprimindo"
    PARCIAL = "Parcial"
    CONCLUIDO = "Concluído"
    EMBALADO = "Embalado"
    ENVIADO = "Enviado"


class Item(BaseModel):
    idProduto: str
    descricao: str
    codigo: str
    quantidade: str
    unidade: str
    localizacao: str = ""
    infoAdicional: str = ""


class Separacao(BaseModel):
    id: str
    idOrigem: str
    objOrigem: str
    situacao: str
    situacaoCheckout: str
    dataCriacao: str
    dataSeparacao: str
    dataCheckout: Optional[str] = None
    itens: List[Item]
    qtdVolumes: str
    numero: str
    dataEmissao: str
    numeroPedidoEcommerce: str
    idFormaEnvio: str
    formaEnvio: str
    idContato: str
    destinatario: str
    situacaoOrigem: Optional[str] = None


class Pedido(BaseModel):
    id: int
    sku: str
    codigo: str
    descricao: str
    status: StatusPedido
    numeroPedido: Optional[str] = None
    destinatario: Optional[str] = None
    dataCriacao: Optional[str] = None
    quantidade: Optional[str] = None


class DashboardMetrics(BaseModel):
    total: int
    pendente: int
    imprimindo: int
    parcial: int
    concluido: int
    embalado: int
    enviado: int