import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MonthTable = () => {
 const [months, setMonths] = useState([
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
 ]);
 const [expenses, setExpenses] = useState({});

 useEffect(() => {
  const fetchExpenses = async () => {
     try {
       const response = await axios.get('http://localhost:5000/api/expenses/');
       const expensesByName = {};
       response.data.forEach(expense => {
         // Agrupa as despesas por nome
         expensesByName[expense.name] = expense;
       });
       setExpenses(expensesByName);
     } catch (error) {
       console.error('Erro ao buscar despesas:', error);
     }
  };
  fetchExpenses();
 }, []);
 
 
 

 return (
    <div className="month-table">
      <h2>Despesas por Mês</h2>
      <table>
        <thead>
          <tr>
            <th>Mês</th>
            {Object.keys(expenses).map(expenseName => (
              <th key={expenseName}>{expenseName}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {months.map((month, index) => (
            <tr key={index}>
              <td>{month}</td>
              {Object.keys(expenses).map(expenseName => (
                <td key={expenseName}>
                 {/* Aqui você pode adicionar a lógica para exibir o valor da despesa para o mês específico */}
                 {/* Por exemplo, se cada despesa tiver um valor específico para cada mês, você pode acessá-lo aqui */}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
);
};

export default MonthTable;
