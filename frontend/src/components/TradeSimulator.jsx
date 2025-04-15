import React, { useState } from "react";

const TradeSimulator = ({ onTrade }) => {
  const [symbol, setSymbol] = useState("AAPL");
  const [message, setMessage] = useState("");

  const simulateTrade = async () => {
    try {
      const res = await fetch(`http://localhost:8000/trade?symbol=${symbol}`, {
        method: "POST",
      });
      const data = await res.json();
      setMessage(data.message);
      onTrade(); // refresh logs after trade
    } catch (err) {
      setMessage("Trade failed.");
      console.error(err);
    }
  };

  return (
    <div className="mb-6 p-4">
      <h2 className="text-lg font-bold mb-2">Simulate Trade</h2>
      <div className="flex gap-2 items-center">
        <input
          className="border px-2 py-1 rounded"
          value={symbol}
          onChange={(e) => setSymbol(e.target.value.toUpperCase())}
          placeholder="Enter symbol (e.g., AAPL)"
        />
        <button
          className="bg-blue-600 text-white px-4 py-1 rounded hover:bg-blue-700"
          onClick={simulateTrade}
        >
          Trade
        </button>
      </div>
      {message && <p className="mt-2 text-sm text-gray-700">{message}</p>}
    </div>
  );
};

export default TradeSimulator;
