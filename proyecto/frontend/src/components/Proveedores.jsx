import React, { useState, useEffect } from "react";
import { proveedoresAPI } from "../services/api";
import "../styles/Componentes.css";

export const Proveedores = () => {
  const [proveedores, setProveedores] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    id: "",
    nombre_empresa: "",
    telefono: "",
  });

  useEffect(() => {
    cargarProveedores();
  }, []);

  const cargarProveedores = async () => {
    try {
      setLoading(true);
      const data = await proveedoresAPI.listar();
      setProveedores(data);
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
      await proveedoresAPI.crear({
        id: parseInt(formData.id),
        nombre_empresa: formData.nombre_empresa,
        telefono: formData.telefono,
      });
      setFormData({ id: "", nombre_empresa: "", telefono: "" });
      setShowForm(false);
      cargarProveedores();
    } catch (err) {
      setError(err.message);
    }
  };

  const handleEliminar = async (id) => {
    if (window.confirm("¿Estás seguro de que deseas eliminar este proveedor?")) {
      try {
        await proveedoresAPI.eliminar(id);
        cargarProveedores();
      } catch (err) {
        setError(err.message);
      }
    }
  };

  if (loading) return <div className="card"><p>Cargando proveedores...</p></div>;

  return (
    <div className="card">
      <h2>🏢 Registro de Proveedores</h2>
      {error && <div className="error">{error}</div>}

      <button className="btn-primary" onClick={() => setShowForm(!showForm)}>
        {showForm ? "Cancelar" : "+ Nuevo Proveedor"}
      </button>

      {showForm && (
        <form onSubmit={handleSubmit} className="form">
          <div className="form-group">
            <label>ID Proveedor:</label>
            <input
              type="number"
              name="id"
              value={formData.id}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Nombre Empresa:</label>
            <input
              type="text"
              name="nombre_empresa"
              value={formData.nombre_empresa}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Teléfono:</label>
            <input
              type="tel"
              name="telefono"
              value={formData.telefono}
              onChange={handleInputChange}
              required
            />
          </div>
          <button type="submit" className="btn-success">
            Guardar Proveedor
          </button>
        </form>
      )}

      {proveedores.length === 0 ? (
        <p>No hay proveedores registrados</p>
      ) : (
        <div className="table-container">
          <table className="table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Empresa</th>
                <th>Teléfono</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              {proveedores.map((prov) => (
                <tr key={prov.id}>
                  <td>{prov.id}</td>
                  <td>{prov.nombre_empresa}</td>
                  <td>{prov.telefono}</td>
                  <td>
                    <button
                      className="btn-danger"
                      onClick={() => handleEliminar(prov.id)}
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
