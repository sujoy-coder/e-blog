from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post, Comment

# function based view - home
# def home(request):
#     posts = Post.objects.all().order_by('-date_posted')
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'blog/home.html', context)


# class based view - home
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})


@login_required(login_url='/accounts/login/')
def profile(request):
    posts = Post.objects.filter(user=request.user).order_by('-date_posted')
    context = {
        'title': 'Profile',
        'posts': posts,
    }
    return render(request, 'blog/profile.html', context)


@login_required(login_url='/accounts/login/')
def create_post(request):
    if request.method == 'POST':
        try:
            title = request.POST['title']
            desc = request.POST['desc']
            new_post = Post(title=title, desc=desc, user=request.user)
            new_post.save()
            messages.success(request, 'Your post is saved !')
            return redirect('profile')
        except:
            messages.error(request, 'Some error occurs, Unable to save your post !')
            return redirect('new_post')
    return render(request, 'blog/new_post.html', {'title': 'New Post'})


@login_required(login_url='/accounts/login/')
def comment(request, post_id):
    if request.method == 'POST':
        msg = request.POST['comment_msg']
        new_comment = Comment(msg=msg, user=request.user, post_id=int(post_id))
        new_comment.save()
        messages.success(request, 'Your comment is saved !')
        return redirect('comment', post_id=post_id)    
    try:
        post = Post.objects.get(id=int(post_id))
        comments = Comment.objects.filter(post__pk=int(post_id)).order_by('-date_commented')
        context = {'title': 'Add Comment',
                  'post': post, 
                  'comments': comments
            }
        return render(request, 'blog/comment.html', context)
    except Exception as e:
        print(e)
        messages.warning(request, 'Some error occurs !')
        return redirect('home')