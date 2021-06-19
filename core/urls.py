"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from catalog.views import RegisterFormView

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
# Homework 6. Django forms 'triangle'
urlpatterns += [
    path('triangle/', include('triangle.urls')),
]
# Homework 7. Django model form 'Person/Person update'
urlpatterns += [
    path('person/', include('person.urls')),
]
# Mozilla tutorial
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    path('catalog/', include('catalog.urls')),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/register/", RegisterFormView.as_view(), name="register"),
]

# HomeWork 10: ddt, silk
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls)),
        path('silk/', include('silk.urls', namespace='silk')),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
