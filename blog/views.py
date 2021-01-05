from django.shortcuts import render, redirect, get_object_or_404, reverse
from blog.models import *
from django.db.models import Q
from blog.forms import commentForm
from django.views.generic import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
def blog(request):
    blogs = Blog.objects.all().order_by('-id')
    qs = request.GET.get('q')
    if qs:
        blogs = Blog.objects.filter(
            Q(title__icontains=qs)|
            Q(user__username=qs)|
            Q(content__icontains=qs)
        ).order_by('-id')
    context = {
        'blogs':blogs
    }
    return render(request,'blog/all_blogs.html', context)

@login_required(login_url='/login')
def single_blog(request, id):
    blog = Blog.objects.get(id=id)
    # comments = BlogComment.objects.filter(blog=blog) ===> this query is an alternative of 
    #(blog.blogcomment_set.all)
    if request.method == 'POST':
        form = commentForm(request.POST or None)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            comment = BlogComment.objects.create(blog=blog, user=request.user, content=content)
            comment.save()
        return redirect('single_blog', id=id)    
    form = commentForm()
    context = {
        'blog':blog,
        'form':form
        # 'comments':comments
    }
    return render(request,'blog/single_blog.html', context)

# def comment_edit(request, id):
#     comment = BlogComment.objects.get(id=id)
#     if request.method == 'POST':
#         form = commentForm(request.POST or None,  instance=comment)
#         if form.is_valid():
#             comment= form.save(commit= False)
#             comment.save()
#         return redirect('single_blog', id=comment.blog.id)
#     form = commentForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'blog/edit_comment.html', context)

class CommentEditView(UserPassesTestMixin, UpdateView):
    model = BlogComment
    template_name = 'blog/edit_comment.html'
    fields = ['content']
    # login_url = '/login/'
    # success_url = '/blogs'

    def form_valid(self, form):
        form.instance.user =self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        comment=self.get_object()
        if self.request.user == comment.user:
            return True
        return False


def comment_delete(request, id):
    comment =get_object_or_404(BlogComment, id=id)
    comment.delete()
    return redirect('single_blog', id=comment.blog.id)





