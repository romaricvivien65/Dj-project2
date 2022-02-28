from django.urls import path, include
from.views import CV_home, CV_article_details, CV_article_create, CV_article_update, CV_article_delete, CV_categorie_create, V_categorie_article_liste, V_categorie_liste, V_like_post, AddCommentView

urlpatterns = [
    path('', CV_home.as_view(), name="L_home"),
    path('article/<int:pk>', CV_article_details.as_view(),
         name="L_article_details"),
    path('add_post/', CV_article_create.as_view(), name="L_article_create"),
    path('add_category/', CV_categorie_create.as_view(), name="L_categorie_create"),
    path('article/edit/<int:pk>', CV_article_update.as_view(), name="L_article_update"),
    path('article/<int:pk>/remove', CV_article_delete.as_view(), name="L_article_delete"),
    path('category/<str:cats>/', V_categorie_article_liste, name="L_categorie_article_liste"),
    path('category-list/', V_categorie_liste, name="L_categorie_liste"),
    path('like/<int:pk>', V_like_post, name="L_like_post"),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name="L_comment_post"),

]
