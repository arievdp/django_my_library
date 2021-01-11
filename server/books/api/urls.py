from .views import bookAPIView
# imports the bookAPIView from .views

from django.conf.urls import url
urlpatterns = [
  url(r'^$', bookAPIView.as_view(), name='book-create'),
]
# The pattern r’^$’is a regular expression that ‘matches an empty line/string’. This means it matches to localhost:8000. It matches to anything that comes after the base URL.

# We call .as_view() on bookAPIView to connect the view to the url. It is the function which will connect the class with its url.

# The name=’book-create’ attribute provides us with a name attribute. We use it to refer to our URL throughout the project. Let’s say you want to change the URL or the view it refers to. Change it here. Without name we would have to go through the entire project to update every reference.