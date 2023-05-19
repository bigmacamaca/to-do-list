import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Task } from '../models/task.model';

const getAllTaskURL= 'http://127.0.0.1:8080/tasks/api/get_tasks'
const getTaskDetailURL= 'http://127.0.0.1:8080/tasks/api/get_task_details'
const searchTaskURL = 'http://127.0.0.1:8080/tasks/api/search_task'
const createTaskURL= 'http://127.0.0.1:8080/tasks/api/create_task/'
const updateTaskURL= 'http://127.0.0.1:8080/tasks/api/update_task'
const deleteTaskURL= 'http://127.0.0.1:8080/tasks/api/delete_task'
const deleteAllTaskURL = 'http://127.0.0.1:8080/tasks/api/delete_all_tasks'

@Injectable({
  providedIn: 'root'
})
export class TaskService {

  constructor(private http: HttpClient) { }

  getAll(): Observable<Task[]> {
    return this.http.get<Task[]>(getAllTaskURL);
  }

  get(id: any): Observable<Task> {
    return this.http.get(`${getTaskDetailURL}/${id}`);
  }
  
  findByTitle(title: any): Observable<Task[]> {
    return this.http.get<Task[]>(`${searchTaskURL}?title=${title}`);
  }

  create(data: any): Observable<any> {
    return this.http.post(createTaskURL, data);
  }

  update_task(id: any, data: any): Observable<any> {
    return this.http.put(`${updateTaskURL}/${id}/`, data);
  }

  delete(id: any): Observable<any> {
    return this.http.delete(`${deleteTaskURL}/${id}`);
  }

  deleteAll():Observable<any> {
    return this.http.delete(deleteAllTaskURL);
  }

}
