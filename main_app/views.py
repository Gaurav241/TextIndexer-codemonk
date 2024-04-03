from rest_framework.views import APIView
from .serializers import UserSerializer, ParagraphSerializer
from .models import User, Paragraph, WordIndex
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import ParagraphSerializer


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter(
            name='word',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description='The word to search for in paragraphs',
            required=True,
        ),
    ],
    responses={200: ParagraphSerializer(many=True)},
)
@api_view(['GET'])
@renderer_classes([JSONRenderer])
def search_word(request):
    """
    Search for paragraphs containing a specific word.
    """
    # Extract the word from the query parameters
    word = request.query_params.get('word')
    if word:
        # Query WordIndex for paragraphs containing the specified word
        word_indices = WordIndex.objects.filter(word=word.lower()).order_by('-frequency')[:10]
        paragraph_ids = [wi.paragraph.id for wi in word_indices]
        paragraphs = Paragraph.objects.filter(id__in=paragraph_ids)
        serializer = ParagraphSerializer(paragraphs, many=True)
        return Response(serializer.data)
    return Response({'message': 'No word provided'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=['GET'],
    responses={200: openapi.Response("List of users", UserSerializer(many=True))},
)
@swagger_auto_schema(
    methods=['POST'],
    request_body=UserSerializer,
    responses={201: openapi.Response("Created user", UserSerializer)},
)
@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
def user_list(request):
    """
    List all users or create a new user.
    """
    if request.method == 'GET':
        # Retrieve all users from the database
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new user with data from request
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParagraphList(APIView):
    @swagger_auto_schema(
        operation_description="List all paragraphs",
        responses={200: openapi.Response("List of paragraphs", ParagraphSerializer(many=True))},
    )
    def get(self, request, format=None):
        """
        List all paragraphs.
        """
        paragraphs = Paragraph.objects.all()
        serializer = ParagraphSerializer(paragraphs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new paragraph and process its content",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'content': openapi.Schema(type=openapi.TYPE_STRING),
                # Add more properties as needed
            },
            required=['content'],
        ),
        responses={201: openapi.Response("Created paragraph", ParagraphSerializer)},
    )
    def post(self, request, format=None):
        """
        Create a new paragraph and process its content.
        """
        serializer = ParagraphSerializer(data=request.data)
        if serializer.is_valid():
            para_obj = serializer.save()

            # Process words in the paragraph
            paragraph = request.data.get('content', '').lower()
            words = paragraph.split()
            for word in set(words):
                frequency = words.count(word)
                WordIndex.objects.create(word=word, paragraph=para_obj, frequency=frequency)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
