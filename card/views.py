from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Card
from .serializer import CardSerializer
import pandas as pd
import random
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib.parse
import os


# Create your views here.
# print("CURRENT DIRECTORY::::: ", os.getcwd())
# print("ITEMS::::")
# for i in os.listdir():
#     print(i)
df = pd.read_csv("dictionary.csv", encoding='utf-8')


def clean_shoresh(curShoresh, hebrew, row):
    if curShoresh.strip() == "":
        newShoresh = df[df["Hebrew-Base"] == hebrew]["Root"].iloc[row]
        if newShoresh != "-":
            return newShoresh.replace(" ", "")
    if "-" in curShoresh:
        return curShoresh
    else:
        return '-'.join(list(curShoresh))


@api_view(['GET'])
def get_possibilities(request, word):

    decoded_word = urllib.parse.unquote(word)
    possible = df[df["Hebrew-Base"] == decoded_word][['Hebrew-Niqqud',
                                                      'Hebrew-Base', 'English']].to_dict('records')

    print(possible)
    return Response(possible)


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()  # .order_by("-timestamp")
    serializer_class = CardSerializer
    ordering = ['-timestamp']

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.query_params.get('sort_by', None)

        if sort_by == 'english':
            queryset = queryset.order_by('english')
        elif sort_by == '-english':
            queryset = queryset.order_by('-english')
        elif sort_by == 'hebrew':
            queryset = queryset.order_by('hebrew')
        elif sort_by == '-hebrew':
            queryset = queryset.order_by('-hebrew')
        elif sort_by == 'timestamp':
            queryset = queryset.order_by('timestamp')
        else:
            queryset = queryset.order_by(*self.ordering)

        return queryset

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        row = validated_data['row_num']

        if len(df[df["Hebrew-Base"] == validated_data['hebrew']]) == 0:
            validated_data['hebrew_nikkud'] = validated_data['hebrew']
            validated_data['english'] = validated_data['english'].lower()
        else:
            validated_data['shoresh'] = clean_shoresh(
                validated_data['shoresh'], validated_data['hebrew'], row)
            validated_data['english'] = validated_data['english'].lower()
            validated_data['hebrew_nikkud'] = df[df["Hebrew-Base"]
                                                 == validated_data['hebrew']]["Hebrew-Niqqud"].iloc[row]
            validated_data['Noun_singularAbsolute'] = df[df['Hebrew-Base']
                                                         == validated_data['hebrew']]['Noun_singularAbsolute'].iloc[row]
            validated_data['Noun_pluralAbsolute'] = df[df['Hebrew-Base']
                                                       == validated_data['hebrew']]['Noun_pluralAbsolute'].iloc[row]
            validated_data['Noun_singularConstruct'] = df[df['Hebrew-Base']
                                                          == validated_data['hebrew']]['Noun_singularConstruct'].iloc[row]
            validated_data['Noun_pluralConstruct'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Noun_pluralConstruct'].iloc[row]
            validated_data['Adj_SM'] = df[df['Hebrew-Base']
                                          == validated_data['hebrew']]['Adj_SM'].iloc[row]
            validated_data['Adj_SF'] = df[df['Hebrew-Base']
                                          == validated_data['hebrew']]['Adj_SF'].iloc[row]
            validated_data['Adj_PM'] = df[df['Hebrew-Base']
                                          == validated_data['hebrew']]['Adj_PM'].iloc[row]
            validated_data['Adj_PF'] = df[df['Hebrew-Base']
                                          == validated_data['hebrew']]['Adj_PF'].iloc[row]
            validated_data['Verb_ActivePresentSM'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_ActivePresentSM'].iloc[row]
            validated_data['Verb_ActivePresentSF'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_ActivePresentSF'].iloc[row]
            validated_data['Verb_ActivePresentPM'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_ActivePresentPM'].iloc[row]
            validated_data['Verb_ActivePresentPF'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_ActivePresentPF'].iloc[row]
            validated_data['Verb_ActivePastS1'] = df[df['Hebrew-Base']
                                                     == validated_data['hebrew']]['Verb_ActivePastS1'].iloc[row]
            validated_data['Verb_ActivePastP1'] = df[df['Hebrew-Base']
                                                     == validated_data['hebrew']]['Verb_ActivePastP1'].iloc[row]
            validated_data['Verb_ActivePastSM2'] = df[df['Hebrew-Base']
                                                      == validated_data['hebrew']]['Verb_ActivePastSM2'].iloc[row]
            validated_data['Verb_ActivePastSF2'] = df[df['Hebrew-Base']
                                                      == validated_data['hebrew']]['Verb_ActivePastSF2'].iloc[row]
            validated_data['Verb_ActivePastPM2'] = df[df['Hebrew-Base']
                                                      == validated_data['hebrew']]['Verb_ActivePastPM2'].iloc[row]
            validated_data['Verb_ActivePastPF2'] = df[df['Hebrew-Base']
                                                      == validated_data['hebrew']]['Verb_ActivePastPF2'].iloc[row]
            validated_data['Verb_ActivePastSM3'] = df[df['Hebrew-Base']
                                                      == validated_data['hebrew']]['Verb_ActivePastSM3'].iloc[row]
            validated_data['Verb_ActivePastSF3'] = df[df['Hebrew-Base']
                                                      == validated_data['hebrew']]['Verb_ActivePastSF3'].iloc[row]
            validated_data['Verb_ActivePastPM3'] = df[df['Hebrew-Base']
                                                      == validated_data['hebrew']]['Verb_ActivePastPM3'].iloc[row]
            validated_data['Verb_ActivePastPF3'] = df[df['Hebrew-Base']
                                                      == validated_data['hebrew']]['Verb_ActivePastPF3'].iloc[row]
            validated_data['Verb_ActiveFutureS1'] = df[df['Hebrew-Base']
                                                       == validated_data['hebrew']]['Verb_ActiveFutureS1'].iloc[row]
            validated_data['Verb_ActiveFutureP1'] = df[df['Hebrew-Base']
                                                       == validated_data['hebrew']]['Verb_ActiveFutureP1'].iloc[row]
            validated_data['Verb_ActiveFutureSM2'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_ActiveFutureSM2'].iloc[row]
            validated_data['Verb_ActiveFutureSF2'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_ActiveFutureSF2'].iloc[row]
            validated_data['Verb_ActiveFuturePM2'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_ActiveFuturePM2'].iloc[row]
            validated_data['Verb_ActiveFuturePF2'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_ActiveFuturePF2'].iloc[row]
            validated_data['Verb_ActiveFutureSM3'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_ActiveFutureSM3'].iloc[row]
            validated_data['Verb_ActiveFutureSF3'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_ActiveFutureSF3'].iloc[row]
            validated_data['Verb_ActiveFuturePM3'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_ActiveFuturePM3'].iloc[row]
            validated_data['Verb_ActiveFuturePF3'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_ActiveFuturePF3'].iloc[row]
            validated_data['Verb_ImperativeSM'] = df[df['Hebrew-Base']
                                                     == validated_data['hebrew']]['Verb_ImperativeSM'].iloc[row]
            validated_data['Verb_ImperativeSF'] = df[df['Hebrew-Base']
                                                     == validated_data['hebrew']]['Verb_ImperativeSF'].iloc[row]
            validated_data['Verb_ImperativePM'] = df[df['Hebrew-Base']
                                                     == validated_data['hebrew']]['Verb_ImperativePM'].iloc[row]
            validated_data['Verb_ImperativePF'] = df[df['Hebrew-Base']
                                                     == validated_data['hebrew']]['Verb_ImperativePF'].iloc[row]
            validated_data['Verb_PassivePresentSM'] = df[df['Hebrew-Base']
                                                         == validated_data['hebrew']]['Verb_PassivePresentSM'].iloc[row]
            validated_data['Verb_PassivePresentSF'] = df[df['Hebrew-Base']
                                                         == validated_data['hebrew']]['Verb_PassivePresentSF'].iloc[row]
            validated_data['Verb_PassivePresentPM'] = df[df['Hebrew-Base']
                                                         == validated_data['hebrew']]['Verb_PassivePresentPM'].iloc[row]
            validated_data['Verb_PassivePresentPF'] = df[df['Hebrew-Base']
                                                         == validated_data['hebrew']]['Verb_PassivePresentPF'].iloc[row]
            validated_data['Verb_PassivePastS1'] = df[df['Hebrew-Base']
                                                      == validated_data['hebrew']]['Verb_PassivePastS1'].iloc[row]
            validated_data['Verb_PassivePastP1'] = df[df['Hebrew-Base']
                                                      == validated_data['hebrew']]['Verb_PassivePastP1'].iloc[row]
            validated_data['Verb_PassivePastSM2'] = df[df['Hebrew-Base']
                                                       == validated_data['hebrew']]['Verb_PassivePastSM2'].iloc[row]
            validated_data['Verb_PassivePastSF2'] = df[df['Hebrew-Base']
                                                       == validated_data['hebrew']]['Verb_PassivePastSF2'].iloc[row]
            validated_data['Verb_PassivePastPM2'] = df[df['Hebrew-Base']
                                                       == validated_data['hebrew']]['Verb_PassivePastPM2'].iloc[row]
            validated_data['Verb_PassivePastPF2'] = df[df['Hebrew-Base']
                                                       == validated_data['hebrew']]['Verb_PassivePastPF2'].iloc[row]
            validated_data['Verb_PassivePastSM3'] = df[df['Hebrew-Base']
                                                       == validated_data['hebrew']]['Verb_PassivePastSM3'].iloc[row]
            validated_data['Verb_PassivePastSF3'] = df[df['Hebrew-Base']
                                                       == validated_data['hebrew']]['Verb_PassivePastSF3'].iloc[row]
            validated_data['Verb_PassivePastPM3'] = df[df['Hebrew-Base']
                                                       == validated_data['hebrew']]['Verb_PassivePastPM3'].iloc[row]
            validated_data['Verb_PassivePastPF3'] = df[df['Hebrew-Base']
                                                       == validated_data['hebrew']]['Verb_PassivePastPF3'].iloc[row]
            validated_data['Verb_PassiveFutureS1'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_PassiveFutureS1'].iloc[row]
            validated_data['Verb_PassiveFutureP1'] = df[df['Hebrew-Base']
                                                        == validated_data['hebrew']]['Verb_PassiveFutureP1'].iloc[row]
            validated_data['Verb_PassiveFutureSM2'] = df[df['Hebrew-Base']
                                                         == validated_data['hebrew']]['Verb_PassiveFutureSM2'].iloc[row]
            validated_data['Verb_PassiveFutureSF2'] = df[df['Hebrew-Base']
                                                         == validated_data['hebrew']]['Verb_PassiveFutureSF2'].iloc[row]
            validated_data['Verb_PassiveFuturePM2'] = df[df['Hebrew-Base']
                                                         == validated_data['hebrew']]['Verb_PassiveFuturePM2'].iloc[row]
            validated_data['Verb_PassiveFuturePF2'] = df[df['Hebrew-Base']
                                                         == validated_data['hebrew']]['Verb_PassiveFuturePF2'].iloc[row]
            validated_data['Verb_PassiveFutureSM3'] = df[df['Hebrew-Base']
                                                         == validated_data['hebrew']]['Verb_PassiveFutureSM3'].iloc[row]
            validated_data['Verb_PassiveFutureSF3'] = df[df['Hebrew-Base']
                                                         == validated_data['hebrew']]['Verb_PassiveFutureSF3'].iloc[row]
            validated_data['Verb_PassiveFuturePM3'] = df[df['Hebrew-Base']
                                                         == validated_data['hebrew']]['Verb_PassiveFuturePM3'].iloc[row]
            validated_data['Verb_PassiveFuturePF3'] = df[df['Hebrew-Base']
                                                         == validated_data['hebrew']]['Verb_PassiveFuturePF3'].iloc[row]
        serializer.save()

    # def perform_update(self, serializer):
    #     validatded_data = serializer.validated_data
    #     validatded_data['shoresh'] = clean_shoresh(validatded_data['shoresh'])
    #     serializer.save()


def random_card(request):
    # get the list of ids from the data
    id_list = list(Card.objects.values_list('id', flat=True))
    # get a random id from the id's
    random_id = random.choice(id_list)
    # get the random row of data from the table
    random_card = get_object_or_404(Card, id=random_id)
    # return the random row as a JSON response
    return JsonResponse(model_to_dict(random_card))
