# from datetime import date
#
# from django.test import TestCase
# from . import models, forms
#
# from django.test import Client
# from django.contrib.auth.models import User
#
#
# class TestModels(TestCase):
#     def test_model_create_fail(self):
#         book = {
#             "title": "Test Title",
#             "description": "Test Description",
#             "image": "image.png",
#             "created_date": date.today(),
#             "updated_date": date.today(),
#             "author": "author"
#     }
#     with self.assertRaises(ValueError):
#         book = models.Book.objects.create(**book)
#
#
# 
# class TestForm(TestCase):
#     def test_form_create_success(self):
#         book = {
#             "title": "Test Title",
#             "description": "Test Description",
#             "image": "image.png",
#             "created_date": date.today(),
#             "updated_date": date.today(),
#             "author": "author"
#         }
#         book = models.Book.objects.create(**book)
#         form = forms.BookForm(initial={"book": book})
#         is_valid_form = form.is_valid()
# 
#         self.assertTrue(is_valid_form)
#         form.save()

# 
# class TestViews(TestCase):
#     def test_get_success(self):
#         book = {
#             "title": "Test Title",
#             "description": "Test Description",
#             "image": "image.png",
#             "created_date": date.today(),
#             "updated_date": date.today(),
#             "author": "author"
#         }
#         book = models.Book.objects.create(**book)
#         client = Client()
#         user = User.objects.create(username='Username')
#         client.force_login(user)
#         response = client.get(path=f"/book/{book.id}/")
#         self.assertEqual(response.status_code, 404)



        
