from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('portfolio/', views.portfolio, name="portfolio"),
	path('portfolio/<str:pk>', views.portfolio_detail, name="portfolio_detail"),
	path('blog/', views.blog, name="blog"),
	path('blog/<str:pk>', views.BlogDetailView.as_view(), name="blog_detail"),
	]