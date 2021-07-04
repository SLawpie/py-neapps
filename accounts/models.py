from django.db import models

class LoginAttempts (models.Model):
    ip = models.CharField(max_length=15)
    #user_name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_agent = models.TextField()
    success = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def ua(self):
        return self.user_agent
