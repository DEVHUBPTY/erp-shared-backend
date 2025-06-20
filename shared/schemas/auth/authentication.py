from pydantic import BaseModel

class LoginDTO(BaseModel):
    email: str
    password: str


class SessionResponse(BaseModel):
    user_id: str
    role: list[str]
