from django.shortcuts import render
from hierarchical_data_app.models import File


# Create your views here.
def show_files(request):
    return render(request, 'files.html', {'files': File.objects.all()})
