"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books', include(('books.api.urls', 'books'), namespace='api-books'))
]

# Here we import include and create the 'api/books’ pattern which takes in any URLs we created in the api folder. Now the base URL for our books API URLs becomes localhost:8000/api/books. Visiting this URL will match to our r’^/api/books’ pattern. This matches to the r’^$’ pattern we constructed in the books API.

# We use namespace=’api-books’ so that the URLs don’t collide with each other. This would happen if they’re named the same in another app we create. Learn more about why we use namespaces in this thread.