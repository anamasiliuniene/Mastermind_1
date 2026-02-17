from django.contrib.auth.models import User
from django.db import models

# <--Assignment -->

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UserAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_assignments")
    assignment = models.ForeignKey(Assignment, on_delete=models.SET_NULL, null=True, blank=True, related_name="user_assignments")
    tasks_done = models.JSONField(default=dict, blank=True)  # JSON: užduočių progress
    answers = models.JSONField(default=dict, blank=True)     # JSON: refleksijos atsakymai
    is_shared = models.BooleanField(default=False)           # ar matomas feede
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.assignment.title if self.assignment else 'Personal'}"


# <--Feed/Comment -->
class Comment(models.Model):
    user_assignment = models.ForeignKey(UserAssignment,
                                        on_delete=models.CASCADE,
                                        related_name="comments")
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username if self.author else 'Anon'}: {self.content}"


# <--Goal / Task -->
class Goal(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="goals")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class GoalTask(models.Model):
    goal = models.ForeignKey(Goal,
                             on_delete=models.CASCADE,
                             related_name="tasks")
    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({'done' if self.is_done else 'pending'})"
