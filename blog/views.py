from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Post
from django.urls import reverse_lazy


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html"
    paginate_by = 10


class PostCreateView(generic.CreateView):
    model = Post
    template_name = "blog/new_post.html"
    fields = [
        'title', 'slug', 'author', 'image', 'excerpt', 'content', 'status'
    ]


class UpdatePostView(generic.UpdateView):
    model = Post
    template_name = "blog/update_post.html"
    fields = [
        'title', 'slug', 'author', 'image', 'excerpt', 'content', 'status'
    ]


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('home')
    fields = [
        'title', 'slug', 'author', 'image', 'excerpt', 'content', 'status'
    ]


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
            },
        )
