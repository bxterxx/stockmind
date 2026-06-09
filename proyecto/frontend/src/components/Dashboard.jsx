import React, { useState, useEffect } from "react";
import { productosAPI, categoriasAPI, proveedoresAPI, movimientosAPI } from "../services/api";
import "../styles/Dashboard.css";

export const Dashboard = () => {
  const [stats, setStats] = useState({
    productos: 0,
    categorias: 0,
    proveedores: 0,
    movimientos: 0,
  });
  // 1. Nuevo estado para guardar los productos con bajo stock
  const [alertasStock, setAlertasStock] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    cargarEstadisticas();
  }, []);

  const cargarEstadisticas = async () => {
    try {
      setLoading(true);
      const [productosData, categoriasData, proveedoresData, movimientosData] = await Promise.all([
        productosAPI.obtenerTodos(),
        categoriasAPI.obtenerTodas(),
        proveedoresAPI.listar(),
        movimientosAPI.listar(),
      ]);

      setStats({
        productos: productosData.length,
        categorias: categoriasData.length,
        proveedores: proveedoresData.length,
        movimientos: movimientosData.length,
      });

      // 2. Lógica para filtrar los productos con stock por debajo del mínimo
      const productosBajoStock = productosData.filter(
        (prod) => parseInt(prod.stock_actual) < parseInt(prod.stock_minimo)
      );
      setAlertasStock(productosBajoStock); // Guardamos las alertas

      setError(null);
    } catch (err) {
      setError("Error al cargar el resumen de estadísticas.");
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="card"><p>Cargando estadísticas...</p></div>;

  return (
    <div className="dashboard">
      <h1 style={{ 
        fontSize: '2.5rem', 
        marginBottom: '20px', 
        fontWeight: 'bold', 
        textAlign: 'center', 
        color: 'white' 
      }}>
        📊 Panel de Control
      </h1>
      
      {error && <div className="error">{error}</div>}

      {/* 3. Notificación de Stock Bajo (Solo aparece si hay alertas) */}
      {alertasStock.length > 0 && (
        <div style={{ 
          backgroundColor: '#ff9800', 
          color: 'white', 
          padding: '15px 20px', 
          borderRadius: '8px', 
          marginBottom: '25px',
          boxShadow: '0 4px 6px rgba(0,0,0,0.1)'
        }}>
          <h3 style={{ margin: '0 0 10px 0', display: 'flex', alignItems: 'center', gap: '8px' }}>
            ⚠️ Alerta: Productos con stock bajo
          </h3>
          <ul style={{ margin: 0, paddingLeft: '20px' }}>
            {alertasStock.map((prod) => (
              <li key={prod.id || prod.id_producto} style={{ marginBottom: '5px' }}>
                <strong>{prod.nombre}</strong> - Stock actual: <strong>{prod.stock_actual}</strong> (Mínimo requerido: {prod.stock_minimo})
              </li>
            ))}
          </ul>
        </div>
      )}
      
      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-icon">📦</div>
          <div className="stat-content">
            <h3>Productos</h3>
            <p className="stat-number">{stats.productos}</p>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon">🏷️</div>
          <div className="stat-content">
            <h3>Categorías</h3>
            <p className="stat-number">{stats.categorias}</p>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon">🏢</div>
          <div className="stat-content">
            <h3>Proveedores</h3>
            <p className="stat-number">{stats.proveedores}</p>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon">📊</div>
          <div className="stat-content">
            <h3>Movimientos</h3>
            <p className="stat-number">{stats.movimientos}</p>
          </div>
        </div>
      </div>

      <div className="welcome-info">
        <h3>¡Bienvenido a StockMind!</h3>
        <p>Tu sistema de gestión de inventarios inteligente y funcional.</p>
        <ul>
          <li>Gestiona productos con categorías y proveedores</li>
          <li>Registra movimientos de entrada y salida</li>
          <li>Administra usuarios del sistema</li>
          <li>Controla tu inventario en tiempo real</li>
        </ul>
      </div>
    </div>
  );
}