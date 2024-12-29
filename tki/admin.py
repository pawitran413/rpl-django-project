from django.contrib import admin
from .models import Tki
from .models import Course

# Register your models here.
class TkiAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname", "nim", "angkatan", "fakultas", "prodi", "status")

class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "matkul", "tki_id")

admin.site.register(Tki, TkiAdmin)
admin.site.register(Course, CourseAdmin)
