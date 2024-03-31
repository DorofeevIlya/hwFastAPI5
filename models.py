from typing import Optional
from pydantic import BaseModel

_count = 1



class User(BaseModel):
    username: str
    email: str
    password: str

    def add_id(self, user_id=None):
        user=UserWithId(username=self.username, email=self.email, password=self.password)
        if user_id:
            user.user_id=user_id
        return user


class UserWithId(User):
    user_id: int
    def __init__(self, username, email, password):
        global _count
        super().__init__(username=username, email=email, password=password, user_id=0)
        self.user_id = _count
        _count+=1




    def __repr__(self):
        return f'{self.user_id=}, {self.username=}, {self.email=}, {self.password=}'

users = [
        UserWithId(username='Алексей Петров', email='apet@mail.ru', password='1234qwer'),
        UserWithId(username='Семён Девятов', email='s9atov@mail.ru', password='1234qwer'),
        UserWithId(username='Глеб Голубев', email='gg@mail.ru', password='1234qwer'),
        UserWithId(username='Инна Селезнева', email='small99fish@mail.ru', password='1234qwer'),
        UserWithId(username='Анна Смирнова', email='annet1995@gmail.com', password='1234qwer')
    ]