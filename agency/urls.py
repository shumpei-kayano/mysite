from django.urls import path

from.import views

app_name = 'agency'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    # 問い合わせページinquiry.htmlへのパス
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('team/',views.TeamView.as_view(),name="team"),
    path('services/',views.ServicesView.as_view(),name="services"),
    path('photos/',views.PhotosView.as_view(),name="photos"),
    path('about/',views.AboutView.as_view(),name="about"),
    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    # path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
    # path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),
    # path('diary-update/<int:pk>/', views.DiaryUpdateView.as_view(), name="diary_update"),
    # path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
]