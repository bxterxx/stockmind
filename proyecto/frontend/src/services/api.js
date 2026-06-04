const API_URL = "http://localhost:8000";

// Productos
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
    const response = await fetch(`${API_URL}/productos/${id}`, {
      method: "DELETE",
    });
    if (!response.ok) throw new Error("Error al eliminar producto");
    return response.json();
  },
};

// Usuarios
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
};

// Categorías
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
    const response = await fetch(`${API_URL}/categorias/${id}`, {
      method: "DELETE",
    });
    if (!response.ok) throw new Error("Error al eliminar categoría");
    return response.json();
  },
};

// Proveedores
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
    const response = await fetch(`${API_URL}/proveedores/${id}`, {
      method: "DELETE",
    });
    if (!response.ok) throw new Error("Error al eliminar proveedor");
    return response.json();
  },
};

// Movimientos
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
    const response = await fetch(`${API_URL}/movimientos/${id}`, {
      method: "DELETE",
    });
    if (!response.ok) throw new Error("Error al eliminar movimiento");
    return response.json();
  },
};
