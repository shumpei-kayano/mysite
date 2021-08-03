from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
import logging

from django.urls import reverse_lazy

from django.shortcuts import render
# genericの読み込みで使用できるようにする
from django.views import generic
# 問い合わせページInquiryFormの読み込み
from.forms import InquiryForm, DiaryCreateForm
from .models import Diary
from django.contrib import messages

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"
# 自分で定義したIndexViewに引数でgenericのTenplateViewクラスを渡している。
# as_view()メソッドはTemplateViewクラス内で定義されている。

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('agency:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class TeamView(generic.TemplateView):
    template_name = "team.html"

class ServicesView(generic.TemplateView):
    template_name = "services.html"

class PhotosView(generic.TemplateView):
    template_name = "photos.html"

class AboutView(generic.TemplateView):
    template_name = "about.html"

class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries

class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'

class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('agency:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '投稿を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "投稿の作成に失敗しました。")
        return super().form_invalid(form)

class DiaryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Diary
    template_name = 'diary_update.html'
    form_class = DiaryCreateForm

    def get_success_url(self):
        return reverse_lazy('agency:diary_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '投稿を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "投稿の更新に失敗しました。")
        return super().form_invalid(form)

class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('agency:diary_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "投稿を削除しました。")
        return super().delete(request, *args, **kwargs)
