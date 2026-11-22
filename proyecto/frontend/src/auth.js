export const SESSION_KEY = "stockmind_usuario";

export const guardarSesion = (usuario) => {
  sessionStorage.setItem(SESSION_KEY, JSON.stringify(usuario));
};

export const obtenerSesion = () => {
  try {
    return JSON.parse(sessionStorage.getItem(SESSION_KEY));
  } catch {
    return null;
  }
};

export const cerrarSesion = () => {
  sessionStorage.removeItem(SESSION_KEY);
};

export const esAdministrador = () => {
  const usuario = obtenerSesion();
  return usuario?.rol?.toLowerCase() === "administrador";
};
