from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from .models import ImZacadQ1Bk, ImZacadQ2Bk
from .serializers import Q1Serializer, Q2Serializer
from rest_framework import status
from konlpy.tag import _komoran
from typing import List
from django.core import serializers
import json


class IMView(APIView):
    def post(self, request):
        insert_data = json.loads(request.body)
        insert_q1 = insert_data.get('Q1')
        insert_a1 = insert_data.get('A1')
        # print(insert_q1)
        # print(insert_a1)

        komoran = _komoran.Komoran()

        insert_a1_pos = komoran.pos(insert_a1)

        # print(insert_a1_pos)

        insert_a1_result = []
        for i in range(0, len(insert_a1_pos)):
            if insert_a1_pos[i][1] == 'NNG' or insert_a1_pos[i][1] == 'NNP' or insert_a1_pos[i][1] == 'NR':
                insert_a1_result.append(insert_a1_pos[i][0])

        insert_a1_result = set(insert_a1_result)

        data_query_set = ImZacadQ1Bk.objects.all()

        data_result = data_query_set.filter(zq_q1=insert_q1).all()
        data_result_serializer = Q1Serializer(data_result, many=True)
        # print(data_result_serializer.data[1]['zq_pk'])
        # print(data_result_serializer.data[1]['zq_q1'])
        # print(data_result_serializer.data[1]['zq_a1'])
        # print(data_result_serializer.data[1]['zq_code'])

        data_idx_result = []

        for n in range(0, len(data_result)):
            data_idx_result.append(data_result_serializer.data[n]['zq_pk'])
        # print(data_idx_result)

        data_pos_all_result: List[List[str]] = []

        for i in range(0, len(data_result)):
            data = data_result_serializer.data[i]['zq_a1']

            data_pos = komoran.pos(data)

            data_pos_result = []

            for j in range(0, len(data_pos) - 1):
                if data_pos[j][1] == 'NNG' or data_pos[j][1] == 'NNP' or data_pos[j][1] == 'NR':
                    data_pos_result.append(data_pos[j][0])

            data_pos_all_result.append(set(data_pos_result))
        # print(data_pos_all_result)

        zacad_result = []
        for k in range(0, len(data_pos_all_result)):
            union = set(insert_a1_result).union(set(data_pos_all_result[k]))
            intersection = set(insert_a1_result).intersection(set(data_pos_all_result[k]))
            similar = (len(intersection) / len(union)) * 100
            zacad_result.append((similar))

        # print(max(zacad_result))
        # print(zacad_result)

        data_all_result = dict(zip(zacad_result, data_idx_result))
        # print(data_all_result)
        #print(data_all_result[max(zacad_result)])

        q2_query_set = ImZacadQ2Bk.objects.all()

        q2_result = q2_query_set.filter(zq_pk=data_all_result[max(zacad_result)]).all()

        print(q2_result.values('zq_q2'))

        output = list(q2_result.values('zq_q2'))

        return JsonResponse(output[0], safe=False)

    def get(self, request, **kwargs):
        if kwargs.get('index') is None:
            data_queryset = ImZacadQ1Bk.objects.all()
            data_queryset_serializer = Q1Serializer(data_queryset, many=True)
            return Response(data_queryset_serializer.data, status=status.HTTP_200_OK)

        else:
            index = kwargs.get('index')
            data_serializer = Q1Serializer(ImZacadQ1Bk.objects.get(zq_pk=index))
            return Response(data_serializer.data, status=status.HTTP_200_OK)

        return Response('ok', status=200)

    def put(self, request):
        return Response('ok', status=200)

    def delete(self, request):
        return Response('ok', status=200)
