from django.urls import include, path, re_path
from django.views.decorators.cache import cache_page

from women.views import *

urlpatterns = [
    path('', (WomenHome.as_view()), name='home'),
    path('about/', about, name='about'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('feedback/', feedback, name='feedback'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),

]

'''path('categs/<int:categid>/', categories),  # <str> - любая непустая строка, не вкл знак /
    # <slug> - ascii , дефис и подчеркивание   #<uuid> - цифры, малые латинские символы , дефис
    # <path> - любая непустая строка, включая /
    # если таких шаблонов недостаточно,  то используется re_path:
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),'''


