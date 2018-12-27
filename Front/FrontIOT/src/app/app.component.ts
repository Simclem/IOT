import { Component, OnInit } from '@angular/core';
import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [AppService]
})
export class AppComponent implements OnInit {
  constructor(public service: AppService) {

  }
  ngOnInit() {
    this.initFront();
  }

  initFront() {
    this.service.getAllStatus().subscribe((data: any) => {
      console.log(data);
    });
  }
}
