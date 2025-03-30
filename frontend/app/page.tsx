"use client"; // Для Next.js

import { useState } from 'react';

export default function Test() {
  const [message, setMessage] = useState<string>("");
  const [inputName, setInputName] = useState<string>("Гость"); // Состояние для ввода

  const fetchData = async () => {
    try {
      const encodedName = encodeURIComponent(inputName);
      const response = await fetch(`http://localhost:8000/?name=${encodedName}`);
      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="flex flex-col gap-2 max-w-md">
      {/* Поле ввода */}
      <input
        type="text"
        value={inputName}
        onChange={(e) => setInputName(e.target.value)}
        placeholder="Введите ваше имя"
        className="p-2 border rounded"
      />
      
      {/* Кнопка с обработчиком */}
      <button 
        onClick={fetchData}
        className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
      >
        Загрузить приветствие
      </button>
      
      {/* Вывод результата */}
      {message && (
        <p className="mt-4 p-2 rounded">
          Ответ сервера: <span className="font-semibold">{message}</span>
        </p>
      )}
    </div>
  );
}
