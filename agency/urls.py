from django.urls import path

from.import views

app_name = 'agency'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    # 問い合わせページinquiry.htmlへのパス
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('team/',views.TeamView.as_view(),name="team"),
    path('services/',views.ServicesView.as_view(),name="services"),
    path('portfolio/',views.PortfolioView.as_view(),name="portfolio"),
    path('about/',views.AboutView.as_view(),name="about"),
]