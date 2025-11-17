export const API_CONFIG = {
  baseURL: import.meta.env.VITE_BACKEND_API_URL || "http://127.0.0.1:8000",
  endpoints: {
    todos: '/todos',
  }
}