from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_year = models.IntegerField(blank=True, null=True)
    copies_total = models.PositiveIntegerField(default=1)
    copies_available = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrows')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrows')
    borrowed_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    returned_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.member} -> {self.book}"

