import { useState, useEffect } from 'react';
import { pedidosAPI, type Pedido, type DashboardMetrics } from '../services/api';
import { FilaPedidos } from '../components/painel/FilaPedidos'; // 1. Importa o "Mestre de Obras"
import { OverallStats } from '../components/painel/OverallStats';

export function PainelProducao() {
  const [pedidos, setPedidos] = useState<Pedido[]>([]);
  const [metricas, setMetricas] = useState<DashboardMetrics | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const carregarDados = async () => {
      try {
        setLoading(true);
        setError(null);
        
        // Buscar pedidos e métricas em paralelo
        const [pedidosData, metricasData] = await Promise.all([
          pedidosAPI.listarPedidos(),
          pedidosAPI.obterMetricas()
        ]);
        
        setPedidos(pedidosData);
        setMetricas(metricasData);
      } catch (err) {
        console.error('Erro ao carregar dados:', err);
        setError('Erro ao conectar com a API. Certifique-se de que o backend está rodando.');
      } finally {
        setLoading(false);
      }
    };

    carregarDados();
  }, []);

  if (loading) {
    return (
      <div className="p-8 flex justify-center items-center min-h-screen">
        <div className="text-gray-600">Carregando dados...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-8">
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
          {error}
        </div>
      </div>
    );
  }

  return (
    <>
      <div className="p-8">
        <div className='w-full max-w-6xl'>
          <h1 className='text-2xl font-bold mb-4'>Dashboard</h1>
          <OverallStats metricas={metricas}/>
          <div className='mt-6'>
          <FilaPedidos pedidos={pedidos}/>
          </div>
        </div>
      </div>
    </>
  );
}