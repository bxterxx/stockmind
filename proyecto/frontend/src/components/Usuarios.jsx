import React, { useState, useEffect } from "react";
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

  useEffect(() => {
    cargarUsuarios();
  }, []);

  const cargarUsuarios = async () => {
    try {
      setLoading(true);
      setError(null);
      
      let respuesta = null;

      // Buscamos inteligentemente cuál método existe en tu api.js
      if (typeof usuariosAPI.listar === "function") {
        respuesta = await usuariosAPI.listar();
      } else if (typeof usuariosAPI.obtenerTodos === "function") {
        respuesta = await usuariosAPI.obtenerTodos();
      } else if (typeof usuariosAPI.obtenerTodas === "function") {
        respuesta = await usuariosAPI.obtenerTodas();
      } else {
        setError("⚠️ No se encontró una función como 'listar' o 'obtenerTodos' dentro de usuariosAPI en tu archivo services/api.js");
        setLoading(false);
        return;
      }

      console.log("Datos que llegaron de la base de datos:", respuesta);

      // Validamos el formato en el que responde tu servidor
      if (Array.isArray(respuesta)) {
        setUsuarios(respuesta);
      } else if (respuesta && Array.isArray(respuesta.usuarios)) {
        setUsuarios(respuesta.usuarios);
      } else if (respuesta && Array.isArray(respuesta.data)) {
        setUsuarios(respuesta.data);
      } else {
        setUsuarios([]);
      }
    } catch (err) {
      console.error("Error al conectar con usuariosAPI:", err);
      setError("Hubo un problema de conexión al cargar los usuarios.");
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      await usuariosAPI.registrar({
        id_usuario: parseInt(formData.id_usuario),
        nombre_completo: formData.nombre_completo,
        username: formData.username,
        password: formData.password,
        rol: formData.rol,
      });
      
      setFormData({ id_usuario: "", nombre_completo: "", username: "", password: "", rol: "usuario" });
      setShowForm(false);
      setError(null);
      cargarUsuarios(); // Recargar de la base de datos real
    } catch (err) {
      setError("No se pudo registrar el usuario. Verifica los datos.");
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
      setError(null);
      setUsuarioPerfil(null);
      const perfil = await usuariosAPI.verPerfil(parseInt(buscarId));
      if (perfil && (perfil.id || perfil.id_usuario)) {
        setUsuarioPerfil(perfil);
      } else {
        setError(`⚠️ El usuario con ID ${buscarId} no existe.`);
      }
    } catch (err) {
      setError(`⚠️ El usuario con ID ${buscarId} no existe.`);
      setUsuarioPerfil(null);
    } finally {
      setLoading(false);
    }
  };

  const handleEliminarUsuario = async (id) => {
    if (window.confirm("¿Estás seguro de que deseas eliminar este usuario?")) {
      try {
        setError(null);
        if (typeof usuariosAPI.eliminar === "function") {
          await usuariosAPI.eliminar(id);
          cargarUsuarios();
        } else {
          setError("⚠️ El método 'eliminar' no está definido en usuariosAPI dentro de tu api.js");
        }
      } catch (err) {
        setError("⚠️ No se pudo eliminar el usuario.");
      }
    }
  };

  return (
    <div className="card">
      <h2>👥 Registro de Usuarios</h2>
      {error && <div className="error">{error}</div>}

      <div style={{ display: 'flex', gap: '12px', marginBottom: '25px', alignItems: 'center', flexWrap: 'wrap' }}>
        <button 
          className="btn-primary" 
          onClick={() => {
            setShowForm(!showForm);
            setError(null);
            if(showPerfil) setShowPerfil(false);
          }}
          style={{
            display: 'inline-flex', alignItems: 'center', gap: '8px',
            backgroundColor: showForm ? '#d32f2f' : '', borderColor: showForm ? '#d32f2f' : ''
          }}
        >
          {showForm ? "Cancelar" : "+ Nuevo Usuario"}
        </button>
        
        <button 
          className={showPerfil ? "btn-primary" : "btn-secondary"} 
          onClick={() => {
            setShowPerfil(!showPerfil);
            setError(null);
            setUsuarioPerfil(null);
            if(showForm) setShowForm(false);
          }}
          style={{
            display: 'inline-flex', alignItems: 'center', gap: '8px',
            backgroundColor: showPerfil ? '#d32f2f' : '', borderColor: showPerfil ? '#d32f2f' : ''
          }}
        >
          {showPerfil ? "Cancelar" : "🔍 Ver Perfil"}
        </button>
      </div>

      {showForm && (
        <form onSubmit={handleSubmit} className="form">
          <div className="form-group">
            <label>ID Usuario:</label>
            <input type="number" name="id_usuario" value={formData.id_usuario} onChange={handleInputChange} required />
          </div>
          <div className="form-group">
            <label>Nombre Completo:</label>
            <input type="text" name="nombre_completo" value={formData.nombre_completo} onChange={handleInputChange} required />
          </div>
          <div className="form-group">
            <label>Username:</label>
            <input type="text" name="username" value={formData.username} onChange={handleInputChange} required />
          </div>
          <div className="form-group">
            <label>Password:</label>
            <input type="password" name="password" value={formData.password} onChange={handleInputChange} required />
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
            Registrar Usuario
          </button>
        </form>
      )}

      {showPerfil && (
        <div className="form">
          <h3>Buscar Perfil de Usuario</h3>
          <div className="form-group">
            <label>ID Usuario:</label>
            <input type="number" value={buscarId} onChange={(e) => setBuscarId(e.target.value)} placeholder="Ingresa el ID" />
          </div>
          <button className="btn-primary" onClick={handleBuscarPerfil}>Buscar</button>

          {usuarioPerfil && (
            <div className="perfil-info" style={{ marginTop: '15px' }}>
              <h4>Información del Usuario</h4>
              <p><strong>ID:</strong> {usuarioPerfil.id || usuarioPerfil.id_usuario}</p>
              <p><strong>Nombre:</strong> {usuarioPerfil.nombre_completo}</p>
              <p><strong>Username:</strong> {usuarioPerfil.username}</p>
              <p><strong>Rol:</strong> {usuarioPerfil.rol}</p>
            </div>
          )}
        </div>
      )}

      <div className="table-container" style={{ marginTop: '30px' }}>
        <h3>Usuarios Registrados</h3>
        {loading && usuarios.length === 0 ? (
          <p>Cargando información desde la base de datos...</p>
        ) : usuarios.length === 0 ? (
          <p>No se encontraron usuarios en este formato. Revisa las alertas de arriba.</p>
        ) : (
          <table className="table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nombre Completo</th>
                <th>Nombre de Usuario</th>
                <th>Rol de Sistema</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              {usuarios.map((usr) => {
                const idActual = usr.id_usuario || usr.id;
                return (
                  <tr key={idActual}>
                    <td>{idActual}</td>
                    <td><strong>{usr.nombre_completo}</strong></td>
                    <td>{usr.username}</td>
                    <td>
                      <span style={{
                        padding: '4px 10px', 
                        borderRadius: '4px', 
                        backgroundColor: '#e8f5e9', 
                        color: '#2e7d32', 
                        fontSize: '0.85rem', 
                        fontWeight: 'bold'
                      }}>
                        {usr.rol}
                      </span>
                    </td>
                    <td>
                      <button 
                        className="btn-danger" 
                        onClick={() => handleEliminarUsuario(idActual)}
                      >
                        Eliminar
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}