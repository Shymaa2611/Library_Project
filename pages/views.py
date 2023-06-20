from django.shortcuts import render,redirect
from .models import books,Category
from .forms import BookForm,CategoryForm

def index(request):
    sum=0
    for x in books.objects.all():
        if x.status=='sold':
            sum=sum+x.price
        elif x.status=='rental':
            sum=sum+x.price
    totalSold=0
    for x in books.objects.all():
        if x.status=='sold':
            totalSold=totalSold+x.price
    totalRental=0
    for x in books.objects.all():
        if x.status=='rental':
            totalRental=totalRental+x.price
    context={
        'book':books.objects.all(),
        'cat':Category.objects.all(),
        'form':BookForm(),
        'catForm':CategoryForm(),
       
        'numberofbooks':books.objects.count(),
        'numberofSoldBooks':books.objects.filter(status='sold').count(),
        'numberofRenatlBooks':books.objects.filter(status='rental').count(),
        'numberofavailabileBooks':books.objects.filter(status='aviliability').count(),
        'revenue':sum,
        'totalRental': totalRental,
        'totalSold':totalSold
    }
   
    if request.method=='POST':
        allbooks=BookForm(request.POST)
        if allbooks.is_valid():
            allbooks.save()
            return redirect('/')
    if request.method=='POST':
        allcategories=CategoryForm(request.POST)
        if allcategories.is_valid():
            allcategories.save()
            return redirect('/')
    return render(request,'pages/index.html',context)

def book(request):
    search=books.objects.all()
    title=None
    if 'search_name' in request.GET:
        title=request.GET['search_name']
        if title:
            search=search.filter(title__icontains=title)
    context={
        'book':search,
        'catForm':CategoryForm()
    } 
    return render(request,'pages/books.html',context)
 
def update(request,id):
    bookid=books.objects.get(id=id)
    if request.method=='POST':
        newBookInfo=BookForm(request.POST,instance=bookid)
        if newBookInfo.is_valid():
            newBookInfo.save()
            return redirect('/')
    else:
        newBookInfo=BookForm(instance=bookid)
    context={
        'form':newBookInfo,
    }
    return render(request,'pages/update.html',context)

def delete(request,id):
    bookid=books.objects.get(id=id)
    if request.method=='POST':
        bookid.delete()
        return redirect('/')
    return render(request,'pages/delete.html')
def updateBook(request,id):
    bookid=books.objects.get(id=id)
    if request.method=='POST':
        newBookInfo=BookForm(request.POST,instance=bookid)
        if newBookInfo.is_valid():
            newBookInfo.save()
            return redirect('/book')
    else:
        newBookInfo=BookForm(instance=bookid)
    context={
        'form':newBookInfo,
    }
    return render(request,'pages/update.html',context)
def deleteBook(request,id):
    bookid=books.objects.get(id=id)
    if request.method=='POST':
        bookid.delete()
        return redirect('/book')
    return render(request,'pages/delete.html')