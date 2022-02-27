from . import parser, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICE = (
        ('FILM', 'FILM'),
        ('SERIAL', 'SERIAL'),
        ('ANIME','ANIME')
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        model = models.Film
        fields = [
            'media_type',
        ]

    def parse_data(self):
        if self.data['media_type'] == 'FILM':
            film_parser = parser.parser_film()
            for i in film_parser:
                models.Film.objects.create(**i)
        elif self.data['media_type'] == 'SERIAL':
            serial_parser = parser.parser_serial()
            for i in serial_parser:
                models.Film.objects.create(**i)
        elif self.data['media_type'] == 'ANIME':
            anime_parser = parser.parser_anime()
            for i in anime_parser:
                models.Film.objects.create(**i)