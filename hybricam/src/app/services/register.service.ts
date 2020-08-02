import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// https://hybricam.herokuapp.com
// https://192.168.8.101:8000
// Change to live domain on deployment
const baseUrl = 'https://hybricam.herokuapp.com/api/marketing/email-subscribe/';
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
