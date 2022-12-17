from django.urls import path
from . import views

urlpatterns = [
    #path converters int: numbers, str: strings, slugs: hyphens-and-underscores_stuff, path whole urls, UUID:Universally unique identifier
    path('', views.index, name='index'),
    path('items/', views.ItemIndex.as_view(), name='items_index'),
    path('items/<int:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('items/<int:pk>/vote/', views.VoteItem.as_view(), name='item-vote'),
    path('items/<int:pk>/vote/results', views.ResultsView.as_view(), name='item-results'),
    path('items/create/', views.ItemCreate.as_view(), name='items_create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='items_update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
    path('user/<username>/', views.profile, name='profile'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('items/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
]