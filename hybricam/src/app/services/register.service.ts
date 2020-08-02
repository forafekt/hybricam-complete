import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

const baseUrl = 'https://192.168.8.101:8000/api/marketing/email-subscribe/'; // Change to live domain on deployment
@Injectable({
  providedIn: 'root'
})
export class RegisterService {

  constructor(private http: HttpClient) { }

    getAll(): Observable<any> {
      return this.http.get(baseUrl);
    }

    get(id: any): Observable<any> {
      return this.http.get(`${baseUrl}/${id}`);
    }

    create(data: any): Observable<any> {
      return this.http.post(baseUrl, data);
  }
}