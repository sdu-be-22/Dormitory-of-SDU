from django.contrib import admin
from .models import Student, Room, Floor, Block, Booking


admin.site.register(Student)
admin.site.register(Block)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Booking)
