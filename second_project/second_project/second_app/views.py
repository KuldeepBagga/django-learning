from django.shortcuts import render
from second_app.models import User
# Create your views here.
def index(request):
    mydict=User.objects.order_by('first_name')
    user_list={"users":mydict}
    return render(request,'second_app/users.html',context=user_list)