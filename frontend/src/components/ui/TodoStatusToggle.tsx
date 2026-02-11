'use client';

import { useState } from 'react';
import { todoApi } from '@/app/api/todos';
import { Todo } from '@/app/api/todos';

interface TodoStatusToggleProps {
  todo: Todo;
  onStatusChange: (updatedTodo: Todo) => void;
}

export default function TodoStatusToggle({ todo, onStatusChange }: TodoStatusToggleProps) {
  const [isLoading, setIsLoading] = useState(false);

  const toggleStatus = async () => {
    if (isLoading) return;

    setIsLoading(true);
    try {
      const updatedTodo = await todoApi.toggleTodoCompletion(todo.id, !todo.is_completed);
      onStatusChange(updatedTodo);
    } catch (error) {
      console.error('Failed to update todo status:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <button
      onClick={toggleStatus}
      disabled={isLoading}
      className={`relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 ${
        todo.is_completed ? 'bg-green-500' : 'bg-gray-200'
      }`}
      aria-pressed={todo.is_completed}
    >
      <span className="sr-only">Toggle todo completion</span>
      <span
        className={`pointer-events-none relative inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out ${
          todo.is_completed ? 'translate-x-5' : 'translate-x-0'
        }`}
      >
        <span
          className={`absolute inset-0 flex h-full w-full items-center justify-center transition-opacity ${
            todo.is_completed ? 'opacity-0 ease-out duration-100' : 'opacity-100 ease-in duration-200'
          }`}
          aria-hidden="true"
        >
          <svg className="h-3 w-3 text-gray-400" fill="none" viewBox="0 0 12 12">
            <path
              d="M4 8l2-2m0 0l2-2M6 6L4 4m2 2l2 2"
              stroke="currentColor"
              strokeWidth={2}
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </span>
        <span
          className={`absolute inset-0 flex h-full w-full items-center justify-center transition-opacity ${
            todo.is_completed ? 'opacity-100 ease-in duration-200' : 'opacity-0 ease-out duration-100'
          }`}
          aria-hidden="true"
        >
          <svg className="h-3 w-3 text-green-500" fill="currentColor" viewBox="0 0 12 12">
            <path d="M3.707 5.293a1 1 0 00-1.414 1.414l1.414-1.414zM5 8l-.707.707a1 1 0 001.414 0L5 8zm4.707-3.293a1 1 0 00-1.414-1.414l1.414 1.414zm-7.414 2l2 2 1.414-1.414-2-2-1.414 1.414zm3.414 2l4-4-1.414-1.414-4 4 1.414 1.414z" />
          </svg>
        </span>
      </span>
    </button>
  );
}