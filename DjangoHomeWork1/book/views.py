from django.shortcuts import get_object_or_404
from django.shortcuts import reverse, redirect
from django.http import Http404, HttpResponse
from django.views import generic
from . import models, forms


class BookListView(generic.ListView):
    template_name = "book_list.html"
    queryset = models.Book.objects.all()
    # context_name = 'book'


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



def put_book_update(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    if request.method == "POST":
        form = forms.BookForm(instance=book_id,
                                data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("books:book_list"))
    else:
        form = forms.BookForm(instance=book_id)
    return render(request, "book_update.html", {"form": form,
                                                 "book": book_id})


def book_delete(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    book_id.delete()
    return redirect(reverse("books:book_list"))


    def get_queryset(self):
        return self.queryset

# def book_all(request):
#     book = models.Book.objects.all()
#     return render(request, 'book_list.html', {'book':book})


class BookDetailView(generic.DetailView):
    template_name = "book_detail.html"
    # context_name = 'book'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

# def book_detail(reguest,id):
#     book_id = get_object_or_404(models.Book, id=id)
#     comment_id = models.BookFeedback.objects.filter(foreign_key_id=id)
#     return render(reguest, 'book_detail.html', {'book':book_id, 'comment':comment_id})


class BookCreateView(generic.CreateView):
    template_name = "add_book.html"
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = "/books/"
    # context_name = 'book'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)

# def add_book(request):
#     if request.method == "POST":
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("books:book_list"))
#             # return HttpResponse("Show Created Successfully")
#     else:
#         form = forms.BookForm()
#     return render(request, "add_book.html", {"form": form})

class BookUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forms.BookForm
    success_url = "/books/"
    # context_name = 'book'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super(BookUpdateView, self).form_valid(form=form)

# def put_book_update(request, id):
#     book_id = get_object_or_404(models.Book, id=id)
#     if request.method == "POST":
#         form = forms.BookForm(instance=book_id,
#                                 data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("books:book_list"))
#     else:
#         form = forms.BookForm(instance=book_id)
#     return render(request, "book_update.html", {"form": form,
#                                                  "book": book_id})



class BookDeleteView(generic.DeleteView):
    success_url = "/books/"
    template_name = "confirm_delete_book.html"
    # context_name = 'book'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

# def book_delete(request, id):
#     book_id = get_object_or_404(models.Book, id=id)
#     book_id.delete()
#     return redirect(reverse("books:book_list"))

