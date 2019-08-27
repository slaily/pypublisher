from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from project.apps.blog.models import Article
from project.apps.blog.forms import ContactForm


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


class ArticleDetailView(DetailView):
    model = Article


class ContactView(FormView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.send_email()

        return super().form_valid(form)
