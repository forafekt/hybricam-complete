from django.conf.urls import url

from .views import (
    ArticlesListView,
    DraftsListView,
    DetailArticleView,
)
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "articles"
urlpatterns = [
    url(r"^$", ArticlesListView.as_view(), name="list"),
    url(r"^drafts/$", DraftsListView.as_view(), name="drafts"),
    url(r"^(?P<pk>[-\w]+)/$", DetailArticleView.as_view(), name="article"),
]
urlpatterns = format_suffix_patterns(urlpatterns)