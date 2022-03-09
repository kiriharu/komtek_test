from rest_framework import serializers
from .models import Directory, DirectoryVersion


class DirectoryVersionSerializer(serializers.ModelSerializer):
    """ Сериализатор версий каталогов """
    class Meta:
        model = DirectoryVersion
        fields = ("version", "start_date", )


class DirectorySerializer(serializers.ModelSerializer):
    """ Сериализатор каталогов """

    versions = DirectoryVersionSerializer(many=True, read_only=True)

    class Meta:
        model = Directory
        fields = ("id", "name", "short_name", "description", "versions", )
