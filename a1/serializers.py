from rest_framework import serializers
from a1.models import Vocab

class VocabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocab
        fields = ('vocab_name', 'ans')
