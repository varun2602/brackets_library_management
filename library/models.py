from django.db import models

# Create your models here.
class books(models.Model):
    book_name = models.CharField(max_length = 100)
    book_author = models.CharField(max_length = 100)
    is_issued = models.BooleanField(default = False)
    issued_to = models.CharField(max_length = 100, blank = True, null = True, default = '')

    def __str__(self):
        return f"{self.book_name}  {self.is_issued} {self.book_author}"
    
