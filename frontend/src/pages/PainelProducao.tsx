import { useState } from 'react';
import { mockPedidos } from '../data/mockData';
import type { Pedido } from '../data/mockData';
import { FilaPedidos } from '../components/painel/FilaPedidos'; // 1. Importa o "Mestre de Obras"

export function PainelProducao() {
  const [pedidos, setPedidos] = useState<Pedido[]>(mockPedidos);

  return (
    <>
      <div className="p-8">
        <div className='w-full max-w-6xl'>
          <FilaPedidos pedidos={pedidos}/>
        </div>
      </div>
    </>
  );
}