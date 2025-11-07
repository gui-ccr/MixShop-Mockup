import { useState } from 'react';
import { mockPedidos } from '../data/mockData';
import type { Pedido } from '../data/mockData';
import { FilaPedidos } from '../components/painel/FilaPedidos'; // 1. Importa o "Mestre de Obras"

export function PainelProducao() {
  const [pedidos, setPedidos] = useState<Pedido[]>(mockPedidos);

  return (
    <>
      <div className="flex w-screen flex-col items-center bg-gray-100 p-8 min-h-screen">
        
        <div className="w-full max-w-6xl mb-4">
            <h1 className='text-2xl font-bold text-gray-800'>Pedidos</h1>
        </div>

        {/* centralizando a tabela com uma largura maxima */}

        <div className='w-full max-w-6xl'>
          <FilaPedidos pedidos={pedidos}/>
        </div>
      </div>
    </>
  );
}