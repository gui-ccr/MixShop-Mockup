import { useState } from 'react';
import { mockPedidos, Pedido } from '../data/mockData';
import { FilaPedidos } from '../components/painel/FilaPedidos'; // 1. Importa o "Mestre de Obras"

export function PainelProducao() {
  const [pedidos, setPedidos] = useState<Pedido[]>(mockPedidos);

  return (
    <div className="flex h-screen w-screen flex-col items-center bg-gray-900 p-8 text-white">
      <h1 className="text-3xl font-bold text-blue-400">
        Painel de Produção - Mix Shop
      </h1>

      {/* 2. O Chefe de Obras agora só DELEGA a tarefa.
             Ele passa a lista de 'pedidos' e o componente 'FilaPedidos'
             se vira para renderizar. */}
      <FilaPedidos pedidos={pedidos} />
    </div>
  );
}