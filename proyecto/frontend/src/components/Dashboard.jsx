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
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="card"><p>Cargando estadísticas...</p></div>;

  return (
    <div className="dashboard">
      <h2>📊 Panel de Control</h2>
      {error && <div className="error">{error}</div>}
      
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
};
