import React, { useState, useEffect } from "react";
import { categoriasAPI } from "../services/api";
import "../styles/Componentes.css";

export const Categorias = () => {
  const [categorias, setCategorias] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [showBuscar, setShowBuscar] = useState(false);
  const [detalle, setDetalle] = useState(null);
  const [buscarId, setBuscarId] = useState("");
  const [formData, setFormData] = useState({
    id: "",
    nombre: "",
  });

  useEffect(() => {
    cargarCategorias();
  }, []);

  const cargarCategorias = async () => {
    try {
      setLoading(true);
      const data = await categoriasAPI.obtenerTodas();
      setCategorias(data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

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
      const nuevaCategoria = {
        id: parseInt(formData.id),
        nombre: formData.nombre,
      };
      await categoriasAPI.crear(nuevaCategoria);
      setFormData({ id: "", nombre: "" });
      setShowForm(false);
      cargarCategorias();
    } catch (err) {
      setError(err.message);
    }
  };

  const handleEliminar = async (id) => {
    if (window.confirm("¿Estás seguro de que deseas eliminar esta categoría?")) {
      try {
        await categoriasAPI.eliminar(id);
        cargarCategorias();
      } catch (err) {
        setError(err.message);
      }
    }
  };

  const handleBuscarPorId = async () => {
    if (!buscarId) {
      setError("Ingresa un ID de categoría");
      return;
    }
    try {
      const categoria = await categoriasAPI.obtenerPorId(parseInt(buscarId));
      setDetalle(categoria);
    } catch (err) {
      setError(err.message);
      setDetalle(null);
    }
  };

  if (loading) return <div className="card"><p>Cargando categorías...</p></div>;

  return (
    <div className="card">
      <h2>🏷️ Gestión de Categorías</h2>
      {error && <div className="error">{error}</div>}

      <button className="btn-primary" onClick={() => setShowForm(!showForm)}>
        {showForm ? "Cancelar" : "+ Nueva Categoría"}
      </button>

      <button className="btn-secondary" onClick={() => setShowBuscar(!showBuscar)}>
        {showBuscar ? "Cancelar" : "🔍 Ver Detalles"}
      </button>

      {showForm && (
        <form onSubmit={handleSubmit} className="form">
          <div className="form-group">
            <label>ID Categoría:</label>
            <input
              type="number"
              name="id"
              value={formData.id}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Nombre:</label>
            <input
              type="text"
              name="nombre"
              value={formData.nombre}
              onChange={handleInputChange}
              required
            />
          </div>
          <button type="submit" className="btn-success">
            Guardar Categoría
          </button>
        </form>
      )}

      {showBuscar && (
        <div className="form">
          <h3>Buscar Categoría por ID</h3>
          <div className="form-group">
            <label>ID Categoría:</label>
            <input
              type="number"
              value={buscarId}
              onChange={(e) => setBuscarId(e.target.value)}
              placeholder="Ingresa el ID de la categoría"
            />
          </div>
          <button className="btn-primary" onClick={handleBuscarPorId}>
            Buscar
          </button>

          {detalle && (
            <div className="perfil-info">
              <h4>Detalles de la Categoría</h4>
              <p><strong>ID:</strong> {detalle.id}</p>
              <p><strong>Nombre:</strong> {detalle.nombre}</p>
            </div>
          )}
        </div>
      )}

      {categorias.length === 0 ? (
        <p>No hay categorías registradas</p>
      ) : (
        <div className="table-container">
          <table className="table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              {categorias.map((cat) => (
                <tr key={cat.id}>
                  <td>{cat.id}</td>
                  <td>{cat.nombre}</td>
                  <td>
                    <button
                      className="btn-danger"
                      onClick={() => handleEliminar(cat.id)}
                    >
                      Eliminar
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};
