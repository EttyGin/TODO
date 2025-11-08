import { useEffect, useState, useCallback } from 'react'
import * as api from '../services/api'
import { Todo } from '../types'

export function useTodos() {
  const [todos, setTodos] = useState<Todo[]>([])
  const [loading, setLoading] = useState(true)

  const fetch = useCallback(async () => {
    setLoading(true)
    try {
      const data = await api.fetchTodos()
      setTodos(data)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetch()
  }, [fetch])

  const addTodo = async (title: string) => {
    await api.createTodo({ title })
  }

  const deleteTodo = async (id: number) => {
    await api.deleteTodo(id)
  }

  return { todos, loading, addTodo, deleteTodo, refetch: fetch }
}
