from rest_framework import viewsets, filters
from .models import Todo
from .serializers import TodoSerializer
from django_filters import rest_framework as filters
import operator
from functools import reduce
from django.db.models import Q

class MultiValueCharFilter(filters.BaseCSVFilter, filters.CharFilter):
 
    def filter(self, qs, value):
        expr = reduce(
            operator.or_,
            (Q(**{f'{self.field_name}__{self.lookup_expr}': v}) for v in value)
        )
        return qs.filter(expr)

class CustomFilter(filters.FilterSet):
    # フィルタ定義
    deadline = filters.DateTimeFilter(field_name='deadline', lookup_expr='lte')
    create_user = filters.CharFilter(field_name='create_user', lookup_expr='exact')
    status = MultiValueCharFilter(field_name='status')

    class Meta:
        model = Todo
        fields = ['deadline', 'create_user', 'status'] #定義したフィルタを列挙

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_class = CustomFilter