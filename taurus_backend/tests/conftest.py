# import pytest
#
# from operations.serializers import UserSerializer
#
#
# @pytest.fixture
# def user():
#
#     user_dict = dict(
#         first_name="Mario",
#         last_name="Rossi",
#         email="mario.rossi@gmail.com",
#         password="hciusdyt736873gdshgsd73",
#         address="Viale Italia, 1, Modena",
#         cellphone_number="371897446"
#     )
#     serializer = UserSerializer(data=user_dict)
#     if serializer.is_valid():
#         serializer.save()
#         serializer.save()
#         return serializer.data
#     else:
#         return None