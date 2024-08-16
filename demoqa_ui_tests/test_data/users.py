from dataclasses import dataclass


@dataclass
class User:
    full_name: str
    name: str
    last_name: str
    email: str
    current_address: str
    permanent_address: str

    gender: str
    phone_number: str
    day_of_birth: str
    year_of_birth: str
    month_of_birth: str
    study_subject1: str
    study_subject2: str
    img_name: str
    hobbies: str
    state: str
    city: str


student = User(
    full_name='Ellend Venture',
    name='Ellend',
    last_name='Venture',
    gender='Male',
    email='ellend@venture.com',
    current_address='Keep Venture, Luthadel',
    permanent_address='Keep Venture, Luthadel',
    phone_number='9998887755',
    day_of_birth='15',
    month_of_birth='November',
    year_of_birth='1900',
    study_subject1='Physics',
    study_subject2='Maths',
    hobbies='Sports, Reading, Music',
    img_name='tom-byrom.jpg',
    state='NCR',
    city='Delhi',
)
