from django.shortcuts import render, redirect, get_object_or_404
#DVDH
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    # comments = Comment.objects.filter(article_id = article_pk)
    # 1은 N을 보장할 수 없기 때문에 querySet(comment_set)형태로 조회 해야한다.
    comments = article.comment_set.all()
    context = {
        'article' : article,
        'comment_form' : comment_form,
        'comments' : comments
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)

@require_POST
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        # comment.article_id = article.pk
        comment.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {
            'comment_form' : comment_form,
            'article' : article
        }
    return redirect('articles:detail', context)

@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
    