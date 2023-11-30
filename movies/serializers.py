from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id",
                  "name",
                  "year",
                  "time",
                  "imdb",
                  "votes",
                  "meta_score",
                  "gross",
                  "certification",
                  "description")

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.year = validated_data.get("year", instance.year)
        instance.time = validated_data.get("time", instance.time)
        instance.imdb = validated_data.get("imdb", instance.imdb)
        instance.votes = validated_data.get("votes", instance.votes)
        instance.meta_score = validated_data.get("meta_score", instance.meta_score)
        instance.gross = validated_data.get("gross", instance.gross)
        instance.certification = validated_data.get("certification", instance.certification)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance
