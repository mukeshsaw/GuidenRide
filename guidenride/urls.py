"""guidenride URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('payments.urls')),
    path('', views.index, name='index'),
    path('tour', views.tour, name='tour'),
    path('booktour', views.booktour, name='booktour'),
    path('book', views.book, name='book'),
    path('events', views.events, name='events'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('pdf_view', views.ViewPdf.as_view(), name='pdf_view'),
    path('pdf_download', views.DownloadPdf.as_view(), name='pdf_download'),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
    path('home', views.home, name='home'),
    path('Mail_send', views.Mail_send, name='Mail_send'),
    path('pdf_detail', views.PDFDetailView.as_view(), name='pdf_detail'),
    # path('html_to_pdf_view', views.html_to_pdf_view, name='html_to_pdf_view'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
