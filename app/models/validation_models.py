from pydantic import BaseModel

class UserInfo(BaseModel):
    username: str
    email: str
    full_name: str
