from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .movieserializer import MovieSerializer, DirectorSerializer, ReviewSerializer
from .models import Movie, Director, Review


@api_view(['GET', 'POST'])
def test_api(request):
    return Response()

@api_view(['GET'])
def movie_list_api_movies_view(request):
    products = Movie.objects.all()
    serializer = MovieSerializer(products, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        product = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'detail': 'movie is not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(product, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_list_api_directors_view(request):
    products = Movie.objects.all()
    serializer = MovieSerializer(products, many=True)
    return Response(data=serializer.data)



@api_view(['GET'])
def directors_detail_api_view(request, id):
    try:
        product = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'detail': 'director is not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(product, many=False)
    return Response(data=serializer.data)





@api_view(['GET'])
def movie_list_api_reviews_view(request):
    products = Review.objects.all()
    serializer = ReviewSerializer(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        product = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'detail': 'comment is  not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(product, many=False)
    return Response(data=serializer.data)
