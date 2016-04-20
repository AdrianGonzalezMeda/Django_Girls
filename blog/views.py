from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

import json

from .models import Post, Comment
from .forms import CommentForm


# Create your views here.

class LoginRequiredMixin(object): #Es como el decorador de login_required
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='login')


#def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'blog/post_list.html', {'posts' : posts}) #Lo que pasas como contexto tienes que recogerlo luego en el html con el mismo nombre que lo que pones entre comillas
class PostList(ListView):
    model = Post #hace un queryset y llama a Post.objects.all() por defecto, por eso si definimos el queryset no lo tenemos que poner
    #context_object_name = 'posts' #Puedes poner esta variable, o la funcion de abajo, son equivalentes, pero tener ambas es redundante. 
    #template_name = 'blog/post_list.html' no es necesario por que por defecto te busca un archivo de esta manera: <app>/<model>_list.html, en nuestro caso post_list.html
    def get_queryset(self): #Si no sobreescribes este metodo, por defecto esta hecho para que solo se haga en cada refresco del servidor, por eso no mostraba los post nuevos hasta que refrescabas.
        queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return queryset
    #Esta se podria si quisierasfiltar los resultados que te da, pero puedes ahorrartelo usando los query sets
    #def get_context_data(self, **kwargs): #llama a la calse padre para recibir un contexo
        # Call the base implementation first to get a context
    #    context = super(post_list, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
    #    context['post'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #    return context


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = Comment.objects.filter(post=post).order_by('created_date')

#     if request.method == "POST":
#         form = CommentForm(request.POST)

#         if form.is_valid():
#                 comment = form.save(commit = False)#Variable distinta a la de arriba
#                 comment.author = request.user
#                 comment.post = post #Lo iguala al post que recogemos arriba, que va a ser uno solo
#                 comment.save()
#                 return redirect('post_detail', pk=post.pk)

#     else:
#         form = CommentForm()

#     return render(request, 'blog/post_detail.html', {'post' : post,
#                                                     'comments' : comments,
#                                                     'form' : form})
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['comments'] = Comment.objects.filter(post=self.object).order_by('created_date') #Filtra que salgan los comentarios del post en el que estan referenciados
        context['form'] = CommentForm
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post = self.get_object() #es el objeto de la calse post detail

        if form.is_valid():
            comment = form.save(commit = False)#Variable distinta a la de arriba
            comment.author = request.user
            comment.post = post #Lo iguala al post que recogemos arriba, que va a ser uno solo
            comment.save()
            return redirect('post_detail', pk=post.pk)


#@login_required(login_url='login') #decorador
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)

#         if form.is_valid():
#             post = form.save(commit = False)#Esto simplemente te lo guarda en una variable antes de "subirlo" por que antes queremos anadirle el autor y eso.
#             post.author = request.user
#             post.publish()#metodo propio, lo publica y le pone fecha de publicacion
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form' : form})
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text'] #Con definir esto ya no te hace falta crear los formularios
    template_name = 'blog/post_edit.html'
    #success_url = '/' Como no puedes poner equi el nombre de 'post_list' por que no hace bien la busqueda inversa, tienes que reescribir la funcion

    def form_valid(self, form):
        form.post = form.instance
        form.post.author = self.request.user
        form.post.published_date = timezone.now() #Si no le das fecha de publicacion no te apareceran luego en el post list
        return super(PostCreate, self).form_valid(form) #Esto hace el save() por defecto
        #ha habido que crear la funcion get_queryset en el class de post_list por que daba fallo con el filtrer

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk}) #reverse hace la busqueda inversa de urls

# @login_required(login_url='login')
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)

#         if form.is_valid():
#             post = form.save(commit = False)
#             post.author = request.user
#             post.publish()
#             return redirect('blog.views.post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form' : form, 'post' : post})
class PostEdit(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blog/post_edit.html'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk}) #reverse hace la busqueda inversa de urls

# @login_required(login_url='login')
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.delete() #Te borra automaticamente los comentarios, por que estan referenciados a un post en concreto.
#     return redirect('post_list')

class PostDelete(LoginRequiredMixin, DeleteView): #Losmixins van primero
    model = Post
    
    def get_success_url(self):
        return reverse('post_list')

    

def comment_like(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.like()

    response_data = { 'response_text_contador' : comment.likes}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )

def comment_dislike(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.dislike()

    response_data = { 'response_text_contador' : comment.dislikes}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )