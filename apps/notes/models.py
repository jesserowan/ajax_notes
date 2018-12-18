from django.db import models

class NoteManager(models.Manager):
    def validate(self, form):
        errors = []
        if not form['title']:
            errors.append("Your note must have a title")
        return errors

class Note(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = NoteManager()
