import axios from 'axios'
import { TodoCreateDTO, TodoDTO } from '../types'

const api = axios.create({
  baseURL: 'http://localhost:8000/todos',
  headers: { 'Content-Type': 'application/json' },
})

export const fetchTodos = async (): Promise<TodoDTO[]> => {
  const res = await api.get('/')
  return res.data
}

export const createTodo = async (payload: TodoCreateDTO): Promise<TodoDTO> => {
  const res = await api.post('/', payload)
  return res.data
}

export const deleteTodo = async (id: number): Promise<void> => {
  await api.delete(`/${id}`)
}

export default api
