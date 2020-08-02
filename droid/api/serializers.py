from rest_framework import serializers
from droid.api.models import Anunciante, DemandaDePecas


"""
Serializers allow complex data such as querysets and model instances to be converted to native Python
datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide
deserialization, allowing parsed data to be converted back into complex types, after first validating the
incoming data.
"""


class AnuncianteSerializer(serializers.ModelSerializer):

    """
    AnuncianteSerializer - Will translate objects implemented in Model Anunciante
    for viewing them in the DRF form.
    """
    class Meta:
        model = Anunciante
        fields = '__all__'


class DemandaDePecaSerializer(serializers.ModelSerializer):

    """
    DemandaDePecaSerializer - Will translate objects implemented in Model DemandaDePecas
    for viewing them in the DRF form.
    """

    class Meta:
        model = DemandaDePecas
        fields = '__all__'
