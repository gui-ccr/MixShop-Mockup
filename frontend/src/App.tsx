// src/App.tsx
import { PainelProducao } from './pages/PainelProducao'
import { Sidebar } from './components/layout/Siderbar' 

function App() {
  return (

    <div className="flex">      
      {/* 3. O ITEM DA ESQUERDA: A Sidebar */}
      <Sidebar />
      {/* 4. O ITEM DA DIREITA: O Conteúdo Principal */}
      <main className="flex-1 bg-gray-200">
        <PainelProducao />
      </main>
    </div>
  )
}

export default App