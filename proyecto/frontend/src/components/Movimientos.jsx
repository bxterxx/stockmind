import React, { useState, useEffect } from "react";
import { movimientosAPI, productosAPI } from "../services/api";
import "../styles/Componentes.css";

export const Movimientos = () => {
  const [movimientos, setMovimientos] = useState([]);
  const [productos, setProductos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [showBuscar, setShowBuscar] = useState(false);
  const [showBuscarId, setShowBuscarId] = useState(false);
  const [noEncontrado, setNoEncontrado] = useState(false);
  const [formData, setFormData] = useState({
    id: "",
    Producto: "",
    Usuario: "",
    tipo: "entrada",
    cantidad: "",
    fecha: "",
  });
  const [buscarProductoId, setBuscarProductoId] = useState("");
  const [buscarMovimientoId, setBuscarMovimientoId] = useState("");
  const [movimientosProducto, setMovimientosProducto] = useState([]);
  const [detalleMovimiento, setDetalleMovimiento] = useState(null);

  useEffect(() => {
    cargarDatos();
  }, []);

  const cargarDatos = async () => {
    try {
      setLoading(true);
      const [movimientosData, productosData] = await Promise.all([
        movimientosAPI.listar(),
        productosAPI.obtenerTodos(),
      ]);
      setMovimientos(movimientosData);
      setProductos(productosData);
      setError(null);
    } catch (err) {
      setError("Error de conexión con el servidor. No se pudieron cargar los movimientos.");
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
      const fechaFormato = formData.fecha || new Date().toISOString().split("T")[0];
      await movimientosAPI.crear({
        id: parseInt(formData.id),
        Producto: parseInt(formData.Producto),
        Usuario: parseInt(formData.Usuario),
        tipo: formData.tipo,
        cantidad: parseInt(formData.cantidad),
        fecha: fechaFormato,
      });
      setFormData({ id: "", Producto: "", Usuario: "", tipo: "entrada", cantidad: "", fecha: "" });
      setShowForm(false);
      cargarDatos();
    } catch (err) {
      setError("No se pudo registrar el movimiento. Verifica los datos.");
    }
  };

  const handleBuscarPorProducto = async () => {
    if (!buscarProductoId) {
      setError("Ingresa un ID de producto");
      return;
    }
    try {
      setError(null);
      const movs = await movimientosAPI.obtenerPorProducto(parseInt(buscarProductoId));
      setMovimientosProducto(movs);
    } catch (err) {
      setError("No se encontraron movimientos para el producto especificado.");
      setMovimientosProducto([]);
    }
  };

  const handleEliminarMovimiento = async (id) => {
    if (window.confirm("¿Estás seguro de que deseas eliminar este movimiento?")) {
      try {
        setError(null);
        await movimientosAPI.eliminar(id);
        cargarDatos();
      } catch (err) {
        setError("⚠️ No se pudo eliminar el movimiento.");
      }
    }
  };

  const handleBuscarMovimientoPorId = async () => {
    if (!buscarMovimientoId) {
      setError("Ingresa un ID de movimiento");
      return;
    }
    try {
      setError(null);
      setNoEncontrado(false);
      setDetalleMovimiento(null);
      const mov = await movimientosAPI.obtenerPorId(parseInt(buscarMovimientoId));
      if (mov && mov.id) {
        setDetalleMovimiento(mov);
      } else {
        setNoEncontrado(true);
      }
    } catch (err) {
      setNoEncontrado(true);
    }
  };

  if (loading) return <div className="card"><p>Cargando movimientos...</p></div>;

  return (
    <div className="card">
      <h2>📊 Registro de Movimientos</h2>
      {error && <div className="error">{error}</div>}

      {/* Contenedor de botones alineado perfectamente en una fila limpia */}
      <div style={{ display: 'flex', gap: '12px', marginBottom: '25px', alignItems: 'center', flexWrap: 'wrap' }}>
        <button 
          className="btn-primary" 
          onClick={() => { 
            setShowForm(!showForm); 
            setError(null);
            if(showBuscar) setShowBuscar(false); 
            if(showBuscarId) setShowBuscarId(false); 
          }}
          style={{
            display: 'inline-flex', alignItems: 'center', gap: '8px',
            backgroundColor: showForm ? '#d32f2f' : '', borderColor: showForm ? '#d32f2f' : ''
          }}
        >
          {showForm ? "Cancelar" : "+ Nuevo Movimiento"}
        </button>
        
        <button 
          className={showBuscar ? "btn-primary" : "btn-secondary"} 
          onClick={() => { 
            setShowBuscar(!showBuscar); 
            setError(null);
            if(showForm) setShowForm(false); 
            if(showBuscarId) setShowBuscarId(false); 
          }}
          style={{
            display: 'inline-flex', alignItems: 'center', gap: '8px',
            backgroundColor: showBuscar ? '#d32f2f' : '', borderColor: showBuscar ? '#d32f2f' : ''
          }}
        >
          {showBuscar ? "Cancelar" : "🔍 Por Producto"}
        </button>
        
        <button 
          className={showBuscarId ? "btn-primary" : "btn-secondary"} 
          onClick={() => { 
            setShowBuscarId(!showBuscarId); 
            setNoEncontrado(false); 
            setError(null);
            setDetalleMovimiento(null); 
            if(showForm) setShowForm(false); 
            if(showBuscar) setShowBuscar(false); 
          }}
          style={{
            display: 'inline-flex', alignItems: 'center', gap: '8px',
            backgroundColor: showBuscarId ? '#d32f2f' : '', borderColor: showBuscarId ? '#d32f2f' : ''
          }}
        >
          {showBuscarId ? "Cancelar" : "🔍 Por ID"}
        </button>
      </div>

      {showForm && (
        <form onSubmit={handleSubmit} className="form">
          <div className="form-group">
            <label>ID Movimiento:</label>
            <input type="number" name="id" value={formData.id} onChange={handleInputChange} required />
          </div>
          <div className="form-group">
            <label>Producto:</label>
            <select name="Producto" value={formData.Producto} onChange={handleInputChange} required>
              <option value="">Selecciona un producto</option>
              {productos.map((prod) => (
                <option key={prod.id} value={prod.id}>{prod.nombre}</option>
              ))}
            </select>
          </div>
          <div className="form-group">
            <label>ID Usuario:</label>
            <input type="number" name="Usuario" value={formData.Usuario} onChange={handleInputChange} required placeholder="ID del usuario" />
          </div>
          <div className="form-group">
            <label>Tipo:</label>
            <select name="tipo" value={formData.tipo} onChange={handleInputChange}>
              <option value="entrada">Entrada</option>
              <option value="salida">Salida</option>
            </select>
          </div>
          <div className="form-group">
            <label>Cantidad:</label>
            <input type="number" name="cantidad" value={formData.cantidad} onChange={handleInputChange} required />
          </div>
          <div className="form-group">
            <label>Fecha:</label>
            <input type="date" name="fecha" value={formData.fecha} onChange={handleInputChange} />
          </div>
          <button type="submit" className="btn-success">Registrar Movimiento</button>
        </form>
      )}

      {showBuscar && (
        <div className="form">
          <h3>Buscar Movimientos por Producto</h3>
          <div className="form-group">
            <label>ID Producto:</label>
            <input type="number" value={buscarProductoId} onChange={(e) => setBuscarProductoId(e.target.value)} placeholder="Ingresa el ID del producto" />
          </div>
          <button className="btn-primary" onClick={handleBuscarPorProducto}>Buscar</button>

          {movimientosProducto.length > 0 && (
            <div className="table-container" style={{ marginTop: '15px' }}>
              <table className="table">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Producto ID</th>
                    <th>Tipo</th>
                    <th>Cantidad</th>
                    <th>Fecha</th>
                  </tr>
                </thead>
                <tbody>
                  {movimientosProducto.map((mov) => (
                    <tr key={mov.id}>
                      <td>{mov.id}</td>
                      <td>{mov.producto_id}</td>
                      <td>{mov.tipo}</td>
                      <td>{mov.cantidad}</td>
                      <td>{mov.fecha}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}

      {showBuscarId && (
        <div className="form">
          <h3>Buscar Movimiento por ID</h3>
          <div className="form-group">
            <label>ID Movimiento:</label>
            <input type="number" value={buscarMovimientoId} onChange={(e) => setBuscarMovimientoId(e.target.value)} placeholder="Ingresa el ID del movimiento" />
          </div>
          <button className="btn-primary" onClick={handleBuscarMovimientoPorId}>Buscar</button>

          {detalleMovimiento && detalleMovimiento.id && (
            <div className="perfil-info" style={{ marginTop: '15px' }}>
              <h4>Detalles del Movimiento</h4>
              <p><strong>ID:</strong> {detalleMovimiento.id}</p>
              <p><strong>Producto ID:</strong> {detalleMovimiento.producto_id}</p>
              <p><strong>Usuario ID:</strong> {detalleMovimiento.id_usuario}</p>
              <p><strong>Tipo:</strong> {detalleMovimiento.tipo}</p>
              <p><strong>Cantidad:</strong> {detalleMovimiento.cantidad}</p>
              <p><strong>Fecha:</strong> {detalleMovimiento.fecha}</p>
            </div>
          )}

          {noEncontrado && (
            <div className="error" style={{ marginTop: '15px', backgroundColor: '#ffebee', color: '#c62828', padding: '10px', borderRadius: '4px' }}>
              ⚠️ El movimiento con ID <strong>{buscarMovimientoId}</strong> no existe en el sistema.
            </div>
          )}
        </div>
      )}

      <h3 style={{ marginTop: '25px' }}>Historial de Movimientos</h3>
      {movimientos.length === 0 ? (
        <p>No hay movimientos registrados</p>
      ) : (
        <div className="table-container">
          <table className="table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Producto ID</th>
                <th>Usuario ID</th>
                <th>Tipo</th>
                <th>Cantidad</th>
                <th>Fecha</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              {movimientos.map((mov) => (
                <tr key={mov.id}>
                  <td>{mov.id}</td>
                  <td>{mov.producto_id}</td>
                  <td>{mov.id_usuario}</td>
                  <td>
                    <span className={mov.tipo === "entrada" ? "badge-success" : "badge-danger"}>
                      {mov.tipo}
                    </span>
                  </td>
                  <td>{mov.cantidad}</td>
                  <td>{mov.fecha}</td>
                  <td>
                    <button className="btn-danger" onClick={() => handleEliminarMovimiento(mov.id)}>Eliminar</button>
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