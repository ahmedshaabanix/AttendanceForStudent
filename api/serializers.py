
from doctor.models import Qr_code
from rest_framework import serializers,exceptions
from doctor.models import Qr_code
from accounts.models import Student
from doctor.models import Qr_code,Attendance
from django.contrib.auth import authenticate



# User Serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = '__all__'

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ('id', 'username', 'email', 'password','department','name',"level")
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = Student.objects.create_student_user( 
                            validated_data['username'],
                            validated_data['email'],
                            validated_data['name'],
                            validated_data['department'],
                            validated_data['level'],
                            validated_data['password']
                            
                            
                            )

    return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField(max_length=128, write_only=True)
#  token = serializers.CharField(max_length=255, read_only=True)

  def validate(self, data):
      username = data.get("username", None)
      password = data.get("password", None)

      if username and password:
          user = authenticate(username=username, password=password)
          if user:
              if user:
                  data["user"] = user
              else:
                  msg = "User is deactivated."
                  raise exceptions.ValidationError(msg)
          else:
              msg = "Unable to login with given credentials."
              raise exceptions.ValidationError(msg)
      else:
        msg = "Must provide username and password both."
        raise exceptions.ValidationError(msg)
      return data


# QR matching Serializers
class Qr_Serializers(serializers.Serializer):
  student_id = serializers.CharField()
  qr_code_text = serializers.CharField()



class Attendance_Serializer(serializers.ModelSerializer):
  class Meta:
    model= Attendance
    fields = '__all__'

    

    

      
