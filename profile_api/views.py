from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test api view"""

    def get (self ,request , format=None):
        """return a  list of APIView features"""

        an_apiview= [
            'uses HTTP method as function (get, post , patch, put , delete)',
            'is similar to traditional django view',
            'gives you the most control over application logic',
            'is mapped manually to urls'

        ]


        return Response({'messages':'Hello', 'an_apiview': an_apiview})
