from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import DateTime,Events,Book,Tour,BookTour
from io import BytesIO
from django.template.loader import  get_template
from django.views import View
from xhtml2pdf import  pisa
from django.utils.dateparse import parse_date
import datetime
from django.urls import reverse
from django.http import JsonResponse
import time
from django.core.mail import send_mail
from django.conf import settings
from easy_pdf.views import PDFTemplateResponseMixin
from django.views.generic import DetailView 
# from django.core.files.storage import FileSystemStorage
# from django.template.loader import render_to_string
# from weasyprint import HTML

import stripe

stripe.api_key = "sk_test_51GzfC7HYcAx7HskPg2OnvRBhSfP8MJDCqMmvmDEnQMKN5fO8xOnXT7A93JkDk46BCCZ7TPyPfDc0xQVrNSQTOWrt00qWSppVnw"

def index(request):
    # x = datetime.datetime.now()
    # day = "2"
    # month =" 3"
    # year = "11"
    # hour = "5"
    # minute = "36"
    # second= "55"
    #
    # order = DateTime(day=day, month=month, year=year, second=second, minute=minute, hour=hour,)
    # order.save()
    # myid = order.id
    # all_tour = Tours.objects.all()
    context ={}
    return render(request, 'index.html',context)

def tour(request):
    if request.method == "POST":
        passenger= request.POST.get('passenger', '')
        value = request.POST.get('test','')
        if value=="v1":
            tour = request.POST.get('tour1', '')
            price = request.POST.get('price1', '')
        elif value=="v2":
            tour = request.POST.get('tour2', '')
            price = request.POST.get('price2', '')
        elif value=="v3":
            tour = request.POST.get('tour3', '')
            price = request.POST.get('price3', '')
        else:
            tour = "2h30m"
            price="39.90"
            pass
        prices = price[:5]
        total = float(prices)*int(passenger)
        total = str(total)+"€"
        print(passenger,tour,price,total,value)
        tour = Tour(passenger=passenger,tour=tour, price=price,total=total)
        tour.save()
        tour_data={'passenger':passenger,'tour': tour, 'price':price,'total':total}
        return render(request, 'book.html',tour_data)
    return render(request, 'tour.html')


def book(request):
    if request.method == "POST":
        passenger= request.POST.get('passenger', '')
        date= request.POST.get('date', '')
        time= request.POST.get('time', '')
        tour = request.POST.get('tour', '')
        price = request.POST.get('price', '')
        prices = price[:5]
        total = float(prices) * int(passenger)
        total = str(total) + "€"
        print(passenger,date, time, tour, price, total)
        times = datetime.datetime.now().strftime('%H:%M')
        date = parse_date(date)
        date = date.strftime("%Y-%m-%d")
        dates = datetime.date.today()
        if time == "time":
            time = times
        print('time = '+ str(times) )
        if date == "":
            date = dates
        print('date = ' + str(dates))
        book = Book(passenger=passenger, date=date, time=time,tour=tour, price=price, total=total)
        book.save()
        # tour = Book.objects.all().filter()
        # print(tour.passenger)
        book_data = {'passenger': passenger, 'tour': tour,'date':date,'time':time, 'price': price, 'total': total}
        return render(request, 'booktour.html',book_data)
    return render(request, 'book.html')

def booktour(request):
    if request.method == "POST":
        passenger = request.POST.get('passenger', '')
        tour= request.POST.get('tour', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        price = request.POST.get('price', '')
        total = request.POST.get('total', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        country = request.POST.get('country', '')
        desc = request.POST.get('desc', '')
        print(passenger,tour,date,time,name, email, phone, country, desc)
        # passenger = passenger, tour = tour, date = date, time = time, name = name, price = price, total = total,
        booktour= BookTour(passenger = passenger, tour = tour, date = date, time = time, price = price, total = total,name=name, email=email, phone=phone,country=country,desc=desc)
        booktour.save()
        booktour_data = {'passenger':passenger,'name':name, 'tour':tour, 'date':date, 'time':time, 'price':price, 'total':total, 'email':email, 'phone':phone, 'country':country, 'desc':desc}
        return render(request, 'pdf_view.html',booktour_data)
    return render(request, 'booktour.html')


def events(request):
    if request.method == "POST":
        name= request.POST.get('name', '')
        email= request.POST.get('email', '')
        day= request.POST.get('day', '')
        month= request.POST.get('month', '')
        year= request.POST.get('year', '')
        phone= request.POST.get('phone', '')
        country= request.POST.get('country', '')
        desc = request.POST.get('desc', '')
        print(name, email,day,month,year,phone,country,desc)
        event = Events(name=name, email=email, phone=phone, day=day, month=month, year=year, country=country,desc=desc)
        event.save()
    return render(request, 'events.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def charge(request):
    if request.method == 'POST':
        print('Data:', request.POST)
        amount = float(request.POST['amount'])
        print(amount)
        customer = stripe.Customer.create(
        email=request.POST['email'],
        name=request.POST['nickname'],
        source=request.POST['stripeToken'],
        address =  {
            "city" : "landon", "country":"us", "line1" :"14 B",  "postal_code":"12345", "state" :"landon"}        )
        int_amount = amount*100
        int_amount = int(int_amount)
        charge = stripe.Charge.create(
        customer=customer,
        # amount=amount*100,
        amount=int_amount,
        currency='usd',
        description="charges for ride"
        )
    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'success.html', {'amount':amount})


def Mail_send(request):
    subject = 'Guide n Ride'
    message = 'Thank you for choosing us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mukeshsawthesuperman@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('success.html')



def render_to_pdf(template_src,context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    else:
        return HttpResponse('Errors')

data = {
    'company':'optimum python technical lab',
    'address': '123 street name',
    'city':'Indore',
    'state':'MP',
    'Phone':'5268463466'
}
class ViewPdf(View):
    def get(self, request,*args,**kwargs):
        pdf = render_to_pdf('pdf_template.html',data)
        return HttpResponse(pdf,content_type='application/pdf')

class DownloadPdf(View):
    def get(self, request,*args,**kwargs):
        pdf = render_to_pdf('pdf_view.html', data)
        response = HttpResponse(pdf,content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341213")
        content = "attachment; filename='%s'" %(filename)
        response['Content.Disposition'] = content
        return response


# def pdf_view(request):
#     return render(request, 'pdf_view.html')



class PDFDetailView(PDFTemplateResponseMixin, DetailView):
    # template_name = 'pdf_detail.html'
    def get(self, request,*args,**kwargs):
        pdf = render_to_pdf('pdf_detail.html', data)
        response = HttpResponse(pdf,content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341213")
        content = "attachment; filename='%s'" %(filename)
        response['Content.Disposition'] = content
        return response
        # model = get_user_model()