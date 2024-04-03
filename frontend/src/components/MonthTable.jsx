import React, { useState } from 'react';

const MonthTable = () => {
  const [months] = useState([
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
  ]);

  return (
    <div className="month-table">
      <h2>Despesas por Mês</h2>
      <table>
        <thead>
          <tr>
            <th>Mês</th>
          </tr>
        </thead>
        <tbody>
          {months.map((month, index) => (
            <tr key={index}>
              <td>{month}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default MonthTable;
