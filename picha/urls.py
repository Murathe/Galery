from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r"^$", views.photo_category, name="photo_category"),
    url(r"^landing/$", views.landing, name="landing"),
    url(r"^search/$", views.search_results, name="search_results"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)