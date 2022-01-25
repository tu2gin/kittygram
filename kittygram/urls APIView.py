# from django.urls import include, path

# from cats.views import cat_list

# urlpatterns = [
#    path('cats/', cat_list),
# ]



# Чтобы всё заработало, исправьте код в urls.py, ведь синтаксис 
# вызова view-классов отличается от синтаксиса вызова view-функций.

# urls.py
from django.urls import include, path

from cats.views import APICat

urlpatterns = [
    path('cats/', APICat.as_view()),
] 
