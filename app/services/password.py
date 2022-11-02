import bcrypt

class PasswordService: 
    @staticmethod
    def compare_password(password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(bytes(password, 'utf-8'), bytes(hashed_password, 'utf-8'))

    @staticmethod
    def hash_password(password: str) -> str:
        return str(bcrypt.hashpw(password=bytes(password, 'utf-8'), salt=bcrypt.gensalt()).decode('utf-8'))