from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url, include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('guess-who/', include('guess_who_app.urls'))
#     # url(r'^', include(router.urls))
]
