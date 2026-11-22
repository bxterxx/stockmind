import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom';
import './App.css';
import { Dashboard } from './components/Dashboard';
import { Productos } from './components/Productos';
import { Usuarios } from './components/Usuarios';
import { Proveedores } from './components/Proveedores';
import { Categorias } from './components/Categorias';
import { Movimientos } from './components/Movimientos';
import { Login } from './components/Login';
import { obtenerSesion, cerrarSesion } from './auth';

function App() {
  const [usuario, setUsuario] = useState(obtenerSesion());
  const administrador = usuario?.rol?.toLowerCase() === 'administrador';

  const salir = () => {
    cerrarSesion();
    setUsuario(null);
  };

  if (!usuario) {
    return <Login onLogin={setUsuario} />;
  }

  return (
    <Router>
      <div className="main-layout">
        <nav className="navbar">
          <div className="logo">📊 StockMind</div>
          <div className="nav-links">
            <Link to="/" className="btn-nav">Inicio</Link>
            <Link to="/productos" className="btn-nav">Productos</Link>
            <Link to="/categorias" className="btn-nav">Categorías</Link>
            <Link to="/proveedores" className="btn-nav">Proveedores</Link>
            <Link to="/movimientos" className="btn-nav">Movimientos</Link>
            {administrador && <Link to="/usuarios" className="btn-nav">Usuarios</Link>}
            <span className="usuario-nav">{usuario.nombre_completo}<br/><small>{administrador ? 'Administrador' : 'Usuario'}</small></span>
            <button className="btn-nav btn-salir" onClick={salir}>Cerrar sesión</button>
          </div>
        </nav>

        <div className="container">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/productos" element={<Productos />} />
            <Route path="/categorias" element={<Categorias />} />
            <Route path="/proveedores" element={<Proveedores />} />
            <Route path="/movimientos" element={<Movimientos />} />
            {administrador && <Route path="/usuarios" element={<Usuarios />} />}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;