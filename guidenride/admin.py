from django.contrib import admin
from .models import DateTime,Events,Book,Tour,BookTour
admin.site.register(DateTime)
admin.site.register(Events)
admin.site.register(Book)
admin.site.register(Tour)
admin.site.register(BookTour)