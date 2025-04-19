import React, { useEffect, useState } from "react";
import {
  BarChart, Bar, PieChart, Pie, Cell, LineChart, Line,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from "recharts";

const COLORS = ["#4ade80", "#f87171"];

const WinLossCharts = () => {
  const [logs, setLogs] = useState([]);
  const [view, setView] = useState("bar");

  useEffect(() => {
    fetch("http://localhost:8000/logs")
      .then(res => res.json())
      .then(data => setLogs(data))
      .catch(err => console.error("Failed to fetch logs:", err));
  }, []);

  // Data transforms
  const resultCount = logs.reduce((acc, log) => {
    if (!log.result) return acc;
    acc[log.result] = (acc[log.result] || 0) + 1;
    return acc;
  }, {});
  

  const resultData = Object.entries(resultCount).map(([k, v]) => ({
    name: k, value: v
  }));

  const trendData = logs.reduce((acc, log) => {
    if (!log.result) return acc;  // ✅ Add this at the top
    const date = new Date(log.timestamp).toISOString().split("T")[0];
    if (!acc[date]) acc[date] = { date, win: 0, loss: 0 };
    acc[date][log.result]++;
    return acc;
  }, {});

  const profitLossData = logs.reduce((acc, log) => {
    if (!log.result) return acc;
    const date = new Date(log.timestamp).toISOString().split("T")[0];
    const change = log.result === "win" ? 1 : -1;  // 🧪 1 unit win/loss
    acc[date] = (acc[date] || 0) + change;
    return acc;
  }, {});
  
  const plTrend = Object.entries(profitLossData).map(([date, value]) => ({
    date,
    net: value,
  }));

  const trendList = Object.values(trendData);

  console.log("ResultData:", resultData);
  console.log("TrendData:", trendList);


  return (
    <div className="p-4">
      <div className="flex gap-2 mb-4">
        {["bar", "pie", "line", "pl"].map((type) => (
          <button
            key={type}
            className={`px-4 py-1 rounded ${
              view === type ? "bg-blue-600 text-white" : "bg-gray-200"
            }`}
            onClick={() => setView(type)}
          >
            {type.toUpperCase()}
          </button>
        ))}
      </div>

      <div style={{ height: "300px", width: "100%" }}>
        <ResponsiveContainer width="100%" height="100%">
          {view === "bar" && (
            <BarChart data={resultData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="value" fill="#4f46e5" />
            </BarChart>
          )}
          {view === "pie" && (
            <PieChart>
              <Pie
                data={resultData}
                dataKey="value"
                nameKey="name"
                cx="50%"
                cy="50%"
                outerRadius={90}
                label
              >
                {resultData.map((_, idx) => (
                  <Cell key={idx} fill={COLORS[idx % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
              <Legend />
            </PieChart>
          )}
          {view === "line" && (
            <LineChart data={trendList}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="win" stroke="#22c55e" />
              <Line type="monotone" dataKey="loss" stroke="#ef4444" />
            </LineChart>
          )}
          {view === "pl" && (
            <LineChart data={plTrend}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="net" stroke="#0ea5e9" />
            </LineChart>
          )}

        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default WinLossCharts;
