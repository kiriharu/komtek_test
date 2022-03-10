from rest_framework import serializers
from .models import Directory, DirectoryVersion, Item


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


class ItemSerializer(serializers.ModelSerializer):

    directory = serializers.IntegerField(source="directory_version.directory.id")
    version = serializers.StringRelatedField(source="directory_version.version")

    class Meta:
        model = Item
        fields = ("id", "parent", "code", "value", "directory", "version")
