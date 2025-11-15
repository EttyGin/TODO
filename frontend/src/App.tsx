import { Container, Title } from '@mantine/core'
import { useState } from 'react'
import { TodoForm } from './components/TodoForm'
import { TodoList } from './components/TodoList'
import type { Todo } from './types'

function App() {
  const [todos, setTodos] = useState<Todo[]>([])

    const handleAddTodo = (title: string) => {
        const newTodo: Todo = {
              id: Date.now(), // ID זמני (בעתיד יבוא מהשרת)
                    title,
                          completed: false
                              }
                                  setTodos([newTodo, ...todos])
                                    }

                                      const handleToggleTodo = (id: number) => {
                                          setTodos(todos.map(todo =>
                                                todo.id === id ? { ...todo, completed: !todo.completed } : todo
                                                    ))
                                                      }

                                                        const handleDeleteTodo = (id: number) => {
                                                            setTodos(todos.filter(todo => todo.id !== id))
                                                              }

                                                                const handleEditTodo = (id: number, newTitle: string) => {
                                                                    setTodos(todos.map(todo =>
                                                                          todo.id === id ? { ...todo, title: newTitle } : todo
                                                                              ))
                                                                                }

                                                                                  return (
                                                                                      <Container size="sm" py={40}>
                                                                                            <Title order={1} ta="center" mb={30}>
                                                                                                    📝 My Todo List
                                                                                                          </Title>
                                                                                                                
                                                                                                                      <TodoForm onAdd={handleAddTodo} />
                                                                                                                            <TodoList
                                                                                                                                    todos={todos}
                                                                                                                                            onToggle={handleToggleTodo}
                                                                                                                                                    onDelete={handleDeleteTodo}
                                                                                                                                                            onEdit={handleEditTodo}
                                                                                                                                                                  />
                                                                                                                                                                      </Container>
                                                                                                                                                                        )
                                                                                                                                                                        }

                                                                                                                                                                        export default App