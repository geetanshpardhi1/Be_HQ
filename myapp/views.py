from django.shortcuts import render
from .models import Resume,Project
# Create your views here.
def home(request):
    projects = Project.objects.all()
    resume = Resume.objects.get(pk=1)
    return render(request,'myapp/home.html',{'resume':resume,'projects':projects})