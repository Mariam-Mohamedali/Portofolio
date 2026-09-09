from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('django', 'Django'),
        ('frontend', 'Frontend'),
        ('java', 'Java'),
        ('cpp', 'C++'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    short_desc = models.CharField(max_length=300, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    tech_stack = models.CharField(max_length=500, help_text='Comma-separated: Django, Python, MySQL')
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    start_date = models.CharField(max_length=50, blank=True)
    end_date = models.CharField(max_length=50, blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('language', 'Programming Language'),
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('database', 'Database'),
        ('tools', 'Tools & Design'),
    ]

    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, help_text='Devicon class e.g. devicon-python-plain')
    percentage = models.IntegerField(default=80)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='language')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.subject}'
