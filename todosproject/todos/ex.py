class MUser:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return self.name


class UserBIO:
    def __init__(self, text, user):
        self.user = user
        self.text = text


class Task:
    def __init__(self, task_name, user):
        self.user = user
        self.task_name = task_name
