from rest_framework import serializers




class StudentSerializer(models.ModelSerializer)
    class Meta:
        model = Student
        fields='_all_'