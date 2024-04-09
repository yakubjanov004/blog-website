from django.contrib import admin
from django.urls import path
from app.views import home,portfolio_detail,single_blog_uchun,blog,about_me,portfolio
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('portfolio-detail/<int:pk>/', portfolio_detail, name="portfolio_detail"),
    path('single-blog/<int:pk>/', single_blog_uchun),
    path('blog', blog, name='blog'),
    path('about', about_me),
    path('portfolio', portfolio)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

