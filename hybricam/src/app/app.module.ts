import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppFlexMaterialModule } from './app-flex-material.module';
import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { UploadComponent } from './upload/upload.component';
import { CameraComponent } from './camera/camera.component';

import { CommonModule } from '@angular/common';
import { RegisterComponent } from './register/register.component';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { DialogComponent, DialogButton } from './register/dialog/dialog.component';
import { TrueFalseValueDirective } from './register/true-false-value.directive';


@NgModule({
  imports:      [ CommonModule, BrowserModule, BrowserAnimationsModule, AppFlexMaterialModule, AppRoutingModule, ReactiveFormsModule, FormsModule, HttpClientModule, ],
  declarations: [ AppComponent, UploadComponent, CameraComponent, RegisterComponent, DialogComponent, DialogButton, TrueFalseValueDirective ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
