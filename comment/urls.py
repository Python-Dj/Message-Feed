from django.urls import path
from . import views



urlpatterns = [
    path("login/", views.login, name="login"),
    path("signUp/", views.signUp, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("feed/", views.news_messages, name="feed"),
    path("comment/<int:pk>", views.comment, name="comment"),
    path("deleteMsg/<int:pk>", views.delete_message, name="delete-message"),
    path("cmtLikes/<int:pk>/", views.comment_likes, name="comment-likes"),
    path("msgLikes/<int:pk>/", views.message_likes, name="message-likes")
]
