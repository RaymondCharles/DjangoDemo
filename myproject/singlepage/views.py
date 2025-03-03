from django.shortcuts import render

# Create your views here.
def home(request):
    # We will render a single HTML template
    return render(request, 'singlepage/home.html')