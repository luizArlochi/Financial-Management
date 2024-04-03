import React, { useState } from 'react';
import './App.css';
import MonthTable from './components/MonthTable';
import AddLabel from './components/AddLabel';

function App() {
  const [isAddingLabel, setIsAddingLabel] = useState(false);

  const handleLabelAdded = () => {
    // Aqui você pode fazer alguma ação após adicionar a despesa, como atualizar a tabela de meses
    console.log('Despesa adicionada com sucesso!');
    // Fechar o formulário de adição após adicionar a despesa
    setIsAddingLabel(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Controle Financeiro</h1>
      </header>
      <main>
        <MonthTable />
        {isAddingLabel && <AddLabel onLabelAdded={handleLabelAdded} />}
        <button onClick={() => setIsAddingLabel(true)}>Adicionar Despesa</button>
      </main>
    </div>
  );
}

export default App;
