import { useState } from 'react';
import { mockPedidos } from '../data/mockData';
import type { Pedido } from '../data/mockData';
import { FilaPedidos } from '../components/painel/FilaPedidos'; // 1. Importa o "Mestre de Obras"
import { OverallStats } from '../components/painel/OverallStats';

export function PainelProducao() {
  const [pedidos, setPedidos] = useState<Pedido[]>(mockPedidos);

  return (
    <>
      <div className="p-8">
        <div className='w-full max-w-6xl'>
          <h1 className='text-2xl font-bold mb-4'>Dashboard</h1>
          <OverallStats/>
          <div className='mt-6'>
          <FilaPedidos pedidos={pedidos}/>
          </div>
        </div>
      </div>
    </>
  );
}