from typing import Optional
from email_validator import EmailNotValidError, validate_email
from pydantic import BaseModel, Field, field_validator, ConfigDict

class userBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    email: str = Field(..., min_length=5, max_length=100)
    role: str = Field(..., min_length=4, max_length=50)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        try:
            # check_deliverability=False evita el error 422 con dominios como yahoo.com o example.com
            validate_email(value, check_deliverability=False)
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email address: {e}")

        return value

    @field_validator("role")
    @classmethod
    def validate_role(cls, value: str) -> str:
        allowed_roles = ["admin", "support", "user"]

        if value not in allowed_roles:
            raise ValueError(
                f"Invalid role. Allowed roles are: {', '.join(allowed_roles)}"
            )

        return value

class userCreate(userBase):
    is_active: bool = True

class userUpdate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    email: str = Field(..., min_length=5, max_length=100)
    role: str = Field(..., min_length=4, max_length=50)
    is_active: bool = True

    @field_validator("email")
    @classmethod
    def validate_update_email(cls, value: str) -> str:
        try:
            validate_email(value, check_deliverability=False)
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email address: {e}")

        return value

    @field_validator("role")
    @classmethod
    def validate_update_role(cls, value: str) -> str:
        allowed_roles = ["admin", "support", "user"]

        if value not in allowed_roles:
            raise ValueError(
                f"Invalid role. Allowed roles are: {', '.join(allowed_roles)}"
            )

        return value

class userPatch(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=3,
        max_length=100
    )

    email: Optional[str] = Field(
        None,
        min_length=5,
        max_length=100
    )

    role: Optional[str] = Field(
        None,
        min_length=4,
        max_length=50
    )

    is_active: Optional[bool] = None

    @field_validator("email")
    @classmethod
    def validate_patch_email(
        cls,
        value: Optional[str]
    ) -> Optional[str]:

        if value is not None:
            try:
                validate_email(value, check_deliverability=False)
            except EmailNotValidError as e:
                raise ValueError(f"Invalid email address: {e}")

        return value

    @field_validator("role")
    @classmethod
    def validate_patch_role(
        cls,
        value: Optional[str]
    ) -> Optional[str]:

        if value is not None:
            allowed_roles = ["admin", "support", "user"]

            if value not in allowed_roles:
                raise ValueError(
                    f"Invalid role. Allowed roles are: {', '.join(allowed_roles)}"
                )

        return value

class userResponse(userBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)