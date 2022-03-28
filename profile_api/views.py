from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializers




class HelloApiView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer

    def get (self ,request , format=None):
        """return a  list of APIView features"""

        an_apiview= [
            'uses HTTP method as function (get, post , patch, put , delete)',
            'is similar to traditional django view',
            'gives you the most control over application logic',
            'is mapped manually to urls'

        ]


        return Response({'messages':'Hello', 'an_apiview': an_apiview})




    def post(self, request):
        """create hello message with our name"""
        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name =serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response ({'message':message})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST

            )


    def put(self, request , pk=None):
        """handle updating a object"""
        return Response({'method': 'PUT'})


    def patch(self, request , pk=None):
        """handle partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request , pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})
