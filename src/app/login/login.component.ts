import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  userUrl ='http://127.0.0.1.5000/user/';
  adminUrl;
  suburl;
  loginJson;
  adminJson;
signUpForm;
loginForm;

  constructor(private http: HttpClient) {
     this.signUpForm = new FormGroup({
      phoneNum : new FormControl(null, [Validators.required]),
      password: new FormControl(null, [Validators.required])
    });
     this.loginForm = new FormGroup({
      phoneNum : new FormControl(null, [Validators.required, Validators.pattern(/^[6-9]\d{9}$/)]),
      password: new FormControl(null, [Validators.required])
    });
  }

  ngOnInit(): void {
  }
  onLogin(): void{
  this.suburl = this.userUrl + this.loginForm.phoneNum;
  this.http.get(this.suburl).toPromise().then(data => {
    this.loginJson = data;
  });
  alert('Login success' + this.loginJson);
}
onSignUp(): void {
  if ( this.signUpForm.valid){
    this.http.get(this.adminUrl).toPromise().then(data => {
      this.adminJson = data;
    });
    alert('Login success' + this.loginJson);
  }
  else{
    alert(' noooo');
  }
}
}
