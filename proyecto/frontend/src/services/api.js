const API_URL = "http://localhost:8000";

// ==========================================
// 👥 USUARIOS
// ==========================================
export const usuariosAPI = {
  registrar: async (datos) => {
    const params = new URLSearchParams({
      id_usuario: datos.id_usuario,
      nombre_completo: datos.nombre_completo,
      username: datos.username,
      password: datos.password,
      rol: datos.rol,
    });
    const response = await fetch(`${API_URL}/usuarios/registro?${params}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    });
    if (!response.ok) throw new Error("Error al registrar usuario");
    return response.json();
  },
  
  verPerfil: async (id) => {
    const response = await fetch(`${API_URL}/usuarios/${id}`);
    if (!response.ok) throw new Error("Usuario no encontrado");
    return response.json();
  },

  listar: async () => {
    // Apunta exactamente a @router.get("/") con el prefijo /usuarios
    const response = await fetch(`${API_URL}/usuarios/`);
    if (!response.ok) throw new Error("Error al obtener usuarios");
    return response.json();
  },

  eliminar: async (id) => {
    try {
      // ✅ CORREGIDO: Envía el ID directo en la URL para cumplir con @router.delete("/{id_usuario}")
      const response = await fetch(`${API_URL}/usuarios/${id}`, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" }
      });
      
      if (!response.ok) throw new Error("Error al eliminar usuario");
      
      // Manejo seguro por si el backend responde con contenido vacío (204 No Content)
      if (response.status === 204) return { success: true };
      return response.json();
    } catch (err) {
      throw new Error("RESTRICT_IN_USE");
    }
  },
};

// ==========================================
// 📦 PRODUCTOS
// ==========================================
export const productosAPI = {
  obtenerTodos: async () => {
    const response = await fetch(`${API_URL}/productos/`);
    if (!response.ok) throw new Error("Error al obtener productos");
    return response.json();
  },
  
  obtenerPorId: async (id) => {
    const response = await fetch(`${API_URL}/productos/${id}`);
    if (!response.ok) throw new Error("Producto no encontrado");
    return response.json();
  },
  
  crear: async (datos) => {
    const response = await fetch(`${API_URL}/productos/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(datos),
    });
    if (!response.ok) throw new Error("Error al crear producto");
    return response.json();
  },
  
  eliminar: async (id) => {
    try {
      const response = await fetch(`${API_URL}/productos/${id}`, {
        method: "DELETE",
      });
      if (!response.ok) throw new Error("Error al eliminar producto");
      return response.json();
    } catch (err) {
      throw new Error("RESTRICT_IN_USE");
    }
  },
};

// ==========================================
// 🏷️ CATEGORÍAS
// ==========================================
export const categoriasAPI = {
  obtenerTodas: async () => {
    const response = await fetch(`${API_URL}/categorias/`);
    if (!response.ok) throw new Error("Error al obtener categorías");
    return response.json();
  },
  
  obtenerPorId: async (id) => {
    const response = await fetch(`${API_URL}/categorias/${id}`);
    if (!response.ok) throw new Error("Categoría no encontrada");
    return response.json();
  },
  
  crear: async (datos) => {
    const params = new URLSearchParams({
      id: datos.id,
      nombre: datos.nombre,
    });
    const response = await fetch(`${API_URL}/categorias/?${params}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    });
    if (!response.ok) throw new Error("Error al crear categoría");
    return response.json();
  },
  
  eliminar: async (id) => {
    try {
      const response = await fetch(`${API_URL}/categorias/${id}`, {
        method: "DELETE",
      });
      if (!response.ok) throw new Error("RESTRICT_IN_USE");
      
      if (response.status === 204) return { success: true };
      return response.json();
    } catch (err) {
      throw new Error("RESTRICT_IN_USE");
    }
  },
};

// ==========================================
// 🏢 PROVEEDORES
// ==========================================
export const proveedoresAPI = {
  listar: async () => {
    const response = await fetch(`${API_URL}/proveedores/`);
    if (!response.ok) throw new Error("Error al obtener proveedores");
    return response.json();
  },
  
  crear: async (datos) => {
    const params = new URLSearchParams({
      id: datos.id,
      nombre_empresa: datos.nombre_empresa,
      telefono: datos.telefono,
    });
    const response = await fetch(`${API_URL}/proveedores/?${params}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    });
    if (!response.ok) throw new Error("Error al crear proveedor");
    return response.json();
  },
  
  eliminar: async (id) => {
    try {
      const response = await fetch(`${API_URL}/proveedores/${id}`, {
        method: "DELETE",
      });
      if (!response.ok) throw new Error("RESTRICT_IN_USE");
      
      if (response.status === 204) return { success: true };
      return response.json();
    } catch (err) {
      throw new Error("RESTRICT_IN_USE");
    }
  },
};

// ==========================================
// 📊 MOVIMIENTOS
// ==========================================
export const movimientosAPI = {
  crear: async (datos) => {
    const params = new URLSearchParams({
      id: datos.id,
      Producto: datos.Producto,
      Usuario: datos.Usuario,
      tipo: datos.tipo,
      cantidad: datos.cantidad,
      fecha: datos.fecha,
    });
    const response = await fetch(`${API_URL}/movimientos/?${params}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    });
    if (!response.ok) throw new Error("Error al crear movimiento");
    return response.json();
  },
  
  listar: async () => {
    const response = await fetch(`${API_URL}/movimientos/`);
    if (!response.ok) throw new Error("Error al obtener movimientos");
    return response.json();
  },
  
  obtenerPorProducto: async (productoId) => {
    const response = await fetch(`${API_URL}/movimientos/producto/${productoId}`);
    if (!response.ok) throw new Error("Error al obtener movimientos del producto");
    return response.json();
  },
  
  obtenerPorId: async (id) => {
    const response = await fetch(`${API_URL}/movimientos/${id}`);
    if (!response.ok) throw new Error("Movimiento no encontrado");
    return response.json();
  },
  
  eliminar: async (id) => {
    try {
      const response = await fetch(`${API_URL}/movimientos/${id}`, {
        method: "DELETE",
      });
      if (!response.ok) throw new Error("Error al eliminar movimiento");
      return response.json();
    } catch (err) {
      throw new Error("RESTRICT_IN_USE");
    }
  },
}