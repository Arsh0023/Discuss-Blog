from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path(r'about/',views.AboutView.as_view() ,name='about'),
    path(r'post/<int:pk>/',views.PostDetailView.as_view(),name = 'post_detail'),
    path(r'',views.PostListView.as_view(),name = 'post_list'),
    path(r'post/new/',views.PostCreateView.as_view(),name='post'),
    path(r'post/<int:pk>/edit/',views.PostUpdateView.as_view(),name = 'post_update'),
    path(r'post/<int:pk>/delete/',views.PostDeleteView.as_view(),name = 'post_delete'),
    path(r'post/drafts/',views.DraftListView.as_view(),name = 'draft_list_view'),
    path(r'post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path(r'post/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path(r'post/<int:pk>/remove/',views.comment_remove, name='comment_remove'),
    path(r'post/<int:pk>/publish/',views.post_publish,name='post_publish'),
]