import { Pedido } from "../../data/mockData";
import { ItemPedido } from "./ItemPedido";

type FilaPedidosProps = {
    pedidos: Pedido[]; // recebe array de pedidos como prop
}

export function FilaPedidos({ pedidos }: FilaPedidosProps) {
  return (
    // 3. Este é o JSX que "cercava" o seu .map()
    <div className="mt-10 w-full max-w-4xl">
      <h2 className="text-2xl font-semibold">Fila de Pedidos</h2>
      <ul className="mt-4 flex flex-col gap-3">
        {/* 4. Agora o loop é mais limpo:
               Para cada 'pedido', ele chama o 'ItemPedido'
               e passa o pedido para ele via prop. */}
        {pedidos.map((pedido) => (
          <ItemPedido key={pedido.id} pedido={pedido} />
        ))}
      </ul>
    </div>
  )
}