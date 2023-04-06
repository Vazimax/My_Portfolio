from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('portfolio/', views.portfolio, name="portfolio"),
	path('portfolio/<str:pk>', views.portfolio_detail, name="portfolio_detail"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	]