import { useState, useEffect } from 'react'
import type { Todo } from '../types'
import { todoApi } from '../services'

export function useTodos() {
  const [todos, setTodos] = useState<Todo[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  // טעינת המשימות בפעם הראשונה
  useEffect(() => {
    loadTodos()
  }, [])

  const loadTodos = async () => {
    try {
      setLoading(true)
      setError(null)
      const data = await todoApi.getAll()
      setTodos(data)
    } catch (err) {
      setError('Failed to load todos')
      console.error('Error loading todos:', err)
    } finally {
      setLoading(false)
    }
  }

  const addTodo = async (title: string) => {
    try {
      setError(null)
      const newTodo = await todoApi.create({ title, completed: false })
      setTodos([newTodo, ...todos])
    } catch (err) {
      setError('Failed to add todo')
      console.error('Error adding todo:', err)
    }
  }

  const toggleTodo = async (id: number) => {
    try {
      setError(null)
      const todo = todos.find(t => t.id === id)
      if (!todo) return

      const updated = await todoApi.update(id, {
        title: todo.title,
        completed: !todo.completed
      })

      setTodos(todos.map(t => t.id === id ? updated : t))
    } catch (err) {
      setError('Failed to toggle todo')
      console.error('Error toggling todo:', err)
    }
  }

  const deleteTodo = async (id: number) => {
    try {
      setError(null)
      await todoApi.delete(id)
      setTodos(todos.filter(t => t.id !== id))
    } catch (err) {
      setError('Failed to delete todo')
      console.error('Error deleting todo:', err)
    }
  }

  const editTodo = async (id: number, newTitle: string) => {
    try {
      setError(null)
      const todo = todos.find(t => t.id === id)
      if (!todo) return

      const updated = await todoApi.update(id, {
        title: newTitle,
        completed: todo.completed
      })

      setTodos(todos.map(t => t.id === id ? updated : t))
    } catch (err) {
      setError('Failed to edit todo')
      console.error('Error editing todo:', err)
    }
  }

  return {
    todos,
    loading,
    error,
    addTodo,
    toggleTodo,
    deleteTodo,
    editTodo,
    refreshTodos: loadTodos
  }
}