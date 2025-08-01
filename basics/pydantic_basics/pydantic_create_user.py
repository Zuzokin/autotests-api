from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError, SecretStr
import uuid


class UserSchema(BaseModel):
    """
    Описание модели пользователя.
    """

    id: uuid
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Описание модели запроса на создание пользователя.
    """

    email: EmailStr
    password: SecretStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Описание модели ответа создания пользователя.
    """

    user: UserSchema
