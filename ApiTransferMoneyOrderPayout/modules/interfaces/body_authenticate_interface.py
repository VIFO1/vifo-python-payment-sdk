from dataclasses import dataclass

@dataclass
class BodyAuthenticateInterface:
    username: str
    password: str

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "password": self.password
        }