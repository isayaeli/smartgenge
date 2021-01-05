from django.shortcuts import render
from about.models import Testimonial, About_Us
# Create your views here.
def about(request):
	testimon = Testimonial.objects.all()
	about = About_Us.objects.all()
	context = {
		'testimon':testimon,
		'about':about
	}
	return render(request, 'about/about.html', context)

