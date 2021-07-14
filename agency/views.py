from django.views import generic

import logging

from django.urls import reverse_lazy

from django.shortcuts import render
# genericの読み込みで使用できるようにする
from django.views import generic
# 問い合わせページInquiryFormの読み込み
from.forms import InquiryForm

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

class PortfolioView(generic.TemplateView):
    template_name = "portfolio.html"

class AboutView(generic.TemplateView):
    template_name = "about.html"