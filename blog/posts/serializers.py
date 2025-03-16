from rest_framework import serializers
from .models import Topic, Category, Post


class TopicSerializer(serializers.Serializer):

    # pole tylko do odczytu, tutaj dla id działa też autoincrement
    id = serializers.IntegerField(read_only=True)

    # pola wymagane
    name = serializers.CharField(required=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    # i pozostałe pola
    created = serializers.DateTimeField()

    # przesłonięcie metody create() z klasy serializers.Serializer
    def create(self, validated_data):
        return Topic.objects.create(**validated_data)

    # przesłonięcie metody update() z klasy serializers.Serializer
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
    

class TopicModelSerializer(serializers.ModelSerializer):
    class Meta:
        # musimy wskazać klasę modelu
        model = Topic
        # definiując poniższe pole możemy określić listę właściwości modelu,
        # które chcemy serializować
        fields = ['id', 'name', 'created', 'category']
        # definicja pola modelu tylko do odczytu
        read_only_fields = ['id']


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'topic', 'created_at', 'modified_at', 'created_by', 'content']
        read_only_fields = ['id']

