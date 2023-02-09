from rest_framework import serializers
from pipelineapi.models import Techie


class TechieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techie
        fields = "__all__"
