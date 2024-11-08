from rest_framework import serializers
from .models import News

class NewsSeiralizers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"