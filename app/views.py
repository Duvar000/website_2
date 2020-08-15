from django.shortcuts import render
from django.views.generic import DetailView , ListView
from .models import blog
# Create your views here.
def main(request):
    qs = blog.objects.all()
    search = request.GET.get("form")

    if search != "" and search is not None:
        qs = qs.filter(name__icontains = search)
 
    context = {
        "queryset": qs
    }
    return render(request , "main.html" , context)
    
class blog_main(DetailView):
    model = blog
    template_name = "blog.html"

    # def main(request):
    # qs = blog.objects.all()
    # search = request.GET.get("form")

    # if search != "" and search is not None:
    #     qs = qs.filter(name__icontains = search)
 
    # context = {
    #     "queryset": qs
    # }
    # return render(request , "main.html" , context)