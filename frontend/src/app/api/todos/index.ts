'use client';

import axios from 'axios';

interface Todo {
  id: string;
  title: string;
  description?: string;
  is_completed: boolean;
  user_id: string;
  created_at: string;
  updated_at: string;
  due_date?: string;
}

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

const apiClient = axios.create({
  baseURL: `${API_BASE_URL}/api`,
});

// Request interceptor to add auth token
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export const todoApi = {
  // Get all todos for the current user
  getTodos: async (): Promise<Todo[]> => {
    try {
      const response = await apiClient.get('/todos');
      return response.data;
    } catch (error) {
      console.error('Error fetching todos:', error);
      throw error;
    }
  },

  // Create a new todo
  createTodo: async (todoData: Partial<Todo>): Promise<Todo> => {
    try {
      const response = await apiClient.post('/todos', todoData);
      return response.data;
    } catch (error) {
      console.error('Error creating todo:', error);
      throw error;
    }
  },

  // Update a todo
  updateTodo: async (id: string, todoData: Partial<Todo>): Promise<Todo> => {
    try {
      const response = await apiClient.put(`/todos/${id}`, todoData);
      return response.data;
    } catch (error) {
      console.error('Error updating todo:', error);
      throw error;
    }
  },

  // Toggle todo completion status
  toggleTodoCompletion: async (id: string, isCompleted: boolean): Promise<Todo> => {
    try {
      const response = await apiClient.patch(`/todos/${id}/complete`, { is_completed: isCompleted });
      return response.data;
    } catch (error) {
      console.error('Error toggling todo completion:', error);
      throw error;
    }
  },

  // Delete a todo
  deleteTodo: async (id: string): Promise<void> => {
    try {
      await apiClient.delete(`/todos/${id}`);
    } catch (error) {
      console.error('Error deleting todo:', error);
      throw error;
    }
  },
};