from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities import Separacao


class ITinyGateway(ABC):
    """Interface do gateway Tiny ERP (Port)"""
    
    @abstractmethod
    async def get_separacoes(self, usar_mock: bool = True) -> List[Separacao]:
        """Busca separações do Tiny ERP"""
        pass
    
    @abstractmethod
    async def get_separacao_by_id(self, separacao_id: str, usar_mock: bool = True) -> Optional[Separacao]:
        """Busca separação específica por ID"""
        pass