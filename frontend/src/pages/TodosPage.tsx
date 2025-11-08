import React, { useState } from 'react'
import { useTodos } from '../hooks/useTodos'
import { Todo } from '../types'
import TodoItem from '../components/TodoItem'

export default function TodosPage() {
  const { todos, loading, addTodo, deleteTodo, refetch } = useTodos()
  const [title, setTitle] = useState('')

  async function handleAdd(e: React.FormEvent) {
    e.preventDefault()
    if (!title.trim()) return
    await addTodo(title.trim())
    setTitle('')
    refetch()
  }

  return (
    <div className="todos-page">
      <form onSubmit={handleAdd} className="todo-form">
        <input
          value={title}
          onChange={e => setTitle(e.target.value)}
          placeholder="Add todo"
        />
        <button type="submit">Add</button>
      </form>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <ul className="todo-list">
          {todos.map(t => (
            <TodoItem key={t.id} todo={t} onDelete={async () => { await deleteTodo(t.id); refetch(); }} />
          ))}
        </ul>
      )}
    </div>
  )
}
