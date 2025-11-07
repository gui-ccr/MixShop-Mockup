import { Search } from 'lucide-react'

export function SearchBar(){
    return(
        <div className='relative w-150'>
            {/* icone de lupa */}
            <div className='absolute left-3 top-1/2 -translate-y-1/2 text-gray-400'>
                <Search className='h-4 w-4'/>
            </div>
            <input type="text" placeholder='Buscar Pedidos...' className='w-full rounded-md border border-gray-300 bg-white py-1.5 pl-10 pr-3 text-sm text-gray-700 shadow-sm focus:ontline-none ' />
        </div>
    )
}