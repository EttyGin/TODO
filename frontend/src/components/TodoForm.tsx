import { TextInput, Button, Group, Paper } from '@mantine/core'
import { IconPlus } from '@tabler/icons-react'
import { useState } from 'react'

interface TodoFormProps {
  onAdd: (title: string) => void
}

export function TodoForm({ onAdd }: TodoFormProps) {
  const [value, setValue] = useState('')

  const handleSubmit = () => {
    if (value.trim()) {
      onAdd(value)
      setValue('')
    }
  }

  return (
    <Paper shadow="sm" p="lg" radius="md" withBorder mb={20}>
      <Group gap="xs">
        <TextInput
          placeholder="What needs to be done?"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyUp={(e) => e.key === 'Enter' && handleSubmit()}
          style={{ flex: 1 }}
          size="md"
        />
        <Button 
          onClick={handleSubmit}
          leftSection={<IconPlus size={18} />}
          size="md"
        >
          Add
        </Button>
      </Group>
    </Paper>
  )
}