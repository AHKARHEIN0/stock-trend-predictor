import React, { useEffect, useState } from "react";
import {
  LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid
} from "recharts";

const TradeChart = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/logs")
      .then(res => res.json())
      .then(data => {
        // Count trades per date
        const grouped = {};
        data.forEach(entry => {
          const date = new Date(entry.timestamp).toISOString().split("T")[0];
          if (!grouped[date]) grouped[date] = 0;
          grouped[date]++;
        });

        const chartData = Object.entries(grouped).map(([date, count]) => ({
          date, count
        }));

        setLogs(chartData);
      })
      .catch(err => console.error("Failed to load logs:", err));
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Trades Per Day</h2>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={logs}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="count" stroke="#007bff" strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default TradeChart;
