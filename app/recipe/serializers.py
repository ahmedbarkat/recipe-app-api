from rest_framework import serializers
from core.models import Reciepe

class RecipeSerializer(serializers.ModelSerializer):
   #
    class  Meta:
        model = Reciepe
        fields = [  "title", "price"]
 


class RecipeDetailSeralizer(RecipeSerializer):
   # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta: 
       model = Reciepe   
       fields = RecipeSerializer.Meta.fields+ ['description']


 
