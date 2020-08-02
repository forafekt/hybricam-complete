import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-dialog',
  templateUrl: './dialog.component.html',
  styleUrls: ['./dialog.component.scss']
})
export class DialogComponent {
  
}

@Component({
  selector: 'app-dialog-button',
  templateUrl: './dialog-button.component.html',
})
export class DialogButton implements OnInit {
  
constructor(public dialog: MatDialog) {}

openDialog(): void {
  let config = new DialogComponent();
  config = {
    position: {
      top: '0',
      right: '0',
    },
    maxWidth: '100vw',
    height: '100%',
    width: '100vw',
    panelClass: 'form-dialog',
  };
  const dailog = this.dialog.open(DialogComponent, config);
}
ngOnInit() {
  this.openDialog()
}
}