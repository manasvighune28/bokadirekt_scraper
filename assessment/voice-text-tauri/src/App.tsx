import { useMicrophone } from "./hooks/useMicrophone";
import "./App.css";

function App() {
  const mic = useMicrophone();

  return (
    <main className="container">
      <h1>Voice to Text (Tauri + React)</h1>

      <p>Mic status: {mic.state}</p>
      {mic.error && <p style={{ color: "red" }}>{mic.error}</p>}

      <div className="row" style={{ gap: "12px", marginTop: "16px" }}>
        <button onClick={mic.start}>Start Mic</button>
        <button onClick={mic.stop}>Stop Mic</button>
      </div>
    </main>
  );
}

export default App;
