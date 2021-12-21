from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'nilay/post_list.html', {})