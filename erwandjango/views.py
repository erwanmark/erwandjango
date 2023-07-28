from django.shortcuts import render, redirect
from .models import people


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        city = request.POST.get('city')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = people.objects.create(name=name, email=email, phone=phone, country=country, city=city, age=age,
                                      gender=gender)
        query.save()
        return redirect("/")
    return render(request, "index.html")


# function for index page
def indexpage(request):
    data = people.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


# function to delete data
def deleteData(request, id):
    d = people.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


# function to update records
def updateData(request, id, ):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        city = request.POST.get('city')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        edit_data = people.objects.get(id=id)
        edit_data.name = name
        edit_data.email = email
        edit_data.phone = phone
        edit_data.age = age
        edit_data.gender = gender
        edit_data.country = country
        edit_data.city = city
        edit_data.save()
        return redirect("/")

    dta = people.objects.get(id=id)
    context = {"dta": dta}
    return render(request, "edit.html", context)