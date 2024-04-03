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
       const response = await axios.get('http://localhost:8000/api/expenses/');
       const expensesByMonth = {};
       // Supondo que você queira exibir todas as despesas em todos os meses
       months.forEach(month => {
         expensesByMonth[month] = [];
       });
       response.data.forEach(expense => {
         // Adiciona cada despesa a todos os meses
         months.forEach(month => {
           expensesByMonth[month].push(expense.name);
         });
       });
       setExpenses(expensesByMonth);
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
            <th>Despesas</th>
          </tr>
        </thead>
        <tbody>
          {months.map((month, index) => (
            <tr key={index}>
              <td>{month}</td>
              <td>
                {expenses[month]}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
 );
};

export default MonthTable;
