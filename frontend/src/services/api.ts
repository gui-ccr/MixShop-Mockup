import axios from 'axios';

// URL base da API - ajuste conforme necessário
const API_BASE_URL = 'https://mix-shop-api-production-1a16.up.railway.app';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Tipos
export type StatusPedido = "Pendente" | "Imprimindo" | "Parcial" | "Concluído" | "Embalado" | "Enviado";

export interface Pedido {
  id: number;
  sku: string;
  codigo: string;
  descricao: string;
  status: StatusPedido;
  numeroPedido?: string;
  destinatario?: string;
  dataCriacao?: string;
  quantidade?: string;
}

export interface DashboardMetrics {
  total: number;
  pendente: number;
  imprimindo: number;
  parcial: number;
  concluido: number;
  embalado: number;
  enviado: number;
}

// Funções da API
export const pedidosAPI = {
  // Listar todos os pedidos
  listarPedidos: async (): Promise<Pedido[]> => {
    const response = await api.get<Pedido[]>('/pedidos/');
    return response.data;
  },

  // Obter métricas do dashboard
  obterMetricas: async (): Promise<DashboardMetrics> => {
    const response = await api.get<DashboardMetrics>('/pedidos/metrics');
    return response.data;
  },

  // Buscar pedidos por status
  buscarPorStatus: async (status: StatusPedido): Promise<Pedido[]> => {
    const response = await api.get<Pedido[]>(`/pedidos/status/${status}`);
    return response.data;
  },

  // Buscar pedido por ID
  buscarPorId: async (id: number): Promise<Pedido> => {
    const response = await api.get<Pedido>(`/pedidos/${id}`);
    return response.data;
  },
};

export default api;
