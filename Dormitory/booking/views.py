from django.shortcuts import render, redirect
from .decorators import unauthenticated_user, allowed_users
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import *


def home(request):
    rooms = Room.objects.all()
    boys_room, girls_room = 0, 0
    for room in rooms:
        if room.available:
            if room.gender == 'Male':
                boys_room += 1
            elif room.gender == 'Female':
                girls_room += 1
    total_rooms = Room.objects.all().count()
    context = {'total_rooms': total_rooms, 'girls_room': girls_room,
               'boys_room': boys_room}
    return render(request, 'booking/home.html', context)


@login_required(login_url='sign_in')
def book(request):
    context = {}
    students = Student.objects.filter(user=request.user)
    for student in students:
        rooms = Room.objects.filter(gender=student.gender, course=student.course, faculty=student.faculty)
        context = {'rooms': rooms}

    if request.method == 'POST':
        room_number = request.POST['room_number']
        floor_number = request.POST['floor']
        block_name = request.POST['block']
        check_file = request.FILES.get('check')
        book_count = Booking.objects.filter(user=request.user).count()
        print(book_count)
        print(room_number, floor_number, block_name, check_file)
        if room_number != '' and floor_number != '' and block_name != '' and book_count < 1 and check_file is not None:
            floor = Floor.objects.get(floor_number=floor_number)
            block = Block.objects.get(block_name=block_name)
            gender, course, faculty = '', '', ''
            for student in Student.objects.filter(user=request.user):
                gender = student.gender
                course = student.course
                faculty = student.faculty
            print('work')
            room_count = Room.objects.filter(room_number=room_number, floor=floor, block=block,
                                             gender=gender, course=course, faculty=faculty, available=True).count()
            print(rooms.count())
            rooms = Room.objects.filter(bed_number=room_count, room_number=room_number, floor=floor, block=block,
                                        gender=gender, course=course, faculty=faculty)
            for room in rooms:
                if room.available:
                    Booking.objects.create(user=request.user, room=room, check_file=check_file)
                    room.available = False
                    room.save()
        else:
            return redirect('book')

    return render(request, 'booking/book.html', context)


@unauthenticated_user
def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist")
            return redirect('sign_up')

        if User.objects.filter(email=email):
            messages.error(request, "Email address already exist")
            return redirect('sign_up')

        if password1 != password2:
            messages.error(request, "Passwords didn't match")

        else:
            my_user = User.objects.create_user(username, email, password1)
            my_user.first_name = first_name
            my_user.last_name = last_name
            my_user.email = email
            my_user.save()
            group = Group.objects.get(name='customer')
            my_user.groups.add(group)
            print(my_user, group)
            messages.success(request, "Your account has been successfully created ")
            return redirect('sign_in')
    return render(request, 'booking/sign_up.html')


@unauthenticated_user
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    print('login')
    return render(request, 'booking/sign_in.html', context)


def logout_user(request):
    logout(request)
    return redirect('sign_in')


@login_required(login_url='sign_in')
def profile(request):
    students = request.user
    context = {'students': students}
    return render(request, 'booking/profile.html', context)


@login_required(login_url='sign_in')
def account_settings(request):
    user = request.user
    saved = ''
    form = UserForm(instance=user)
    student_form = StudentForm(instance=request.user.student)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        student_form = StudentForm(request.POST, instance=request.user.student)
        if form.is_valid() and student_form.is_valid():
            form.save()
            student_form.save()
            saved = 'Saved!'
    context = {'form': form, 'student_form': student_form, 'saved': saved}
    return render(request, 'booking/account_settings.html', context)


@allowed_users(allowed_roles=['admin'])
@login_required(login_url='sign_in')
def add_room(request):
    if request.method == 'POST':
        bed_number = request.POST['bed_number']
        room_number = request.POST['room_number']
        floor_number = request.POST['floor']
        block_name = request.POST['block']
        gender = request.POST['gender']
        course = request.POST['course']
        faculty = request.POST['faculty']
        button = request.POST['button']
        print(bed_number, room_number, floor_number, block_name, button, gender)
        if room_number != '' and floor_number != '' and block_name != '':
            floor = Floor.objects.get(floor_number=floor_number)
            block = Block.objects.get(block_name=block_name)
            if button == 'Add':
                print('work')
                room = Room.objects.create(bed_number=bed_number, room_number=room_number, floor=floor, block=block,
                                           gender=gender, course=course, faculty=faculty)
                room.save()
            elif button == 'Delete' and Room.objects.filter(bed_number=bed_number, room_number=room_number, floor=floor, block=block,
                                                            gender=gender, course=course, faculty=faculty):
                Room.objects.filter(bed_number=bed_number, room_number=room_number, floor=floor, block=block,
                                    gender=gender, course=course, faculty=faculty).delete()
        else:
            return redirect('add_room')
    context = {}
    return render(request, 'booking/add_room.html', context)


@login_required(login_url='sign_in')
def room_list(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'booking/room_list.html', context)


@login_required(login_url='sign_in')
def booking_list(request):
    book_list = Booking.objects.all()
    button = request.POST.get('cancel')
    booked = Booking.objects.filter(user=request.user)
    print(button)
    if button == 'Cancel' and booked:
        print('cancel')
        Booking.objects.filter(user=request.user).delete()
        for booking in booked:
            rooms = Room.objects.filter(room_number=booking.room.room_number,
                                        floor=booking.room.floor, block=booking.room.block)
            for room in rooms:
                room.available = True
                room.save()

    context = {'book_list': book_list}
    return render(request, 'booking/booking_list.html', context)
