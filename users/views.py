from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    # print(Comment.objects.all())
    # context = {
    #     'posts': Post.objects.all()
    # }

    return render(request, "users/home.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form' : form})