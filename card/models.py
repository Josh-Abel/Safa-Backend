from django.db import models

# Create your models here.


class Card(models.Model):
    hebrew = models.CharField(max_length=300)
    hebrew_nikkud = models.CharField(max_length=300, null=True, blank=True)
    english = models.CharField(max_length=300)
    shoresh = models.CharField(max_length=10, null=True, blank=True)
    pos = models.CharField(max_length=10)
    binyan = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    example = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    # image = models.ImageField(null=True, blank=True, upload_to="images/")
    timestamp = models.DateTimeField(auto_now=True)
    row_num = models.IntegerField(null=True, blank=True)

    # Adding the conjugations
    Noun_singularAbsolute = models.CharField(
        max_length=300, null=True, blank=True)
    Noun_pluralAbsolute = models.CharField(
        max_length=300, null=True, blank=True)
    Noun_singularConstruct = models.CharField(
        max_length=300, null=True, blank=True)
    Noun_pluralConstruct = models.CharField(
        max_length=300, null=True, blank=True)
    Adj_SM = models.CharField(max_length=300, null=True, blank=True)
    Adj_SF = models.CharField(max_length=300, null=True, blank=True)
    Adj_PM = models.CharField(max_length=300, null=True, blank=True)
    Adj_PF = models.CharField(max_length=300, null=True, blank=True)
    Verb_ActivePresentSM = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActivePresentSF = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActivePresentPM = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActivePresentPF = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActivePastS1 = models.CharField(max_length=300, null=True, blank=True)
    Verb_ActivePastP1 = models.CharField(max_length=300, null=True, blank=True)
    Verb_ActivePastSM2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActivePastSF2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActivePastPM2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActivePastPF2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActivePastSM3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActivePastSF3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActivePastPM3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActivePastPF3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActiveFutureS1 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActiveFutureP1 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActiveFutureSM2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActiveFutureSF2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActiveFuturePM2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActiveFuturePF2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActiveFutureSM3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActiveFutureSF3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActiveFuturePM3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ActiveFuturePF3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_ImperativeSM = models.CharField(max_length=300, null=True, blank=True)
    Verb_ImperativeSF = models.CharField(max_length=300, null=True, blank=True)
    Verb_ImperativePM = models.CharField(max_length=300, null=True, blank=True)
    Verb_ImperativePF = models.CharField(max_length=300, null=True, blank=True)
    Verb_PassivePresentSM = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassivePresentSF = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassivePresentPM = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassivePresentPF = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassivePastS1 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassivePastP1 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassivePastSM2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassivePastSF2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassivePastPM2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassivePastPF2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassivePastSM3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassivePastSF3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassivePastPM3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassivePastPF3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassiveFutureS1 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassiveFutureP1 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassiveFutureSM2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassiveFutureSF2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassiveFuturePM2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassiveFuturePF2 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassiveFutureSM3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassiveFutureSF3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassiveFuturePM3 = models.CharField(
        max_length=300, null=True, blank=True)
    Verb_PassiveFuturePF3 = models.CharField(
        max_length=300, null=True, blank=True)

    def __str__(self):
        return self.english + "     =====     " + self.hebrew
