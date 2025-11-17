import axios from 'axios'
import { API_CONFIG } from '../config/api'
import type { Todo } from '../types'

const api = axios.create({
  baseURL: API_CONFIG.baseURL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const todoApi = {
    getAll: async (): Promise<Todo[]> => {
    const response = await api.get(API_CONFIG.endpoints.todos)
    return response.data
  },

  getById: async (id: number): Promise<Todo> => {
    const response = await api.get(`${API_CONFIG.endpoints.todos}/${id}`)
    return response.data
  },

  create: async (todo: Omit<Todo, 'id'>): Promise<Todo> => {
    const response = await api.post(API_CONFIG.endpoints.todos, todo)
    return response.data
  },

  update: async (id: number, todo: Omit<Todo, 'id'>): Promise<Todo> => {
    const response = await api.put(`${API_CONFIG.endpoints.todos}/${id}`, todo)
    return response.data
  },

  delete: async (id: number): Promise<void> => {
    await api.delete(`${API_CONFIG.endpoints.todos}/${id}`)
  },
}