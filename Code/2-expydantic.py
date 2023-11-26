# from pydantic import BaseModel, validator

# class user(BaseModel):
#     nome: str
#     idade: int
#     email: str

#     @validator('email')
#     def validade_email(cls, value):
#         if '@' not in value:
#             raise ValueError('Email está invalido')
#         return value

# user1 = user(
#     nome="Joao",
#     idade= 28,
#     email = "joao@gmail.com"
# )

# print(user1)