from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class TokenClaims(BaseModel):
    sub: str
    iat: int
    exp: int
