
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    
    path('playfounds/', views.playfounds_index, name='playfounds-index'),  
    path('playfounds/<int:pk>/', views.playfound_detail, name='playfounds-detail'),  
    path('playfounds/create/', views.PlayFoundCreate.as_view(), name='playfounds-create'),  
    path('playfounds/<int:pk>/update/', views.PlayFoundUpdate.as_view(), name='playfound-update'),  
    path('playfounds/<int:pk>/delete/', views.PlayFoundDelete.as_view(), name='playfound-delete'),  
    
    path('playfounds/<int:pk>/suggest/', views.SuggestionCreate.as_view(), name='suggestion-create'),
    path('suggestions/<int:pk>/update/', views.SuggestionUpdate.as_view(), name='suggestion-update'),
    path('suggestions/<int:pk>/delete/', views.SuggestionDelete.as_view(), name='suggestion-delete'),

    path('accounts/signup/', views.signup, name='signup'),
]
