from rest_framework import viewsets
from .models import Word
from .serializers import WordSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from random import sample

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

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

