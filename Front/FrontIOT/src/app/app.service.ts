import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class AppService {
    constructor(private http: HttpClient) { }

    getAllStatus(): any {
        return this.http.get('http://192.168.1.16:5000/getStatus');
    }
}
