from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import BookForm, RegistrationForm, LoginForm, ContactForm
from .models import Book
from .serializer import BookSerializer


def index(request):
    return render(request, 'books/index.html')


def catalogue(request):
    context = {'books_list': Book.objects.all()}

    paginator = Paginator(Book.objects.all(), 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)

    context['page_obj'] = page_objects

    return render(request, 'books/books_list.html', context)


@permission_required('books.add_book')
def book_details(request, book_id):
    the_book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book_info.html', {'book_item': the_book})


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_add.html'
    context_object_name = 'form'
    success_url = reverse_lazy('books_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_edit.html'
    context_object_name = 'form'
    success_url = reverse_lazy('books_list')

    @method_decorator(permission_required('books.change_book'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('books_list')

    @method_decorator(permission_required('books.delete_book'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            return redirect('index_book')
    else:
        form = RegistrationForm()
    return render(request, 'books/auth/registration.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print('is_anon', request.user.is_anonymous)
            print('is_auth', request.user.is_authenticated)
            login(request, user)
            print('is_anon', request.user.is_anonymous)
            print('is_auth', request.user.is_authenticated)
            print(user)
            return redirect('index_book')
    else:
        form = LoginForm()
    return render(request, 'books/auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('log_in')


def contact_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['content'],
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_RECEIVER],
                fail_silently=False
            )
            if mail:
                return redirect('index_book')
    else:
        form = ContactForm()
    return render(request, 'books/email.html', {'form': form})


@api_view(['GET', 'POST'])
def books_api_list(request):
    if request.method == 'GET':
        books_list = Book.objects.all()
        serializer = BookSerializer(books_list, many=True)
        return Response({'books_list': serializer.data})
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def books_api_detail(request, pk, format=None):
        book_obj = get_object_or_404(Book, pk=pk)
        if book_obj.exist:
            if request.method == 'GET':
                serializer = BookSerializer(book_obj)
                return Response(serializer.data)
            elif request.method == 'PUT':
                serializer = BookSerializer(book_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': "Данные успешно изменены", 'books': serializer.data})
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method == 'DELETE':
                book_obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
