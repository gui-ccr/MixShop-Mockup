import { EllipsisVerticalIcon } from 'lucide-react';
import type { Pedido } from '../../data/mockData';
import { Chip } from '../common/Chip'

const getStatusColor = (status: Pedido['status']) => {
    switch (status) {
        case "Pendente":
            return 'bg-gray-200 text-gray-800';
        case "Imprimindo":
            return 'bg-yellow-200 text-yellow-800';
        case "Parcial":
            return 'bg-orange-200 text-orange-800';
        case "Concluído":
            return 'bg-green-200 text-green-800';
        case "Embalado":
            return 'bg-blue-200 text-blue-800';
        case "Enviado":
            return 'bg-purple-200 text-purple-800';
        default:
            return 'bg-gray-100 text-black';
    }
}

type ItemPedidoProps = {
    pedido: Pedido; // recebe objeto pedido como prop
}


export function ItemPedido({ pedido }: ItemPedidoProps) {
    
    const corDoStatus = getStatusColor(pedido.status)

    return (
        <tr className='hover:bg-gray-200'>
            {/* as celulas de td com os dados do 'pedido */}
            <td className='py-3 px-4 text-sm text-gray-900 font-medium'>
                {pedido.codigo}
            </td>
            <td className='py-3 px-4 text-sm text-gray-600'>
                {pedido.sku}
            </td>
            <td className='py-3 px-4 text-sm text-gray-900 font-medium'>
                {pedido.descricao}
            </td>
            <td className='py-3 px-4 text-sm'>
                <Chip label={pedido.status} colorClasses={corDoStatus}/>
            </td>
            <td className='py-3 px-4 text-center text-gray-500 font-bold cursor-pointer hover:text-gray-900'>
                <EllipsisVerticalIcon/>
            </td>
        </tr>
    )
}