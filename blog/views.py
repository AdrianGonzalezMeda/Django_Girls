from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts}) #Lo que pasas como contexto tienes que recogerlo luego en el html con el mismo nombre que lo que pones entre comillas

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('created_date')

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit = False)#Variable distinta a la de arriba
            comment.author = request.user
            comment.post = post #Lo iguala al post que recogemos arriba, que va a ser uno solo
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post' : post,
                                                    'comments' : comments,
                                                    'form' : form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit = False)#Esto simplemente te lo guarda en una variable antes de "subirlo" por que antes queremos anadirle el autor y eso.
            post.author = request.user
            post.publish()#metodo propio, lo publica y le pone fecha de publicacion
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form' : form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.publish()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form' : form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete() #Te borra automaticamente los comentarios, por que estan referenciados a un post en concreto.
    return redirect('post_list')