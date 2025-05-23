from django.urls import path

from books.views import *

urlpatterns = [
    path('', index, name='index_book'),
    path('catalogue/', catalogue, name='books_list'),
    path('catalogue/<int:book_id>/', book_details, name='the_book'),

    path('books/add/', BookCreateView.as_view(), name='add_book'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='edit_book'),
    path('books/del/<int:pk>', BookDeleteView.as_view(), name='del_book'),

    path('registration/', user_registration, name='regis'),
    path('login/', user_login, name='log_in'),
    path('logout/', user_logout, name='log_out'),

    path('email/', contact_email, name='email_contact'),

    path('api/list', books_api_list, name='books_api_list'),
    path('api/detail/<int:pk>', books_api_detail, name='books_api_detail')
]

