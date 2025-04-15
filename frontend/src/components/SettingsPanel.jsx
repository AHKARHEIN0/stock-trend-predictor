import React, { useEffect, useState } from "react";

const SettingsPanel = () => {
  const [settings, setSettings] = useState({});
  const [message, setMessage] = useState("");

  const fetchSettings = async () => {
    try {
      const res = await fetch("http://localhost:8000/settings");
      const data = await res.json();
      setSettings(data);
    } catch (err) {
      console.error("Failed to fetch settings");
    }
  };

  const updateSetting = async (key, value) => {
    try {
      await fetch("http://localhost:8000/settings", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ key, value: String(value) }),
      });
      setMessage(`Updated ${key}`);
      fetchSettings(); // refresh
    } catch (err) {
      setMessage("Failed to update.");
    }
  };

  useEffect(() => {
    fetchSettings();
  }, []);

  return (
    <div className="p-4 border mb-6">
      <h2 className="text-lg font-bold mb-2">Trading Settings</h2>
      {Object.entries(settings).map(([key, value]) => (
        <div key={key} className="mb-2 flex gap-2 items-center">
          <label className="w-48">{key}</label>
          <input
            type="text"
            value={value}
            onChange={(e) =>
              setSettings({ ...settings, [key]: e.target.value })
            }
            className="border px-2 py-1 rounded w-32"
          />
          <button
            className="bg-green-600 text-white px-3 py-1 rounded hover:bg-green-700"
            onClick={() => updateSetting(key, settings[key])}
          >
            Save
          </button>
        </div>
      ))}
      {message && <p className="text-sm mt-2 text-gray-700">{message}</p>}
    </div>
  );
};

export default SettingsPanel;
