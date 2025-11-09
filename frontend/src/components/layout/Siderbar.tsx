import { HomeIcon, PackageIcon, BarChart2Icon, SettingsIcon, LogOutIcon, ChartAreaIcon, BoxesIcon, WalletIcon, UserPenIcon, ScanBarcodeIcon, SeparatorVerticalIcon } from 'lucide-react'


export function Sidebar() {
    return (
        <aside className='hidden md:flex h-screen w-50 flex-col bg-white p-4 text-white sticky top-0'>
            
            {/* LOGO */}
        <div className='mb-8'>
            <h2 className='text-2xl font-bold text-black'>Mix Shop</h2>
        </div>

        <nav className='flex-1'>
            <ul className='flex flex-col gap-2'>
                <li className='flex cursor-pointer items-center gap-3 rounded-md text-black 
                hover:text-gray-400 p-2'>
                    <HomeIcon className='h-5 w-5'/>
                    <span className='font-sm'>Dashboard</span>
                </li>
                <li className='flex cursor-pointer items-center gap-3 rounded-md text-black hover:text-gray-400 p-2'>
                    <ScanBarcodeIcon className='h-5 w-5'/>
                    <span className='font-sm'>Impressão</span>
                </li>
                <li className='flex cursor-pointer items-center gap-3 rounded-md text-black hover:text-gray-400 p-2'>
                    <SeparatorVerticalIcon className='h-5 w-5'/>
                    <span className='font-sm'>Separação</span>
                </li>
                <li className='flex cursor-pointer items-center gap-3 rounded-md text-black hover:text-gray-400 p-2'>
                    <BoxesIcon className='h-5 w-5'/>
                    <span className='font-sm'>Embalagem</span>
                </li>
                <li className='flex cursor-pointer items-center gap-3 rounded-md text-black hover:text-gray-400 p-2 '>
                    <PackageIcon className='h-5 w-5'/>
                    <span className='font-bold'>Expedição</span>
                </li>
                <li className='flex cursor-pointer items-center gap-3 rounded-md text-black hover:text-gray-400 p-2'>
                    <UserPenIcon className='h-5 w-5'/>
                    <span className='font-sm'>RH</span>
                </li>
                <li className='flex cursor-pointer items-center gap-3 rounded-md text-black hover:text-gray-400 p-2'>
                    <BarChart2Icon className='h-5 w-5'/>
                    <span className='font-sm'>Relatórios</span>
                </li>
                <li className='flex cursor-pointer items-center gap-3 rounded-md text-black hover:text-gray-400 p-2'>
                    <WalletIcon className='h-5 w-5'/>
                    <span className='font-sm'>Financeiro</span>
                </li>
            </ul>
        </nav>

        {/* RODAPE */}
        <div>
            <ul className='flex flex-col gap-2'>
                <li className='flex cursor-pointer items-center gap-3 rounded-md text-black hover:text-gray-400 p-2'>
                    <SettingsIcon className='h-5 w-5'/>
                    <span className='font-medium'>Configurações</span>
                </li>
                <li className='flex cursor-pointer items-center gap-3 rounded-md text-red-600 hover:text-black p-2'>
                    <LogOutIcon className='h-5 w-5'/>
                    <span className='font-medium'>Sair</span>
                </li>
            </ul>
        </div>
        </aside>
    )
}