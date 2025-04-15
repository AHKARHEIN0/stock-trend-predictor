import React, { useState } from "react";
import LogsViewer from "./components/LogsViewer";
import TradeSimulator from "./components/TradeSimulator";
import TradeChart from "./components/TradeChart";
import SettingsPanel from "./components/SettingsPanel";

function App() {
  const [refresh, setRefresh] = useState(false);
  const reloadLogs = () => setRefresh((prev) => !prev);

  return (
    <div className="App max-w-5xl mx-auto p-4">
      <SettingsPanel />
      <TradeSimulator onTrade={reloadLogs} />
      <TradeChart />
      <LogsViewer key={refresh} />
    </div>
  );
}


export default App;
