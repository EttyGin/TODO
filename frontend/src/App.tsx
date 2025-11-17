import { Container, Title, Box, Alert, Loader, Center } from '@mantine/core'
import { TodoForm, TodoList } from './components'
import { useTodos } from './hooks'

function App() {
  const { todos, loading, error, addTodo, toggleTodo, deleteTodo, editTodo } = useTodos()

  return (
    <Box
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: '100vh',
        backgroundColor: '#f5f5f5'
      }}
    >
      <Container size="sm" w="100%" maw={600}>
        <Title order={1} ta="center" mb={30}>
          📝 My Todo List
        </Title>

        {error && (
          <Alert color="red" mb={20}>
            {error}
          </Alert>
        )}
        
        <TodoForm onAdd={addTodo} />

        {loading ? (
          <Center py={40}>
            <Loader size="lg" />
          </Center>
        ) : (
          <TodoList
            todos={todos}
            onToggle={toggleTodo}
            onDelete={deleteTodo}
            onEdit={editTodo}
          />
        )}
      </Container>
    </Box>
  )
}

export default App