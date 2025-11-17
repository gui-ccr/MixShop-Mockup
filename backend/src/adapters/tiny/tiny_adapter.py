import httpx
from typing import List, Optional
from src.domain.entities import Separacao, Item
from src.domain.interfaces.tiny_gateway import ITinyGateway
from src.config import settings


class TinyAdapter(ITinyGateway):
    """Adaptador para integração com Tiny ERP"""
    
    def __init__(self):
        self.api_url = settings.TINY_API_URL
        self.token = settings.TINY_API_TOKEN
        self._dados_mockados = self._carregar_dados_mockados()
    
    def _carregar_dados_mockados(self) -> List[dict]:
        """Carrega dados mockados do Tiny ERP baseados nos JSONs fornecidos"""
        return [
            {
                "id": "894164451",
                "idOrigem": "894164433",
                "objOrigem": "notafiscal",
                "situacao": "2",
                "situacaoCheckout": "1",
                "dataCriacao": "04/11/2025",
                "dataSeparacao": "05/11/2025",
                "itens": [
                    {
                        "idProduto": "891805847",
                        "descricao": "Suporte para Linhas e Barbantes Croche Costura Costureira Lã Macramé",
                        "codigo": "3d8097",
                        "quantidade": "1.0000",
                        "unidade": "UN",
                        "localizacao": "",
                        "infoAdicional": ""
                    }
                ],
                "qtdVolumes": "1",
                "numero": "87302",
                "dataEmissao": "04/11/2025",
                "numeroPedidoEcommerce": "251105VA14A0HH",
                "idFormaEnvio": "773273998",
                "formaEnvio": "Shopee Envios",
                "idContato": "760595885",
                "destinatario": "Lidia Rank Schaia"
            },
            {
                "id": "894194443",
                "idOrigem": "894178643",
                "objOrigem": "notafiscal",
                "situacao": "2",
                "situacaoCheckout": "1",
                "dataCriacao": "04/11/2025",
                "dataSeparacao": "05/11/2025",
                "itens": [
                    {
                        "idProduto": "822221488",
                        "descricao": "Luminaria Mesa Abajur Led Portátil ONDULADO Decoracao Diversos Presente Quarto Casa Geometrica Luxo",
                        "codigo": "3D593",
                        "quantidade": "1.0000",
                        "unidade": "un",
                        "localizacao": "",
                        "infoAdicional": ""
                    }
                ],
                "qtdVolumes": "1",
                "numero": "87428",
                "dataEmissao": "04/11/2025",
                "numeroPedidoEcommerce": "251105VJCEPU2W",
                "idFormaEnvio": "773273998",
                "formaEnvio": "Shopee Envios",
                "idContato": "760597843",
                "destinatario": "Teresa Francisca Klovrza Bifulco Walters"
            },
            {
                "id": "894213062",
                "idOrigem": "894213049",
                "objOrigem": "notafiscal",
                "situacao": "2",
                "situacaoCheckout": "1",
                "dataCriacao": "04/11/2025",
                "dataSeparacao": "05/11/2025",
                "itens": [
                    {
                        "idProduto": "885622955",
                        "descricao": "Kit Carimbo Marcador Brigadeiros NOME PERSONALIZADO Molde Festa Confeitaria Aniversario Brigadeiro",
                        "codigo": "3D5518",
                        "quantidade": "1.0000",
                        "unidade": "UN",
                        "localizacao": "",
                        "infoAdicional": ""
                    }
                ],
                "qtdVolumes": "1",
                "numero": "87817",
                "dataEmissao": "04/11/2025",
                "numeroPedidoEcommerce": "251105025TMRJ4",
                "idFormaEnvio": "773273998",
                "formaEnvio": "Shopee Envios",
                "idContato": "760602725",
                "destinatario": "Rodinel Claudio de Paula Silva"
            },
            {
                "id": "894245947",
                "idOrigem": "894245943",
                "objOrigem": "notafiscal",
                "situacao": "2",
                "situacaoCheckout": "1",
                "dataCriacao": "05/11/2025",
                "dataSeparacao": "05/11/2025",
                "itens": [
                    {
                        "idProduto": "881775661",
                        "descricao": "Suporte Parede Vertical Compativel Roteador Modem Ajustavel Universal - PRETO",
                        "codigo": "3D5143-1",
                        "quantidade": "1.0000",
                        "unidade": "UN",
                        "localizacao": "",
                        "infoAdicional": ""
                    }
                ],
                "qtdVolumes": "1",
                "numero": "87989",
                "dataEmissao": "05/11/2025",
                "numeroPedidoEcommerce": "25110517P4SP1S",
                "idFormaEnvio": "773273998",
                "formaEnvio": "Shopee Envios",
                "idContato": "760607359",
                "destinatario": "Marcio Arodi da Silva Vieira"
            },
            {
                "id": "894252155",
                "idOrigem": "894252149",
                "objOrigem": "notafiscal",
                "situacao": "2",
                "situacaoCheckout": "1",
                "dataCriacao": "05/11/2025",
                "dataSeparacao": "05/11/2025",
                "itens": [
                    {
                        "idProduto": "881707879",
                        "descricao": "Carimbo Marcador Brigadeiros PERSONALIZAVEL DESENHOS MARCAS LOGO LOGOMARCAS  Molde Festa Confeitaria Aniversario",
                        "codigo": "3D5006",
                        "quantidade": "1.0000",
                        "unidade": "UN",
                        "localizacao": "",
                        "infoAdicional": ""
                    }
                ],
                "qtdVolumes": "1",
                "numero": "88027",
                "dataEmissao": "05/11/2025",
                "numeroPedidoEcommerce": "2511051ASSV69P",
                "idFormaEnvio": "773273998",
                "formaEnvio": "Shopee Envios",
                "idContato": "759906710",
                "destinatario": "Rogério dos Santos Dias"
            }
        ]
    
    async def get_separacoes(self, usar_mock: bool = True) -> List[Separacao]:
        """Busca separações do Tiny ERP"""
        if usar_mock or not self.token:
            return self._obter_separacoes_mockadas()

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.api_url}/separacoes.pesquisa.php",
                    data={
                        "token": self.token,
                        "formato": "json"
                    }
                )
                response.raise_for_status()
                data = response.json()
                
                if data and "retorno" in data:
                    retorno = data["retorno"]
                    if "separacoes" in retorno:
                        return [self._dict_para_separacao(sep) for sep in retorno["separacoes"]]
                
                return []
        except Exception as e:
            print(f"Erro ao buscar separações do Tiny: {e}")
            return self._obter_separacoes_mockadas()
    
    async def get_separacao_by_id(self, separacao_id: str, usar_mock: bool = True) -> Optional[Separacao]:
        """Busca separação específica por ID"""
        if usar_mock or not self.token:
            separacoes = self._obter_separacoes_mockadas()
            return next((sep for sep in separacoes if sep.id == separacao_id), None)

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.api_url}/separacao.obter.php",
                    data={
                        "token": self.token,
                        "id": separacao_id,
                        "formato": "json"
                    }
                )
                response.raise_for_status()
                data = response.json()
                
                if data and "retorno" in data and "separacao" in data["retorno"]:
                    return self._dict_para_separacao(data["retorno"]["separacao"])
                
                return None
        except Exception as e:
            print(f"Erro ao buscar separação {separacao_id} do Tiny: {e}")
            return None
    
    def _obter_separacoes_mockadas(self) -> List[Separacao]:
        """Retorna separações mockadas"""
        return [self._dict_para_separacao(sep_data) for sep_data in self._dados_mockados]
    
    def _dict_para_separacao(self, data: dict) -> Separacao:
        """Converte dict para Separacao"""
        itens = [Item(**item) for item in data["itens"]]
        
        return Separacao(
            id=data["id"],
            idOrigem=data["idOrigem"],
            objOrigem=data["objOrigem"],
            situacao=data["situacao"],
            situacaoCheckout=data["situacaoCheckout"],
            dataCriacao=data["dataCriacao"],
            dataSeparacao=data["dataSeparacao"],
            dataCheckout=data.get("dataCheckout"),
            itens=itens,
            qtdVolumes=data["qtdVolumes"],
            numero=data["numero"],
            dataEmissao=data["dataEmissao"],
            numeroPedidoEcommerce=data["numeroPedidoEcommerce"],
            idFormaEnvio=data["idFormaEnvio"],
            formaEnvio=data["formaEnvio"],
            idContato=data["idContato"],
            destinatario=data["destinatario"],
            situacaoOrigem=data.get("situacaoOrigem")
        )