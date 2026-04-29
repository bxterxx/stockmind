import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';

// Estos son componentes "dummy" para que no de error por falta de definición
const Dashboard = () => (
  <div className="card">
    <h2> Panel de Control</h2>
    <p>Bienvenido al sistema StockMind.</p>
  </div>
);
const Proveedores = () => (
  <div className="card">
    <h2> Registro de Proveedores</h2>
    <p>Administra los proveedores de tu inventario.</p>
  </div>
);

const Productos = () => (
  <div className="card">
    <h2> Gestión de Productos</h2>
    <p>Aquí verás tu tabla de inventario próximamente.</p>
  </div>
);

const Usuarios = () => (
  <div className="card">
    <h2> Registro de Usuarios</h2>
    <p>Administra quién tiene acceso al sistema.</p>
  </div>
);


function App() {
  return (
    <Router>
      <div className="main-layout">
        <div className="container">
          <nav className="navbar">
      <div className="logo">StockMind</div>
      <div className="nav-links">
        <Link to="/" className="btn-nav">Inicio</Link>
        <Link to="/productos" className="btn-nav">Productos</Link>
        <Link to="/usuarios" className="btn-nav">Usuarios</Link>
        <Link to="/proveedores" className="btn-nav">Proveedores</Link>
      </div>
    </nav>
          <div className="card">
            <h3> Bienvenido a StockMind</h3>
            <p>Tu sistema de gestión de inventarios inteligente.</p>
          </div>
        </div>
      </div>
        <div className="container">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/productos" element={<Productos />} />
            <Route path="/usuarios" element={<Usuarios />} />
            <Route path="/proveedores" element={<Proveedores />} />
          </Routes>
        </div>
    </Router>
  );
}

export default App;