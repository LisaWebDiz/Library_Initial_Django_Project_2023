# Library: Initial Django Experience Project 2023
### Description

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

### Features
    • Django admin panel for managing data
    • Fully documented REST API
    • Data storage using PostgreSQL
    • pgAdmin for database viewing: http://localhost:5050
    • Admin panel: http://localhost:8000/admin/
    • Registration/Authentication

### Pages

![Mainpage](assets/mainpage.png)
![Registration](assets/registration.png)
![Login](assets/login.png)
![Catalogue](assets/catalogue.png)
![Book_Detail](assets/detail.png)
![Add_Book](assets/add_book.png)
![Update_Book](assets/update_book.png)
![Contact us](assets/contact_us.png)
