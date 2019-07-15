from django.views.generic import ListView

from project.apps.blog.models import Article


class ArticleListView(ListView):
    queryset = Article.objects.order_by('-created_at')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _, page, _, _ = self.paginate_queryset(
            ArticleListView.queryset,
            ArticleListView.paginate_by,
        )
        context['page'] = page

        return context
