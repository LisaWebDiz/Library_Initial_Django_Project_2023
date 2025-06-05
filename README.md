# Library: Initial Django Experience Project 2023
### Description
This is a simple Library Management Web Application built with Django and Django REST Framework. The app allows users to register, browse books, and manage data via an admin panel or API. It uses PostgreSQL for data storage and supports RESTful API endpoints with full documentation.

### Quick start via Docker

```bash
git clone https://github.com/yourusername/library_initial_django_project_2023.git
cd library_initial_django_project_2023
cp example.env .env
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
Enjoy!

### Key Features

    • User registration & authentication via Django’s built-in django.contrib.auth framework
    • Django admin panel for managing data at http://localhost:8000/admin/
    • Fully documented REST API
    • Data storage using PostgreSQL
    • Built-in pgAdmin interface for managing the database at http://localhost:5050
    • Catalogue list view and detail view for books
    • Add / edit / delete book entries — available for registered users
    • Frontend styled with CSS and Bootstrap


### Pages

![Mainpage](assets/mainpage.png)
![Registration](assets/registration.png)
![Login](assets/login.png)
![Catalogue](assets/catalogue.png)
![Book_Detail](assets/detail.png)
![Add_Book](assets/add_book.png)
![Update_Book](assets/update_book.png)
![Contact us](assets/contact_us.png)
