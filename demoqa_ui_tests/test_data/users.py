from dataclasses import dataclass


@dataclass
class User:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


student = User(
    full_name='Ellend Venture',
    email='ellend@venture.com',
    current_address='Keep Venture, Luthadel',
    permanent_address='Keep Venture, Luthadel',
)
