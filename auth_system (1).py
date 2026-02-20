import hashlib

# Class: CryptoManager

class CryptoManager:
    """
    Handles password validation and hashing.
    Uses static methods because no object state is required.
    """

    @staticmethod
    def generate_hash(password):
        """Return SHA-256 hash of the password."""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def validate_password(password):
        """
        Password rules:
        - At least 10 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one digit
        """
        if len(password) < 10:
            return False

        if not any(ch.isupper() for ch in password):
            return False

        if not any(ch.islower() for ch in password):
            return False

        if not any(ch.isdigit() for ch in password):
            return False

        return True


# Class: Member

class Member:
    """
    Represents a system member.
    Only hashed passwords are stored.
    """

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash


# Class: SecureAccessManager

class SecureAccessManager:
    """
    Controls user registration and authentication.
    Simulates secure storage using a dictionary.
    """

    def __init__(self):
        self._database = {}  # Simulated secure storage

    def create_account(self, username, password):
        # Normalize username
        normalized_username = username.strip().lower()

        if normalized_username in self._database:
            print("❌ Account already exists.")
            return

        # Validate password strength
        if not CryptoManager.validate_password(password):
            print("❌ Password must be at least 10 characters long and include uppercase, lowercase, and numbers.")
            return

        # Hash password before storing
        password_hash = CryptoManager.generate_hash(password)

        # Store securely
        self._database[normalized_username] = Member(normalized_username, password_hash)

        print("🔐 Password successfully hashed.")
        print("✅ Account created successfully!")

    def authenticate(self, username, password):
        normalized_username = username.strip().lower()

        if normalized_username not in self._database:
            print("❌ No such user found.")
            return

        entered_hash = CryptoManager.generate_hash(password)
        stored_hash = self._database[normalized_username].password_hash

        if entered_hash == stored_hash:
            print("✅ Authentication successful. Access granted.")
        else:
            print("❌ Authentication failed. Incorrect password.")


# Main Execution

def main():
    system = SecureAccessManager()

    print("=== ACCOUNT REGISTRATION ===")
    user = input("Username: ")
    pwd = input("Password: ")
    system.create_account(user, pwd)

    print("\n=== LOGIN PROCESS ===")
    user = input("Username: ")
    pwd = input("Password: ")
    system.authenticate(user, pwd)


if __name__ == "__main__":
    main()