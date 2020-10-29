from django.views import generic, View
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Post
from .forms import PostCreateForm
from reply.forms import ReplyCreateForm


class PostListView(LoginRequiredMixin, generic.ListView):
    queryset = Post.objects.filter(is_published=True)
    template_name = 'index.html'


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'new_post.html'
    form_class = PostCreateForm

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse_lazy('post_detail', args=[post.id]))
        return render(request, 'new_post.html', {'form': form})


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    form_class = ReplyCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_posts'] = Post.objects.filter(is_published=True)
        context['replies'] = self.object.replies.all()
        context['form'] = self.get_form()
        return context

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.post = self.object
            new_reply.save()
            return self.form_valid(form)
        else:
            form = self.get_form()
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post = self.object
        form.save()
        return super().form_valid(form)


class PostUpdateView(generic.UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_update.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
