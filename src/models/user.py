from pydantic import BaseModel, ConfigDict, EmailStr, Field


class SecurityQuestion(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    question: str
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")


class UserRegistrationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str
    password_repeat: str = Field(alias="passwordRepeat")
    security_question: SecurityQuestion = Field(alias="securityQuestion")
    security_answer: str = Field(alias="securityAnswer")


class RegisteredUserData(BaseModel):
    id: int
    email: str
    role: str | None = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class Authentication(BaseModel):
    token: str
    umail: str | None = None
    bid: int | None = None


class LoginResponse(BaseModel):
    authentication: Authentication
