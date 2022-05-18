from django.db import models
from django.contrib.auth.models import User

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

COURSE = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
]
FACULTY = [
    ('Faculty of Law and Social Sciences', 'Faculty of Law and Social Sciences'),
    ('Faculty of Education and Humanities Sciences', 'Faculty of Education and Humanities Sciences'),
    ('Faculty of Engineering and Natural Sciences', 'Faculty of Engineering and Natural Sciences'),
    ('Business school', 'Business school')
]


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField('Phone', max_length=13, null=True, blank=True)
    gender = models.CharField('Gender', choices=GENDER, max_length=50, null=True, blank=True)
    course = models.IntegerField('Course year', choices=COURSE, null=True, blank=True)
    faculty = models.CharField('Faculty name', choices=FACULTY, max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def save(self, **kwargs):
        super(Student, self).save(**kwargs)


class Block(models.Model):
    block_name = models.CharField('Block name', max_length=50)

    def __str__(self):
        return str(self.block_name) + ' block'

    class Meta:
        ordering = ('block_name', )


class Floor(models.Model):
    floor_number = models.IntegerField('Floor number')

    def __str__(self):
        return str(self.floor_number) + ' floor'

    class Meta:
        ordering = ('floor_number', )


class Room(models.Model):
    bed_number = models.IntegerField('Bed number')
    room_number = models.IntegerField('Room number')
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    gender = models.CharField('Gender', choices=GENDER, max_length=100)
    course = models.IntegerField('Course year', choices=COURSE)
    faculty = models.CharField('Faculty name', choices=FACULTY, max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.block) + ' block ' + str(self.floor) + ' floor ' + str(self.room_number) + ' room'

    class Meta:
        ordering = ('room_number', )


class Booking(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_file = models.FileField(null=True)

    def __str__(self):
        return str(self.user) + ' ' + str(self.room)

