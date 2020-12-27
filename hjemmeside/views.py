from django.shortcuts import render
from django.views.generic import TemplateView
from hjemmeside.models import HjemmeSideInfoModel

# Create your views here.
class HomepageView(TemplateView):
    template_name = "hjemmeside/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        userinput = HjemmeSideInfoModel.objects.get(pk=1)
        context.update({
            'userinput':userinput,
            })
        return context
