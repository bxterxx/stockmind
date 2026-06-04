import React, { useState, useEffect } from "react";
import { productosAPI, categoriasAPI, proveedoresAPI } from "../services/api";
import "../styles/Componentes.css";

export const Productos = () => {
  const [productos, setProductos] = useState([]);
  const [categorias, setCategorias] = useState([]);
  const [proveedores, setProveedores] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [showBuscar, setShowBuscar] = useState(false);
  const [detalleProducto, setDetalleProducto] = useState(null);
  const [buscarId, setBuscarId] = useState("");
  const [formData, setFormData] = useState({
    id_producto: "",
    nombre: "",
    precio_venta: "",
    stock_actual: "",
    stock_minimo: "",
    descripcion: "",
    categoria_id: "",
    proveedor_id: "",
  });

  useEffect(() => {
    cargarDatos();
  }, []);

  const cargarDatos = async () => {
    try {
      setLoading(true);
      const [productosData, categoriasData, proveedoresData] = await Promise.all([
        productosAPI.obtenerTodos(),
        categoriasAPI.obtenerTodas(),
        proveedoresAPI.listar(),
      ]);
      setProductos(productosData);
      setCategorias(categoriasData);
      setProveedores(proveedoresData);
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
      await productosAPI.crear({
        id_producto: parseInt(formData.id_producto),
        nombre: formData.nombre,
        precio_venta: parseFloat(formData.precio_venta),
        stock_actual: parseInt(formData.stock_actual),
        stock_minimo: parseInt(formData.stock_minimo),
        descripcion: formData.descripcion,
        categoria_id: parseInt(formData.categoria_id),
        proveedor_id: parseInt(formData.proveedor_id),
      });
      setFormData({
        id_producto: "",
        nombre: "",
        precio_venta: "",
        stock_actual: "",
        stock_minimo: "",
        descripcion: "",
        categoria_id: "",
        proveedor_id: "",
      });
      setShowForm(false);
      cargarDatos();
    } catch (err) {
      setError(err.message);
    }
  };

  const handleEliminar = async (id) => {
    if (window.confirm("¿Estás seguro de que deseas eliminar este producto?")) {
      try {
        await productosAPI.eliminar(id);
        cargarDatos();
      } catch (err) {
        setError(err.message);
      }
    }
  };

  const handleBuscarPorId = async () => {
    if (!buscarId) {
      setError("Ingresa un ID de producto");
      return;
    }
    try {
      const producto = await productosAPI.obtenerPorId(parseInt(buscarId));
      setDetalleProducto(producto);
    } catch (err) {
      setError(err.message);
      setDetalleProducto(null);
    }
  };

  if (loading) return <div className="card"><p>Cargando productos...</p></div>;

  return (
    <div className="card">
      <h2>📦 Gestión de Productos</h2>
      {error && <div className="error">{error}</div>}
      
      <button className="btn-primary" onClick={() => setShowForm(!showForm)}>
        {showForm ? "Cancelar" : "+ Nuevo Producto"}
      </button>

      <button className="btn-secondary" onClick={() => setShowBuscar(!showBuscar)}>
        {showBuscar ? "Cancelar" : "🔍 Ver Detalles"}
      </button>

      {showForm && (
        <form onSubmit={handleSubmit} className="form">
          <div className="form-group">
            <label>ID Producto:</label>
            <input type="number" name="id_producto" value={formData.id_producto} onChange={handleInputChange} required />
          </div>
          <div className="form-group">
            <label>Nombre:</label>
            <input type="text" name="nombre" value={formData.nombre} onChange={handleInputChange} required />
          </div>
          <div className="form-group">
            <label>Precio Venta:</label>
            <input type="number" step="0.01" name="precio_venta" value={formData.precio_venta} onChange={handleInputChange} required />
          </div>
          <div className="form-group">
            <label>Stock Actual:</label>
            <input type="number" name="stock_actual" value={formData.stock_actual} onChange={handleInputChange} required />
          </div>
          <div className="form-group">
            <label>Stock Mínimo:</label>
            <input type="number" name="stock_minimo" value={formData.stock_minimo} onChange={handleInputChange} required />
          </div>
          <div className="form-group">
            <label>Descripción:</label>
            <textarea name="descripcion" value={formData.descripcion} onChange={handleInputChange} required></textarea>
          </div>
          <div className="form-group">
            <label>Categoría:</label>
            <select name="categoria_id" value={formData.categoria_id} onChange={handleInputChange} required>
              <option value="">Selecciona una categoría</option>
              {categorias.map((cat) => (
                <option key={cat.id} value={cat.id}>{cat.nombre}</option>
              ))}
            </select>
          </div>
          <div className="form-group">
            <label>Proveedor:</label>
            <select name="proveedor_id" value={formData.proveedor_id} onChange={handleInputChange} required>
              <option value="">Selecciona un proveedor</option>
              {proveedores.map((prov) => (
                <option key={prov.id} value={prov.id}>{prov.nombre_empresa}</option>
              ))}
            </select>
          </div>
          <button type="submit" className="btn-success">Guardar Producto</button>
        </form>
      )}

      {showBuscar && (
        <div className="form">
          <h3>Buscar Producto por ID</h3>
          <div className="form-group">
            <label>ID Producto:</label>
            <input
              type="number"
              value={buscarId}
              onChange={(e) => setBuscarId(e.target.value)}
              placeholder="Ingresa el ID del producto"
            />
          </div>
          <button className="btn-primary" onClick={handleBuscarPorId}>
            Buscar
          </button>

          {detalleProducto && (
            <div className="perfil-info">
              <h4>Detalles del Producto</h4>
              <p><strong>ID:</strong> {detalleProducto.id}</p>
              <p><strong>Nombre:</strong> {detalleProducto.nombre}</p>
              <p><strong>Precio:</strong> ${detalleProducto.precio_venta}</p>
              <p><strong>Stock Actual:</strong> {detalleProducto.stock_actual}</p>
              <p><strong>Stock Mínimo:</strong> {detalleProducto.stock_minimo}</p>
              <p><strong>Descripción:</strong> {detalleProducto.descripcion}</p>
              <p><strong>Categoría ID:</strong> {detalleProducto.categoria_id}</p>
              <p><strong>Proveedor ID:</strong> {detalleProducto.proveedor_id}</p>
            </div>
          )}
        </div>
      )}

      {productos.length === 0 ? (
        <p>No hay productos registrados</p>
      ) : (
        <div className="table-container">
          <table className="table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Precio</th>
                <th>Stock</th>
                <th>Mín.</th>
                <th>Descripción</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              {productos.map((prod) => (
                <tr key={prod.id}>
                  <td>{prod.id}</td>
                  <td>{prod.nombre}</td>
                  <td>${prod.precio_venta}</td>
                  <td>{prod.stock_actual}</td>
                  <td>{prod.stock_minimo}</td>
                  <td>{prod.descripcion}</td>
                  <td>
                    <button className="btn-danger" onClick={() => handleEliminar(prod.id)}>
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
