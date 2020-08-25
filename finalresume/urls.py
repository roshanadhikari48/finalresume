from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('project/<int:project_id>', views.detail, name='detail'),
    path('blog/', include('blog.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
