from django.shortcuts import redirect, render
from .models import Role

# Create your views here.
def index(request):
    search_query = request.GET.get('q', '')
    if search_query:
        role = Role.objects.filter(role_name__icontains=search_query)
    else:
        role = Role.objects.all()
    
    context = {
        'roles': role,
    }
    return render(request, 'index.html', context)

def create_role(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        
        dept =Role.objects.create(role_name = name,description = description)
        dept.save()
        return redirect('index')
    return render(request,'create_role.html')

def update_role(request,id):
    role = Role.objects.get(role_id = id)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        role = Role.objects.filter(role_id = id).update(role_name = name,description = description)
        return redirect('index')
    context = {
        'roles':role
    }
    return render(request,'update_role.html',context)

def delete_role(request,id):
    role = Role.objects.get(role_id = id)
    var = request.GET.get('q')
    if var == "0":
        
        role.status = False
    else:
        role.status = True
    
    role.save()
    return redirect('index')