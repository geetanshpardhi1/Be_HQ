from django.shortcuts import render
from .models import Resume,Project
# Create your views here.
def home(request):
    projects = Project.objects.all()
    resume = Resume.objects.order_by('-pk').first()
    return render(request,'myapp/home.html',{'resume':resume,'projects':projects})