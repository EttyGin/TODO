import { Stack, Text } from '@mantine/core'
import type { Todo } from '../types/todo'
import { TodoItem } from './TodoItem'

interface TodoListProps {
  todos: Todo[]
  onToggle: (id: number) => void
  onDelete: (id: number) => void
  onEdit: (id: number, newTitle: string) => void
}

export function TodoList({ todos, onToggle, onDelete, onEdit }: TodoListProps) {
  console.log('TodoList received todos:', todos, 'Type:', typeof todos)
  
  if (!todos || !Array.isArray(todos)) {
    console.error('todos is not an array:', todos)
    return (
      <Text ta="center" c="red" py={40}>
        Error: Invalid data format
      </Text>
    )
  }

  if (todos.length === 0) {
    return (
      <Text ta="center" c="dimmed" py={40}>
        No tasks yet. Add one above!
      </Text>
    )
  }

  return (
    <Stack gap="sm">
      {todos.map(todo => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onToggle={onToggle}
          onDelete={onDelete}
          onEdit={onEdit}
        />
      ))}
    </Stack>
  )
}