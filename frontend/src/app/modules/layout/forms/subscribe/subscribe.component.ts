import { Component, OnInit, Input } from '@angular/core';
import { SubscribeService } from './subscribe.service';
import { MatSnackBar } from '@angular/material/snack-bar';


@Component({
  selector: 'app-subscribe',
  templateUrl: './subscribe.component.html',
  styleUrls: ['./subscribe.component.scss']
})
export class SubscribeComponent implements OnInit {
  Subscribe = ({
    email: '',
  });
  submitted = false;

  constructor(
    private subscribeService: SubscribeService,
    public snackBar: MatSnackBar
    ) { }
    openSnackBar(message: string, action: string) {
      this.snackBar.open(message, action, {
         duration: 90000,
        });
      }

  ngOnInit(): void {
  }

  saveSubscribe(): void {
    const data = {
      email: this.Subscribe.email,
    };
    this.subscribeService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
        },
        error => {
          console.log(error);
          this.snackBar.open(error.error.message, 'Error: You may have already subscribed!  Please try another e-mail...');
        });
  }
}

