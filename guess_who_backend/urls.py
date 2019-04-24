from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guess-who/', include('guess_who_app.urls'))
]
