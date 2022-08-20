from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profile_api import serializers
from profile_api import models
from profile_api import permissions




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





class HelloViewSet(viewsets.ViewSet):
    """test api view"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""

        a_viewset = [
            'uses action (lists , create ,retrieve, update, partial_update)',
            'automatically maps to urls using routers',
            'provides more functionlity with less code',
            ]
        return Response({'message':'Hello!' , 'a_viewset':a_viewset})



    def create(self , request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!!'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve (self ,request ,pk=None):
        """Handle getting a object by its Id"""
        return Response ({'http_method':'GET'})


    def update(self, request, pk=None):
        """handle updating an option"""
        return Response({'http_method':'PUT'})

    def partial_update (self, request, pk=None):
        """handle updating part of an object"""
        return Response ({'http_method': 'PATCH'})

    def distroy (self, request , pk=None):
        """handle removing an object"""
        return Response({'http_method':'DELETE'})




class UserProfileViewSet(viewsets.ModelViewSet):
    """ handle creating and upadating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset= models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields= ('id','name', 'email',)



class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
