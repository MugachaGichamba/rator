from django.shortcuts import render

# Create your views here.
def home(request):
    # print(Comment.objects.all())
    # context = {
    #     'posts': Post.objects.all()
    # }

    return render(request, "users/home.html")

