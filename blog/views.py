from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment


# Create your views here.
def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        BlogPost.objects.create(title=title, content=content)
        return redirect('post_list')
    return render(request, 'blog/create_post.html')

def edit_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_detail', id=post.id)
    return render(request, 'blog/edit_post.html', {'post': post})

def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/delete_post.html', {'post': post})

def add_comment(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        author = request.POST['author']
        text = request.POST['text']
        Comment.objects.create(post=post, author=author, text=text)
        return redirect('post_detail', id=post.id)
    return render(request, 'blog/add_comment.html', {'post': post})

def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == 'POST':
        comment.text = request.POST['text']
        comment.save()
        return redirect('post_detail', id=comment.post.id)
    return render(request, 'blog/edit_comment.html', {'comment': comment})

def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    post_id = comment.post.id
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', id=post_id)
    return render(request, 'blog/delete_comment.html', {'comment': comment})
