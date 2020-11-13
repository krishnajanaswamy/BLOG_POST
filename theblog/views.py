from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,  DetailView, CreateView, UpdateView,DeleteView
from .models import Post, Comment
from .forms import PostForm, EditForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.db.models import Count


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post.id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
     model = Post
     template_name = 'home.html'
     ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comments.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')
    #fields = '__all__'



class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title','body')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ('title','title_tag','body')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



