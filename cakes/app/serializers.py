from rest_framework import serializers

from .models import Cakes,Category,Shape,Weight

class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category

        fields = '__all__'


    
class ShapeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Shape

        fields = '__all__'


    
class WeightSerializer(serializers.ModelSerializer):

    class Meta:

        model = Weight

        fields = '__all__'

# 


class categoryfield(serializers.PrimaryKeyRelatedField):

    def get_attribute(self, instance):

        return getattr(instance,self.source_attr[0])

    def to_representation(self, value):

        return CategorySerializer(value).data
    
                       
class shapefield(serializers.PrimaryKeyRelatedField):

    def get_attribute(self, instance):

        return getattr(instance,self.source_attr[0])

    def to_representation(self, value):

        return ShapeSerializer(value).data
    

class weightfield(serializers.PrimaryKeyRelatedField):

    def get_attribute(self, instance):

        return getattr(instance,self.source_attr[0])

    def to_representation(self, value):

        return WeightSerializer(value).data


    
    
class CakeSerializer(serializers.ModelSerializer):

    category = categoryfield(queryset=Category.objects.all())

    shape = shapefield(queryset=Shape.objects.all())

    weight = weightfield(queryset=Weight.objects.all())

    status = serializers.SerializerMethodField()

    def get_status (self,obj):

        if obj.price < 1000 :

            return 'max server'

        return None

    



    class Meta:

        model = Cakes

        # fields = ['name','description','photo']
        fields = '__all__'
        # exclude = ''