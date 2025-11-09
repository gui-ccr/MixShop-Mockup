import { StatCard } from "../common/Statcard";

import { Package, Truck, Undo2, CheckCircle } from 'lucide-react';

const stats = [
  {
    title: "Total de Pedidos",
    value: "42",
    Icon: Package,
    colors: { iconBg: "bg-blue-100", iconText: "text-blue-600" },
  },
  {
    title: "Em Expedição",
    value: "12",
    Icon: Truck,
    colors: { iconBg: "bg-yellow-100", iconText: "text-yellow-600" },
  },
  {
    title: "Concluídos",
    value: "30",
    Icon: CheckCircle,
    colors: { iconBg: "bg-green-100", iconText: "text-green-600" },
  },
  {
    title: "Devolvidos",
    value: "2",
    Icon: Undo2,
    colors: { iconBg: "bg-red-100", iconText: "text-red-600" },
  },
];

export function OverallStats() {
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