from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'hebrew', 'hebrew_nikkud', 'english', 'shoresh',
                  'pos', 'binyan', 'gender', 'example', 'note', 'timestamp', 'row_num',
                  'Noun_singularAbsolute',
                  'Noun_pluralAbsolute',
                  'Noun_singularConstruct',
                  'Noun_pluralConstruct',
                  'Adj_SM',
                  'Adj_SF',
                  'Adj_PM',
                  'Adj_PF',
                  'Verb_ActivePresentSM',
                  'Verb_ActivePresentSF',
                  'Verb_ActivePresentPM',
                  'Verb_ActivePresentPF',
                  'Verb_ActivePastS1',
                  'Verb_ActivePastP1',
                  'Verb_ActivePastSM2',
                  'Verb_ActivePastSF2',
                  'Verb_ActivePastPM2',
                  'Verb_ActivePastPF2',
                  'Verb_ActivePastSM3',
                  'Verb_ActivePastSF3',
                  'Verb_ActivePastPM3',
                  'Verb_ActivePastPF3',
                  'Verb_ActiveFutureS1',
                  'Verb_ActiveFutureP1',
                  'Verb_ActiveFutureSM2',
                  'Verb_ActiveFutureSF2',
                  'Verb_ActiveFuturePM2',
                  'Verb_ActiveFuturePF2',
                  'Verb_ActiveFutureSM3',
                  'Verb_ActiveFutureSF3',
                  'Verb_ActiveFuturePM3',
                  'Verb_ActiveFuturePF3',
                  'Verb_ImperativeSM',
                  'Verb_ImperativeSF',
                  'Verb_ImperativePM',
                  'Verb_ImperativePF',
                  'Verb_PassivePresentSM',
                  'Verb_PassivePresentSF',
                  'Verb_PassivePresentPM',
                  'Verb_PassivePresentPF',
                  'Verb_PassivePastS1',
                  'Verb_PassivePastP1',
                  'Verb_PassivePastSM2',
                  'Verb_PassivePastSF2',
                  'Verb_PassivePastPM2',
                  'Verb_PassivePastPF2',
                  'Verb_PassivePastSM3',
                  'Verb_PassivePastSF3',
                  'Verb_PassivePastPM3',
                  'Verb_PassivePastPF3',
                  'Verb_PassiveFutureS1',
                  'Verb_PassiveFutureP1',
                  'Verb_PassiveFutureSM2',
                  'Verb_PassiveFutureSF2',
                  'Verb_PassiveFuturePM2',
                  'Verb_PassiveFuturePF2',
                  'Verb_PassiveFutureSM3',
                  'Verb_PassiveFutureSF3',
                  'Verb_PassiveFuturePM3',
                  'Verb_PassiveFuturePF3']
