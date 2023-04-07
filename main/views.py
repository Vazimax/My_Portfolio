from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate
	)

from django.views import generic


from .forms import ContactForm


def home(request):
	certificates = Certificate.objects.filter(is_active=True)
	blogs = Blog.objects.filter(is_active=True)
	portfolio = Portfolio.objects.filter(is_active=True)#
	user = UserProfile.objects.all()

	context = {
		'certificates': certificates,
		'blogs': blogs,
		'portfolio': portfolio,
		'profile':user,
	}

	return render(request,'index.html',context)


class ContactView(generic.FormView):
	template_name = "contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


def portfolio(request):
	portfolios = Portfolio.objects.filter(is_active=True)
	context = {
		'portfolios': portfolios,
		'title': 'Portfolio',
	}

	return render(request,'portfolio.html',context)


def portfolio_detail(request,pk):
    portfolio = Portfolio.objects.get(id=pk)

    context = {
        'portfolio': portfolio,
        'title': portfolio.name,
    }

    return render(request, 'portfolio_detail.html', context)

# class BlogView(generic.ListView):
# 	model = Blog
# 	template_name = "blog.html"
# 	paginate_by = 10
	
# 	def get_queryset(self):
# 		return super().get_queryset().filter(is_active=True)

def blog(request):
	blogs = Blog.objects.all()

	context = {
		'blogs':blogs,
		'title': "Blog"
	}


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "blog-detail.html"