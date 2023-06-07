from passlib.context import CryptContext

pwdContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwdContext.hash(password)

def verify(password: str, hashedPass: str):
    return pwdContext.verify(password, hashedPass)
