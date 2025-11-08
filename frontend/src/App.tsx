import React from 'react'
import TodosPage from './pages/TodosPage'

export default function App() {
  return (
    <div className="app-root">
      <header className="header">
        <h1>Todo List</h1>
      </header>
      <main>
        <TodosPage />
      </main>
    </div>
  )
}
