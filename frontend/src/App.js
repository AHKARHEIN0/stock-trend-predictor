import React, { useState } from "react";
import LogsViewer from "./components/LogsViewer";
import TradeSimulator from "./components/TradeSimulator";

function App() {
  const [refresh, setRefresh] = useState(false);

  const reloadLogs = () => {
    setRefresh((prev) => !prev);
  };

  return (
    <div className="App max-w-4xl mx-auto p-4">
      <TradeSimulator onTrade={reloadLogs} />
      <LogsViewer key={refresh} />
    </div>
  );
}

export default App;
