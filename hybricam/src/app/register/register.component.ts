import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, FormControl } from '@angular/forms';
import { RegisterService } from '../services/register.service';
import { MatSnackBar } from '@angular/material/snack-bar';


@Component({
    selector: 'app-register',
    templateUrl: './register.component.html',
    styleUrls: ['./register.component.scss']
})

export class RegisterComponent implements OnInit {
    registerForm: FormGroup;
    submitted = false;

    constructor(private formBuilder: FormBuilder, public snackBar: MatSnackBar, private registerService: RegisterService) { }

    ngOnInit() {
        this.registerForm = this.formBuilder.group({
            firstName: ['', Validators.required],
            lastName: ['', Validators.required],
            email: ['', [Validators.required, Validators.email,Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$')]],
            accepted: new FormControl("yes")
        });
    }

    // convenience getter for easy access to form fields
    get f() { return this.registerForm.controls; }

    onSubmit(message: string, action: string): void {
      this.registerService.create(this.registerForm.value)
      .subscribe(
        response => {
          console.log(response);
          this.snackBar.open(message, action, {
            duration: 90000,
          });
          this.submitted = true;
        },
        error => {
          console.log(error);
          this.snackBar.open(error.error.message, 'Connection error or please try another e-mail.');
          
          location.reload()
        });
        (error: { error: { message: string; }; }) => {
          console.log(error);
        }
        
        // stop here if form is invalid
        if (this.registerForm.invalid) {
            return;
        }
      }
  }
