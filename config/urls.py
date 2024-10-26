from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('users/', include('users.urls')),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += debug_toolbar_urls()