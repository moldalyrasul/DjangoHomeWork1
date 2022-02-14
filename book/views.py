from django.shortcuts import render
from . import  models
from django.shortcuts import get_object_or_404

def book_all(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book':book})

def book_detail(reguest,id):
    book_id = get_object_or_404(models.Book, id=id)
    comment_id = models.BookFeedback.objects.filter(foreign_key_id=id)
    return render(reguest, 'book_detail.html', {'book':book_id, 'comment':comment_id})