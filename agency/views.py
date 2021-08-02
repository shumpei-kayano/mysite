from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
import logging

from django.urls import reverse_lazy

from django.shortcuts import render
# genericの読み込みで使用できるようにする
from django.views import generic
# 問い合わせページInquiryFormの読み込み
from.forms import InquiryForm
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