import React, { useState } from "react";
import { usuariosAPI } from "../services/api";
import "../styles/Componentes.css";

export const Usuarios = () => {
  const [usuarios, setUsuarios] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [showPerfil, setShowPerfil] = useState(false);
  const [usuarioPerfil, setUsuarioPerfil] = useState(null);
  const [formData, setFormData] = useState({
    id_usuario: "",
    nombre_completo: "",
    username: "",
    password: "",
    rol: "usuario",
  });
  const [buscarId, setBuscarId] = useState("");

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      const nuevoUsuario = await usuariosAPI.registrar({
        id_usuario: parseInt(formData.id_usuario),
        nombre_completo: formData.nombre_completo,
        username: formData.username,
        password: formData.password,
        rol: formData.rol,
      });
      setUsuarios([...usuarios, nuevoUsuario]);
      setFormData({
        id_usuario: "",
        nombre_completo: "",
        username: "",
        password: "",
        rol: "usuario",
      });
      setShowForm(false);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleBuscarPerfil = async () => {
    if (!buscarId) {
      setError("Ingresa un ID de usuario");
      return;
    }
    try {
      setLoading(true);
      const perfil = await usuariosAPI.verPerfil(parseInt(buscarId));
      setUsuarioPerfil(perfil);
      setShowPerfil(true);
      setError(null);
    } catch (err) {
      setError(err.message);
      setShowPerfil(false);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>👥 Registro de Usuarios</h2>
      {error && <div className="error">{error}</div>}

      <div className="button-group">
        <button className="btn-primary" onClick={() => setShowForm(!showForm)}>
          {showForm ? "Cancelar" : "+ Nuevo Usuario"}
        </button>
        <button className="btn-secondary" onClick={() => setShowPerfil(!showPerfil)}>
          {showPerfil ? "Cancelar" : "🔍 Ver Perfil"}
        </button>
      </div>

      {showForm && (
        <form onSubmit={handleSubmit} className="form">
          <div className="form-group">
            <label>ID Usuario:</label>
            <input
              type="number"
              name="id_usuario"
              value={formData.id_usuario}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Nombre Completo:</label>
            <input
              type="text"
              name="nombre_completo"
              value={formData.nombre_completo}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Username:</label>
            <input
              type="text"
              name="username"
              value={formData.username}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Password:</label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Rol:</label>
            <select name="rol" value={formData.rol} onChange={handleInputChange}>
              <option value="usuario">Usuario</option>
              <option value="administrador">Administrador</option>
              <option value="gerente">Gerente</option>
            </select>
          </div>
          <button type="submit" className="btn-success" disabled={loading}>
            {loading ? "Registrando..." : "Registrar Usuario"}
          </button>
        </form>
      )}

      {showPerfil && (
        <div className="form">
          <h3>Buscar Perfil de Usuario</h3>
          <div className="form-group">
            <label>ID Usuario:</label>
            <input
              type="number"
              value={buscarId}
              onChange={(e) => setBuscarId(e.target.value)}
              placeholder="Ingresa el ID"
            />
          </div>
          <button className="btn-primary" onClick={handleBuscarPerfil} disabled={loading}>
            {loading ? "Buscando..." : "Buscar"}
          </button>

          {usuarioPerfil && (
            <div className="perfil-info">
              <h4>Información del Usuario</h4>
              <p><strong>ID:</strong> {usuarioPerfil.id}</p>
              <p><strong>Nombre:</strong> {usuarioPerfil.nombre_completo}</p>
              <p><strong>Username:</strong> {usuarioPerfil.username}</p>
              <p><strong>Rol:</strong> {usuarioPerfil.rol}</p>
            </div>
          )}
        </div>
      )}

      {usuarios.length > 0 && (
        <div className="usuarios-list">
          <h3>Usuarios Registrados</h3>
          <ul>
            {usuarios.map((usr) => (
              <li key={usr.id_usuario}>
                {usr.nombre_completo} ({usr.username}) - {usr.rol}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};
