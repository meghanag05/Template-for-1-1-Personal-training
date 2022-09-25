
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Mohan Kulapathi"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Administrator"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))

]
