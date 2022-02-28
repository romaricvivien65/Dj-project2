from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, PostEditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def V_like_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked =  False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('L_article_details', args=[str(pk)]))


class CV_home(ListView):
    model = Post
    template_name = 'blog/T_home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CV_home, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context



def V_categorie_liste(request):
    cat_list = Category.objects.all()
    return render(request, 'blog/T_categorie_liste.html', {'TPL_cat_list': cat_list})


def V_categorie_article_liste(request, cats):
    category_post = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'blog/T_categorie_article_liste.html', {'TPL_cats': cats.title().replace('-', ' '), 'TPL_category_post': category_post})




class CV_article_details(DetailView):
    model = Post
    template_name = 'blog/T_article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CV_article_details, self).get_context_data(*args, **kwargs)


        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class CV_article_create(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/T_article_add.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CV_article_create, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
   
    
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/T_add_comment.html'
    # fields = '__all__'
    success_url = reverse_lazy('L_home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)




class CV_categorie_create(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'blog/T_categorie_add.html'
    fields = '__all__'
    # fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CV_categorie_create, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class CV_article_update(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'blog/T_article_update.html'
    # fields = ['title', 'title_tag', 'body']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CV_article_update, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class CV_article_delete(DeleteView):
    model = Post
    template_name = 'blog/T_article_delete.html'
    success_url = reverse_lazy('L_home')

    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CV_article_delete, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
