import { Pedido } from '../../data/mockData';

const getStatusColor = (status: Pedido['status']) => {
    switch (status) {
        case "Pendente":
            return 'bg-gray-500';
        case "Imprimindo":
            return 'bg-yellow-500';
        case "Parcial":
            return 'bg-orange-500';
        case "Concluído":
            return 'bg-green-500';
        case "Embalado":
            return 'bg-blue-500';
        case "Enviado":
            return 'bg-purple-500';
        default:
            return 'bg-gray-200 text-black';
    }
}

type ItemPedidoProps = {
    pedido: Pedido; // recebe objeto pedido como prop
}


export function ItemPedido({ pedido }: ItemPedidoProps) {
    return (
        <li className="flex justify-between rounded-lg bg-gray-800 p-4 shadow-md">
      <div className="flex flex-col">
        <span className="font-bold text-gray-200">{pedido.descricao}</span>
        <span className="text-sm text-gray-400">SKU: {pedido.sku}</span>
      </div>
      <div className="flex items-center">
        {/* TODO: Mudar a cor com base no status */}
        <span className={`${getStatusColor(pedido.status)} rounded-full px-3 py-1 text-sm font-medium`}>
          {pedido.status}
        </span>
      </div>
    </li>
    )
}