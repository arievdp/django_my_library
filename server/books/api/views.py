# A view takes a web request and returns a web response

from rest_framework import generics, mixins
# generics refers to API views that map to your database models - pre built views that provide for common patterns
# mixin classes provide the actions that are used to provide the basic view behaviour, such as .get() and .post(), destroy and update
from books.models import Book
from .serializers import bookSerializer
class bookAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  # CreateModelMixin - provides .create(request, *args, **kwargs)
  # Returns 201 Create response / 400 Bad Request
  # ListAPIView serves read-only enpoints (GET) - represents a collection of model instances
  resource_name = 'books'
  # lowercase books so it is the same model in Ember and Django
  serializer_class = bookSerializer
  # returns all book objects in the database
  def get_queryset(self):
    return Book.objects.all()
  # creates a new database record of a book using the request and arguments
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
    # **kwargs used to pass a keyworded variable-length argument to a function eg. a hash / object of data
    # function(kwargs_1='test', kwargs_2='test_2') will be outputted as {'kwargs_2': 'test_2', 'kwargs_1': 'test'}