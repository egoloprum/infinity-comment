from django.shortcuts import render, redirect
from .models import Comment

# Create your views here.

def main(request):
    comments = Comment.objects.all().order_by('created_at')

    if request.method == 'POST':
      if request.POST.get('comment') is not None:
        comment = Comment.objects.create(
            body=request.POST.get('comment')
        )
        return redirect('main')

      if request.POST.get('reply-comment') is not None:
        par = request.POST.get('parent-comment')
        par = Comment.objects.get(pk=par)
        comment = Comment.objects.create(
            parent=par,
            body=request.POST.get('reply-comment')
        )
        return redirect('main')
            
    context = {'comments':comments}

    return render(request, 'main.html', context)

