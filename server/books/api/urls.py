from .views import bookAPIView
# imports the bookAPIView from .views

from django.conf.urls import url
urlpatterns = [
  url(r'^$', bookAPIView.as_view(), name='book-create'),
]
# The pattern r’^$’is a regular expression that ‘matches an empty line/string’. This means it matches to localhost:8000. It matches to anything that comes after the base URL.

# We call .as_view() on bookAPIView to connect the view to the url. It is the function which will connect the class with its url.