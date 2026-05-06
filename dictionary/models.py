from django.db import models
from django.core.exceptions import ValidationError

class Word(models.Model):

    CATEGORY_CHOICES = (
        ('FOOD', 'Food'),
        ('BODY', 'Body'),
        ('ANIMAL', 'Animal'),
        ('FAMILY', 'Family'),
        ('PLACE', 'Place'),
        ('NUMBER', 'Number'),
        ('COLOR', 'Color'),
        ('GREETING', 'Greeting'),
        ('VERB', 'Verb'),
        ('OTHER', 'Other'),
    )

    tamil_word = models.CharField(max_length=255, unique=True)
    arabic_word = models.CharField(max_length=255, unique=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='OTHER'
    )

    example_sentence = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        self.tamil_word = self.tamil_word.strip()
        self.arabic_word = self.arabic_word.strip()

        if Word.objects.exclude(pk=self.pk).filter(tamil_word__iexact=self.tamil_word).exists():
            raise ValidationError({'tamil_word': 'This Tamil word already exists.'})

        if Word.objects.exclude(pk=self.pk).filter(arabic_word__iexact=self.arabic_word).exists():
            raise ValidationError({'arabic_word': 'This Arabic word already exists.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tamil_word} → {self.arabic_word}"