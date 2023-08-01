from django.shortcuts import render, redirect
from .models import bookingsystem


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        to = request.POST.get('to')
        departuredate = request.POST.get('departuredate')
        returntrip = request.POST.get('returntrip')


        query = bookingsystem.objects.create(name=name, email=email, phone=phone, to=to, departuredate=departuredate, returntrip=returntrip,)
        query.save()
        return redirect("/")
    return render(request, "index.html")


# function for index page
def indexpage(request):
    data = bookingsystem.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


# function to delete data
def deleteData(request, id):
    d = bookingsystem.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


# function to update records
def updateData(request, id, ):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        to = request.POST.get('to')
        departuredate = request.POST.get('departuredate')
        returntrip = request.POST.get('returntrip')

        edit_data = bookingsystem.objects.get(id=id)
        edit_data.name = name
        edit_data.email = email
        edit_data.phone = phone
        edit_data.to = to
        edit_data.departuredate = departuredate
        edit_data.returntrip = returntrip
        edit_data.save()
        return redirect("/")

    dta = bookingsystem.objects.get(id=id)
    context = {"dta": dta}
    return render(request, "edit.html", context)
