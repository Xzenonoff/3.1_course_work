from django.views.generic import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'
