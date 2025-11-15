import { Paper, Group, Checkbox, TextInput, ActionIcon, Text } from '@mantine/core'
import { IconEdit, IconTrash, IconCheck, IconX } from '@tabler/icons-react'
import { useState } from 'react'
import type { Todo } from '../types/todo'

interface TodoItemProps {
  todo: Todo
  onToggle: (id: number) => void
  onDelete: (id: number) => void
  onEdit: (id: number, newTitle: string) => void
}

export function TodoItem({ todo, onToggle, onDelete, onEdit }: TodoItemProps) {
  const [isEditing, setIsEditing] = useState(false)
  const [editValue, setEditValue] = useState(todo.title)

  const handleSave = () => {
    if (editValue.trim()) {
      onEdit(todo.id, editValue)
      setIsEditing(false)
    }
  }

  const handleCancel = () => {
    setEditValue(todo.title)
    setIsEditing(false)
  }

  return (
    <Paper shadow="xs" p="md" radius="md" withBorder mb={10}>
      <Group justify="space-between">
        <Group style={{ flex: 1 }}>
          <Checkbox
            checked={todo.completed}
            onChange={() => onToggle(todo.id)}
            size="md"
          />
          
          {isEditing ? (
            <TextInput
              value={editValue}
              onChange={(e) => setEditValue(e.target.value)}
              onKeyUp={(e) => e.key === 'Enter' && handleSave()}
              style={{ flex: 1 }}
              autoFocus
            />
          ) : (
            <Text
              style={{
                textDecoration: todo.completed ? 'line-through' : 'none',
                color: todo.completed ? '#999' : '#000',
                flex: 1
              }}
            >
              {todo.title}
            </Text>
          )}
        </Group>

        <Group gap={5}>
          {isEditing ? (
            <>
              <ActionIcon color="green" onClick={handleSave} variant="light">
                <IconCheck size={18} />
              </ActionIcon>
              <ActionIcon color="gray" onClick={handleCancel} variant="light">
                <IconX size={18} />
              </ActionIcon>
            </>
          ) : (
            <>
              <ActionIcon color="blue" onClick={() => setIsEditing(true)} variant="light">
                <IconEdit size={18} />
              </ActionIcon>
              <ActionIcon color="red" onClick={() => onDelete(todo.id)} variant="light">
                <IconTrash size={18} />
              </ActionIcon>
            </>
          )}
        </Group>
      </Group>
    </Paper>
  )
}