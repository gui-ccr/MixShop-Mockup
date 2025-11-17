import { StatCard } from "../common/Statcard";
import { Package, Truck, Undo2, CheckCircle } from 'lucide-react';
import type { DashboardMetrics } from "../../services/api";

type OverallStatsProps = {
  metricas: DashboardMetrics | null;
};

export function OverallStats({ metricas }: OverallStatsProps) {
  // Valores padrão caso as métricas ainda não tenham sido carregadas
  const stats = [
    {
      title: "Total de Pedidos",
      value: metricas?.total.toString() || "0",
      Icon: Package,
      colors: { iconBg: "bg-blue-100", iconText: "text-blue-600" },
    },
    {
      title: "Em Expedição",
      value: metricas ? (metricas.imprimindo + metricas.parcial).toString() : "0",
      Icon: Truck,
      colors: { iconBg: "bg-yellow-100", iconText: "text-yellow-600" },
    },
    {
      title: "Concluídos",
      value: metricas ? (metricas.concluido + metricas.embalado + metricas.enviado).toString() : "0",
      Icon: CheckCircle,
      colors: { iconBg: "bg-green-100", iconText: "text-green-600" },
    },
    {
      title: "Pendentes",
      value: metricas?.pendente.toString() || "0",
      Icon: Undo2,
      colors: { iconBg: "bg-red-100", iconText: "text-red-600" },
    },
  ];

  return(

    <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4">
      {/* loop de dados */}

      {stats.map((stat) => (
        <StatCard
        key={stat.title}
        title={stat.title}
        value={stat.value}
        Icon={stat.Icon}
        colorClasses={stat.colors}
        />
      ))}
    </div>
  )
}