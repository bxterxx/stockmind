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
  const [noEncontrado, setNoEncontrado] = useState(false);
  const [formData, setFormData] = useState({ id: "", nombre: "" });

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
      setError("Error de conexión con el servidor. No se pudieron cargar las categorías.");
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
      await categoriasAPI.crear({
        id: parseInt(formData.id),
        nombre: formData.nombre,
      });
      setFormData({ id: "", nombre: "" });
      setShowForm(false);
      cargarCategorias();
    } catch (err) {
      setError("No se pudo guardar la categoría.");
    }
  };

  const handleEliminar = async (id) => {
    if (window.confirm("¿Estás seguro de que deseas eliminar esta categoría?")) {
      try {
        setError(null); 
        await categoriasAPI.eliminar(id);
        await cargarCategorias();
      } catch (err) {
        setError("⚠️ No se puede eliminar esta categoría porque está siendo utilizada por uno o más productos.");
      }
    }
  };

  const handleBuscarPorId = async () => {
    if (!buscarId) {
      setError("Ingresa un ID de categoría");
      return;
    }
    try {
      setError(null);
      setNoEncontrado(false);
      setDetalle(null); 

      const categoria = await categoriasAPI.obtenerPorId(parseInt(buscarId));
      if (categoria && categoria.id) {
        setDetalle(categoria);
      } else {
        setDetalle(null);
        setNoEncontrado(true); 
      }
    } catch (err) {
      setDetalle(null);
      setNoEncontrado(true);
    }
  };

  if (loading) return <div className="card"><p>Cargando categorías...</p></div>;

  return (
    <div className="card">
      <h2>🏷️ Gestión de Categorías</h2>
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
          {showForm ? "Cancelar" : "+ Nueva Categoría"}
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
            <label>ID Categoría:</label>
            <input type="number" name="id" value={formData.id} onChange={handleInputChange} required />
          </div>
          <div className="form-group">
            <label>Nombre:</label>
            <input type="text" name="nombre" value={formData.nombre} onChange={handleInputChange} required />
          </div>
          <button type="submit" className="btn-success">Guardar Categoría</button>
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
          <button className="btn-primary" onClick={handleBuscarPorId}>Buscar</button>

          {detalle && detalle.id && (
            <div className="perfil-info" style={{ marginTop: '15px' }}>
              <h4>Detalles de la Categoría</h4>
              <p><strong>ID:</strong> {detalle.id}</p>
              <p><strong>Nombre:</strong> {detalle.nombre}</p>
            </div>
          )}

          {noEncontrado && (
            <div className="error" style={{ marginTop: '15px', backgroundColor: '#ffebee', color: '#c62828', padding: '10px', borderRadius: '4px' }}>
              ⚠️ La categoría con ID <strong>{buscarId}</strong> no existe en el sistema.
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
                    <button className="btn-danger" onClick={() => handleEliminar(cat.id)}>Eliminar</button>
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