import re
from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    def check_for_special_characters(self, value):
        special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if special_chars.search(value):
            raise serializers.ValidationError(
                "should not contain special characters")
        return value

    class Meta:
        model = Company
        fields = "__all__"

    def validate_name(self, name):
        name = self.check_for_special_characters(name)
        return name

    def validate_location(self, location):
        location = self.check_for_special_characters(location)
        return location

    def validate_about(self, about):
        about = self.check_for_special_characters(about)
        return about

    def validate_type(self, type):
        type = self.check_for_special_characters(type)
        return type
