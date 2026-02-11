'use client';

import { useState, useEffect } from 'react';
import { todoApi } from '../api/todos';
import { Todo } from '../api/todos';
import TodoStatusToggle from '@/components/ui/TodoStatusToggle';

export default function DashboardPage() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [newTodo, setNewTodo] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    try {
      setLoading(true);
      const todosData = await todoApi.getTodos();
      setTodos(todosData);
    } catch (err) {
      setError('Failed to load todos');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleAddTodo = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!newTodo.trim()) return;

    try {
      const createdTodo = await todoApi.createTodo({
        title: newTodo.trim(),
        is_completed: false
      });
      setTodos([createdTodo, ...todos]);
      setNewTodo('');
    } catch (err) {
      setError('Failed to add todo');
      console.error(err);
    }
  };

  const toggleTodoCompletion = async (todo: Todo) => {
    try {
      const updatedTodo = await todoApi.toggleTodoCompletion(todo.id, !todo.is_completed);
      setTodos(todos.map(t => t.id === updatedTodo.id ? updatedTodo : t));
    } catch (err) {
      setError('Failed to update todo');
      console.error(err);
    }
  };

  const deleteTodo = async (id: string) => {
    try {
      await todoApi.deleteTodo(id);
      setTodos(todos.filter(todo => todo.id !== id));
    } catch (err) {
      setError('Failed to delete todo');
      console.error(err);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <p>Loading todos...</p>
      </div>
    );
  }

  return (
    <div>
      <div className="md:flex md:items-center md:justify-between mb-6">
        <div className="flex-1 min-w-0">
          <h1 className="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl sm:truncate">
            My Todos
          </h1>
        </div>
      </div>

      {error && (
        <div className="mb-4 rounded-md bg-red-50 p-4">
          <div className="flex">
            <div className="ml-3">
              <h3 className="text-sm font-medium text-red-800">{error}</h3>
            </div>
          </div>
        </div>
      )}

      {/* Add Todo Form */}
      <form onSubmit={handleAddTodo} className="mb-6">
        <div className="flex gap-2">
          <input
            type="text"
            value={newTodo}
            onChange={(e) => setNewTodo(e.target.value)}
            placeholder="Add a new todo..."
            className="flex-1 min-w-0 block w-full px-3 py-2 rounded-md border border-gray-300 shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          />
          <button
            type="submit"
            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Add
          </button>
        </div>
      </form>

      {/* Todo List */}
      <div className="bg-white shadow overflow-hidden sm:rounded-md">
        <ul className="divide-y divide-gray-200">
          {todos.length === 0 ? (
            <li className="px-4 py-4 sm:px-6">
              <p className="text-gray-500">No todos yet. Add one above!</p>
            </li>
          ) : (
            todos.map((todo) => (
              <li key={todo.id} className="px-4 py-4 sm:px-6 hover:bg-gray-50">
                <div className="flex items-center justify-between">
                  <div className="flex items-center">
                    <TodoStatusToggle
                      todo={todo}
                      onStatusChange={(updatedTodo) => {
                        setTodos(todos.map(t => t.id === updatedTodo.id ? updatedTodo : t));
                      }}
                    />
                    <span className={`ml-3 text-sm ${todo.is_completed ? 'line-through text-gray-500' : 'text-gray-900'}`}>
                      {todo.title}
                    </span>
                  </div>
                  <div className="flex items-center">
                    <button
                      onClick={() => deleteTodo(todo.id)}
                      className="ml-2 inline-flex items-center px-2.5 py-0.5 border border-transparent text-xs font-medium rounded text-red-700 bg-red-100 hover:bg-red-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                    >
                      Delete
                    </button>
                  </div>
                </div>
                {todo.description && (
                  <div className="ml-7 mt-1 text-sm text-gray-500">
                    {todo.description}
                  </div>
                )}
                <div className="ml-7 mt-1 text-xs text-gray-400">
                  Created: {new Date(todo.created_at).toLocaleDateString()}
                </div>
              </li>
            ))
          )}
        </ul>
      </div>
    </div>
  );
}