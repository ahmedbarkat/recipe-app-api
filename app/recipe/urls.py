from rest_framework import routers
 
from django.urls import path, re_path 
from recipe.views import RecipeViewSet


app_name = 'recipe'

router = routers.DefaultRouter()
router.register('recipes', RecipeViewSet)
 

urlpatterns = router.urls
 