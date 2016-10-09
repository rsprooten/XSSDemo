import re

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .models import levelEen, levelTwee, levelDrie, levelVier


class IndexView(TemplateView):
    template_name = "index.html"

class LevelEenReset(View):
    model = levelEen

    def get(self, request, *args, **kwargs):
        toDelete = self.model.objects.filter(host=request.META['HTTP_HOST'])
        for i in toDelete:
            i.delete()
        return redirect('opdrachteen')


class LevelEenView(CreateView):
    model = levelEen
    template_name = "een.html"
    success_url = reverse_lazy('opdrachteen')
    fields = ['naam', 'bericht']

    def get_context_data(self, **kwargs):
        context = super(LevelEenView, self).get_context_data(**kwargs)
        context['objects'] = levelEen.objects.filter(host=self.request.META['HTTP_HOST'])
        return context


    def form_valid(self, form):
        form.instance.host = self.request.META['HTTP_HOST']
        return super(LevelEenView, self).form_valid(form)


class LevelTweeReset(View):
    model = levelTwee

    def get(self, request, *args, **kwargs):
        toDelete = self.model.objects.filter(host=request.META['HTTP_HOST'])
        for i in toDelete:
            i.delete()
        return redirect('opdrachttwee')


class LevelTweeView(CreateView):
    model = levelTwee
    template_name = "twee.html"
    success_url = reverse_lazy('opdrachttwee')
    fields = ['naam', 'bericht']

    def get_context_data(self, **kwargs):
        context = super(LevelTweeView, self).get_context_data(**kwargs)
        context['objects'] = levelTwee.objects.filter(host=self.request.META['HTTP_HOST'])
        return context


    def form_valid(self, form):
        form.instance.host = self.request.META['HTTP_HOST']
        form.instance.naam = form.instance.naam.replace("<script>", "").replace("</script>", "")
        form.instance.bericht = form.instance.bericht.replace("<script>", "").replace("</script>", "")
        return super(LevelTweeView, self).form_valid(form)


class LevelDrieReset(View):
    model = levelDrie

    def get(self, request, *args, **kwargs):
        toDelete = self.model.objects.filter(host=request.META['HTTP_HOST'])
        for i in toDelete:
            i.delete()
        return redirect('opdrachtdrie')


class LevelDrieView(CreateView):
    model = levelDrie
    template_name = "drie.html"
    success_url = reverse_lazy('opdrachtdrie')
    fields = ['naam', 'bericht']

    def _clean_string(self, string):
        return re.sub("(?i)[<]*[/]*script>","", string)

    def get_context_data(self, **kwargs):
        context = super(LevelDrieView, self).get_context_data(**kwargs)
        context['objects'] = levelDrie.objects.filter(host=self.request.META['HTTP_HOST'])
        return context

    def form_valid(self, form):
        form.instance.host = self.request.META['HTTP_HOST']
        naam = form.instance.naam
        bericht = form.instance.bericht
        form.instance.naam = self._clean_string(naam)
        form.instance.bericht = self._clean_string(bericht)
        return super(LevelDrieView, self).form_valid(form)


class LevelVierReset(View):
    model = levelVier

    def get(self, request, *args, **kwargs):
        toDelete = self.model.objects.filter(host=request.META['HTTP_HOST'])
        for i in toDelete:
            i.delete()
        return redirect('opdrachtvier')


class LevelVierView(CreateView):
    model = levelVier
    template_name = "vier.html"
    success_url = reverse_lazy('opdrachtvier')
    fields = ['naam', 'bericht']

    def _clean_string(self, string):
        return re.sub("(?i)[<]*[/]*script>", "", string)

    def get_context_data(self, **kwargs):
        context = super(LevelVierView, self).get_context_data(**kwargs)
        context['objects'] = levelVier.objects.filter(host=self.request.META['HTTP_HOST'])
        return context

    def form_valid(self, form):
        form.instance.host = self.request.META['HTTP_HOST']
        naam = form.instance.naam
        bericht = form.instance.bericht
        form.instance.naam = self._clean_string(naam).upper()
        form.instance.bericht = self._clean_string(bericht)
        return super(LevelVierView, self).form_valid(form)