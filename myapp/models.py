# from django.db import models
from django.db import models
from django.contrib.auth.models import User


# -----------------------------
#  User Profile (Extra fields)
# -----------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    department = models.CharField(max_length=100, blank=True)
    employee_id = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# -----------------------------
#  IT Helpdesk Ticket Model
# -----------------------------
class Ticket(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ticket #{self.id} - {self.subject}"
    
    from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject



# -----------------------------
# #  Chatbot Conversation History
# # -----------------------------
# class ChatHistory(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     reply = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Chat by {self.user.username} at {self.timestamp}"


# # -----------------------------
# #  AI Bot Response Logs
# # -----------------------------
# class BotResponseLog(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     user_message = models.TextField()
#     bot_response = models.TextField()
#     confidence_score = models.FloatField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Response to {self.user.username} ({self.confidence_score})"

# # Create your models here.
