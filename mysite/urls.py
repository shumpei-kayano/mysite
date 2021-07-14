from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # agencyのurlsにルーティングを移譲している
    path('', include('agency.urls')),
]
