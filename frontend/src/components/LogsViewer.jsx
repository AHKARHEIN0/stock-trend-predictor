import React, { useEffect, useState } from "react";

const LogsViewer = () => {
  const [logs, setLogs] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchLogs = async () => {
      try {
        const res = await fetch("http://localhost:8000/logs");
        const data = await res.json();
        setLogs(data);
      } catch (err) {
        setError("Failed to load logs.");
        console.error(err);
      }
    };

    fetchLogs();
  }, []);

  if (error) return <div>{error}</div>;

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Trade Log</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full border border-gray-300 text-sm">
          <thead className="bg-gray-100">
            <tr>
              <th className="px-2 py-1 border">Time</th>
              <th className="px-2 py-1 border">Symbol</th>
              <th className="px-2 py-1 border">Prediction</th>
              <th className="px-2 py-1 border">Allowed</th>
              <th className="px-2 py-1 border">Confidence</th>
              <th className="px-2 py-1 border">Price</th>
              <th className="px-2 py-1 border">Volume</th>
              <th className="px-2 py-1 border">Result</th>
            </tr>
          </thead>
          <tbody>
            {logs.length === 0 && (
              <tr>
                <td colSpan="7" className="text-center p-2">
                  No logs yet.
                </td>
              </tr>
            )}
            {logs.map((log, idx) => (
              <tr key={idx} className="hover:bg-gray-50">
                <td className="px-2 py-1 border">{log.timestamp}</td>
                <td className="px-2 py-1 border">{log.symbol}</td>
                <td className="px-2 py-1 border">{log.prediction}</td>
                <td className="px-2 py-1 border">{log.allowed ? "✅" : "❌"}</td>
                <td className="px-2 py-1 border">{log.confidence}</td>
                <td className="px-2 py-1 border">{log.price}</td>
                <td className="px-2 py-1 border">{log.volume}</td>
                <td className="px-2 py-1 border">{log.result || "-"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default LogsViewer;
