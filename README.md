# Hybricam Complete

Mobile-browser camera application developed with Angular, Django & Django REST.
This project was developed on a clients need for a product event, where they need to retrieve customer information then 
allow the user to take a photo of the product and add filters to the picture then save or share the image. After the 
even the client then needs to extract the data.

## TODO:
* Clean-up Service-worker and other PWA elements.
* Package the 'serve' app.
* Add more dynamic to API.
* Clean code.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing 
purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Django Framework
Django REST Framework
Angular@latest
```

### Installing

I will give more in depth instructions as i continue to develop the project.

```
pip install -r requirements.txt
```

cd hybricam

```
npm install
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

For development you will need to run 2 localhosts in HTTPS.

### Certificates includes in project
There is also a script in /hybricam/ssl/example.crt to create your own.


Django
<br>
Angular

```
Django : python manage.py runserver_plus 0.0.0.0:8000 --cert-file hybricam/ssl/example.crt

Angular : ng serve --host=0.0.0.0
```


## Deployment

Use the environment variables and automated scripts to deploy. At the moment it is setup for Heroku.

## Built With

* [Django](https://github.com/django/django) - Back-end
* [Django REST](https://github.com/encode/django-rest-framework) - API service
* [Angular](https://github.com/angular/angular) - Front-end client

## Contributing
 
Open to contributions.  Many hands make light work.

## Authors

* **Jonny Doyle** - *Initial work* - [LinkedIn](https://www.linkedin.com/in/jonnydoyle/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* WebRTC
