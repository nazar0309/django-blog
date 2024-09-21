from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)  # A short title for the "About" section
    updated_on = models.DateTimeField(auto_now=True)  # Automatically updates on save
    content = models.TextField(db_index=False)  # Main content, no indexing

    def __str__(self):
        return self.title
    
class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
