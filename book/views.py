from django.shortcuts import render
from . import  models
from django.shortcuts import get_object_or_404
from . import  forms
from django.shortcuts import reverse, redirect

def book_all(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book':book})

def book_detail(reguest,id):
    book_id = get_object_or_404(models.Book, id=id)
    comment_id = models.BookFeedback.objects.filter(foreign_key_id=id)
    return render(reguest, 'book_detail.html', {'book':book_id, 'comment':comment_id})

def add_book(request):
    if request.method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("books:book_list"))
            # return HttpResponse("Show Created Successfully")
    else:
        form = forms.BookForm()
    return render(request, "add_book.html", {"form": form})