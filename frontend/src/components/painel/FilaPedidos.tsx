import { Pedido } from "../../data/mockData";
import { SearchBar } from "../common/SearchBar";
import { ItemPedido } from "./ItemPedido";

type FilaPedidosProps = {
    pedidos: Pedido[]; // recebe array de pedidos como prop
}

export function FilaPedidos({ pedidos }: FilaPedidosProps) {
  return (
    // card branco envolve todo o conteudo 
    <div className="bg-white rounded-lg shadow-sm overflow-hidden">
      {/* CABEÇALHO DO BLOCO */}

      <div className=" p-5 flex border-b border-gray-200">

        {/* LINHA 1 TITULO */}
        <h2 className="text-lg text-gray-800 font-bold mb-4">
          Fila de Pedidos
          </h2>
      </div>

      <div className="flex justify-between items-center">
        <SearchBar/>
        <div className="flex gap-2">
          <button className="bg-gray-100 text-gray-700 px-3 py-1.5 rounded-md text-sm font-medium border border-gray-300 hover:bg-gray-200">
          Filters
          </button>
        </div>
      </div>

    <div className="overflow-x-auto">
      <table className="w-full text-left">
        {/* cabeçalho <thead> fundo cinza claro*/}
        <thead className="bg-gray-50">
          <th className="py-3 px-4 text-sm font-semibold text-gray-600">Código</th>
          <th className="py-3 px-4 text-sm font-semibold text-gray-600">SKU</th>
          <th className="py-3 px-4 text-sm font-semibold text-gray-600">Descrição</th>
          <th className="py-3 px-4 text-sm font-semibold text-gray-600">Status</th>
          <th className="py-3 px-4 text-sm font-semibold text-gray-600">Ações</th>
        </thead>

        {/* o corpo <tbody> */}

        <tbody className="bg-white divide-y divide-gray-200">
          {pedidos.map((pedido) => (
            <ItemPedido key={pedido.id} pedido={pedido}/>
          ))}
        </tbody>
      </table>
    </div>

    {/* RODAPE DO BLOCO */}
    <div className="p-4 flex justify-between items-center text-sm text-gray-600 border-t border-gray-200">
          <button className="px-3 py-1 rounded-md border border-gray-300 hover:bg-gray-50">Anterior</button>
          <span>Pagina 1 de 1</span>
          <button className="px-3 py-1 rounded-md border border-gray-300 hover:bg-gray-50">Proximo</button>
    </div>
  </div>
  )
}