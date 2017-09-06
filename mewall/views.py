from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'mewall/post_list.html', {'posts': posts})


def about(request):
    return render(request, 'mewall/about.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mewall/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":  # as a POST dict
        # we know the user hit 'submit'
        # alternative to using: if request.method == 'POST':
        # can just use form = PostForm(data=request.POST or None)
        form = PostForm(data=request.POST)
        # check validation
        if form.is_valid():
            # if the user submitted the form and the form is valid
            post = form.save(commit=False)        # create new instance of PostForm
            post.published_date = timezone.now()  # manually create the published date and time
            post.save()                           # save PostForm instance
            # redirect to a page to display a completed form
            return redirect('post_detail', pk=post.pk)
    else:  # elif method == 'Get':
        form = PostForm()

    context = {'form': form}
    return render(request, 'mewall/post_edit.html', context)


def post_image(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'mewall/post_image.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'mewall/post_edit.html', {'form': form, 'post': post})
