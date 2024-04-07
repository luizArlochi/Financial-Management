import React, { useState } from 'react';
import axios from 'axios';


const AddLabel = ({ onLabelAdded }) => {
  const [name, setName] = useState('');
  const [tag, setTag] = useState('');
  const [color, setColor] = useState('');

  const handleAddLabel = async () => {
    try {
      await axios.post('http://localhost:5000/api/expenses/', { name, tag, color }, {
        headers: {
          'Content-Type': 'application/json',
        },
      
      });
      onLabelAdded();
      setName('');
      setTag('');
      setColor('');
    } catch (error) {
      console.error('Erro ao adicionar despesa:', error);
    }
  };

  return (
    <div className="add-label">
      <h2>Adicionar Despesa</h2>
      <label>
        Nome da Despesa:
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      <label>
        Tag:
        <input
          type="text"
          value={tag}
          onChange={(e) => setTag(e.target.value)}
        />
      </label>
      <label>
        Cor:
        <input
          type="color"
          value={color}
          onChange={(e) => setColor(e.target.value)}
        />
      </label>
      <button onClick={handleAddLabel}>Adicionar Despesa</button>
    </div>
  );
};

export default AddLabel;
