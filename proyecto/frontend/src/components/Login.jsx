import React, { useState } from "react";
import { usuariosAPI } from "../services/api";
import { guardarSesion } from "../auth";
import "../styles/Componentes.css";

export const Login = ({ onLogin }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError("");
    try {
      const usuario = await usuariosAPI.login(username, password);
      guardarSesion(usuario);
      onLogin(usuario);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-page">
      <form className="login-card" onSubmit={handleSubmit}>
        <div className="login-logo">📊</div>
        <h1>StockMind</h1>
        <p>Inicia sesión para continuar</p>
        {error && <div className="error">{error}</div>}
        <div className="form-group">
          <label>Usuario</label>
          <input
            type="text"
            value={username}
            onChange={(event) => setUsername(event.target.value)}
            placeholder="Nombre de usuario"
            required
          />
        </div>
        <div className="form-group">
          <label>Contraseña</label>
          <input
            type="password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
            placeholder="Contraseña"
            required
          />
        </div>
        <button className="btn-primary login-button" type="submit" disabled={loading}>
          {loading ? "Ingresando..." : "Iniciar sesión"}
        </button>
      </form>
    </div>
  );
};
