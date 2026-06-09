import React, { useState, useEffect } from "react";
import { proveedoresAPI } from "../services/api";
import "../styles/Componentes.css";

export const Proveedores = () => {
  const [proveedores, setProveedores] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [showBuscar, setShowBuscar] = useState(false);
  const [detalle, setDetalle] = useState(null);
  const [buscarId, setBuscarId] = useState("");
  const [noEncontrado, setNoEncontrado] = useState(false);
  const [formData, setFormData] = useState({ id: "", nombre_empresa: "", telefono: "" });

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
      setError("Error de conexión con el servidor. No se pudieron cargar los proveedores.");
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
      await proveedoresAPI.crear({
        id: parseInt(formData.id),
        nombre_empresa: formData.nombre_empresa,
        telefono: formData.telefono,
      });
      setFormData({ id: "", nombre_empresa: "", telefono: "" });
      setShowForm(false);
      cargarProveedores();
    } catch (err) {
      setError("No se pudo guardar el proveedor.");
    }
  };

  const handleEliminar = async (id) => {
    if (window.confirm("¿Estás seguro de que deseas eliminar este proveedor?")) {
      try {
        setError(null);
        await proveedoresAPI.eliminar(id);
        cargarProveedores();
      } catch (err) {
        setError("⚠️ No se puede eliminar este proveedor porque está siendo utilizado por uno o más productos.");
      }
    }
  };

  const handleBuscarPorId = async () => {
    if (!buscarId) {
      setError("Ingresa un ID de proveedor");
      return;
    }
    setError(null);
    setNoEncontrado(false);
    setDetalle(null);

    const proveedorEncontrado = proveedores.find(
      (p) => parseInt(p.id) === parseInt(buscarId)
    );

    if (proveedorEncontrado) {
      setDetalle(proveedorEncontrado);
    } else {
      setDetalle(null);
      setNoEncontrado(true);
    }
  };

  if (loading) return <div className="card"><p>Cargando proveedores...</p></div>;

  return (
    <div className="card">
      <h2>🏢 Gestión de Proveedores</h2>
      {error && <div className="error">{error}</div>}

      <div style={{ display: 'flex', gap: '15px', marginBottom: '20px', alignItems: 'center' }}>
        <button 
          className="btn-primary" 
          onClick={() => {
            setShowForm(!showForm);
            setError(null);
            if(showBuscar) setShowBuscar(false);
          }}
          style={{ 
            display: 'inline-flex', 
            alignItems: 'center', 
            gap: '8px',
            backgroundColor: showForm ? '#d32f2f' : '',
            borderColor: showForm ? '#d32f2f' : ''
          }}
        >
          {showForm ? "Cancelar" : "+ Nuevo Proveedor"}
        </button>

        <button 
          className={showBuscar ? "btn-primary" : "btn-secondary"} 
          onClick={() => {
            setShowBuscar(!showBuscar);
            setNoEncontrado(false);
            setError(null);
            setDetalle(null);
            if(showForm) setShowForm(false);
          }}
          style={{ 
            display: 'inline-flex', 
            alignItems: 'center', 
            gap: '8px',
            backgroundColor: showBuscar ? '#d32f2f' : '',
            borderColor: showBuscar ? '#d32f2f' : ''
          }}
        >
          {showBuscar ? "Cancelar" : "🔍 Ver Detalles"}
        </button>
      </div>

      {showForm && (
        <form onSubmit={handleSubmit} className="form">
          <div className="form-group">
            <label>ID Proveedor:</label>
            <input type="number" name="id" value={formData.id} onChange={handleInputChange} required />
          </div>
          <div className="form-group">
            <label>Nombre Empresa:</label>
            <input type="text" name="nombre_empresa" value={formData.nombre_empresa} onChange={handleInputChange} required />
          </div>
          <div className="form-group">
            <label>Teléfono:</label>
            <input type="text" name="telefono" value={formData.telefono} onChange={handleInputChange} required />
          </div>
          <button type="submit" className="btn-success">Guardar Proveedor</button>
        </form>
      )}

      {showBuscar && (
        <div className="form">
          <h3>Buscar Proveedor por ID</h3>
          <div className="form-group">
            <label>ID Proveedor:</label>
            <input
              type="number"
              value={buscarId}
              onChange={(e) => setBuscarId(e.target.value)}
              placeholder="Ingresa el ID del proveedor"
            />
          </div>
          <button className="btn-primary" onClick={handleBuscarPorId}>Buscar</button>

          {detalle && (detalle.id || detalle.id_proveedor) && (
            <div className="perfil-info" style={{ marginTop: '15px' }}>
              <h4>Detalles del Proveedor</h4>
              <p><strong>ID:</strong> {detalle.id ? detalle.id : detalle.id_proveedor}</p>
              <p><strong>Nombre Empresa:</strong> {detalle.nombre_empresa}</p>
              <p><strong>Teléfono:</strong> {detalle.telefono}</p>
            </div>
          )}

          {noEncontrado && (
            <div className="error" style={{ marginTop: '15px', backgroundColor: '#ffebee', color: '#c62828', padding: '10px', borderRadius: '4px' }}>
              ⚠️ El proveedor con ID <strong>{buscarId}</strong> no existe en el sistema.
            </div>
          )}
        </div>
      )}

      {proveedores.length === 0 ? (
        <p>No hay proveedores registrados</p>
      ) : (
        <div className="table-container">
          <table className="table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nombre Empresa</th>
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
                    <button className="btn-danger" onClick={() => handleEliminar(prov.id)}>Eliminar</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}