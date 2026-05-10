from rest_framework import viewsets
from .serializers import WordSerializer
from rest_framework.decorators import action
from random import sample
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# from rest_framework_api_key.permissions import HasAPIKey
from .models import Word
from rest_framework.permissions import AllowAny
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework_api_key.permissions import HasAPIKey

class ReadOnlyOrHasAPIKey(BasePermission):

    def has_permission(self, request, view):

        # Public read access
        if request.method in SAFE_METHODS:
            return True

        # Protected write access
        return HasAPIKey().has_permission(request, view)

class WordViewSet(viewsets.ModelViewSet):
    # queryset = Word.objects.all()
    queryset = Word.objects.filter(is_approved=True).order_by('tamil_word')
    serializer_class = WordSerializer
    permission_classes = [ReadOnlyOrHasAPIKey]


    @action(detail=False, methods=['get'])
    def random(self, request):
        count = int(request.GET.get('count', 10))  # default 10 words
        all_ids = list(Word.objects.values_list('id', flat=True))
        if len(all_ids) == 0:
            return Response([])
        random_ids = sample(all_ids, min(count, len(all_ids)))
        words = Word.objects.filter(id__in=random_ids)
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)


    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.GET.get('q', '').strip()

        if not query:
            return Response([])

        results = Word.objects.filter( tamil_word__istartswith=query)[:15]  # limit to 15 suggestions
        serializer = WordSerializer(results, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([ReadOnlyOrHasAPIKey])
def export_words_json(request):
    words = Word.objects.all().values(
        'id',
        'tamil_word',
        'arabic_word',
        'category',
        'example_sentence'
    )

    return Response(list(words))