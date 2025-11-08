import React from 'react'
import { Todo } from '../types'

type Props = {
  todo: Todo
  onDelete: () => void
}

export default function TodoItem({ todo, onDelete }: Props) {
  return (
    <li className="todo-item">
      <span>{todo.title}</span>
      <button className="delete-btn" onClick={onDelete}>Delete</button>
    </li>
  )
}
