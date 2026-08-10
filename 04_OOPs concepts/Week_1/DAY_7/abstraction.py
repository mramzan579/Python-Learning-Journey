# Abstraction: Hiding implementation details and enforcing strict contracts on child classes.
# Ensures all drivers use identical interface method names so the main system never breaks.

from abc import ABC, abstractmethod


# =============================================================
# Challenge 1: Payment Gateways
# =============================================================
# Enforces same payment methods across different processors (JazzCash, Stripe)

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund_payment(self, transaction_id):
        pass


class JazzCash(PaymentGateway):
    # Private helper for internal OTP verification before processing
    def _verify_otp(self, otp):
        print(f"Verifying OTP: {otp} for JazzCash payment.")

    def process_payment(self, amount):
        self._verify_otp("1234")
        print(f"Processing payment of {amount} through JazzCash.")

    def refund_payment(self, transaction_id):
        print(f"Refund processed through JazzCash for transaction ID: {transaction_id}")


class Stripe(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} through Stripe.")

    def refund_payment(self, transaction_id):
        print(f"Refund processed through Stripe for transaction ID: {transaction_id}")


# --- Testing Challenge 1 ---
p1 = JazzCash()
p1.process_payment(500)
p1.refund_payment("TXN_9988")


# =============================================================
# Challenge 2: Database Drivers
# =============================================================
# Unified interface for relational (SQL) and NoSQL databases

class DatabaseDriver(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class PostgreSQL(DatabaseDriver):
    def connect(self):
        print("Connecting to PostgreSQL database...")

    def execute_query(self, query):
        print(f"Executing SQL query: {query}")

    def disconnect(self):
        print("PostgreSQL connection closed.")


class MongoDB(DatabaseDriver):
    def connect(self):
        print("Connecting to MongoDB database...")

    def execute_query(self, query):
        print(f"Executing NoSQL query: {query}")  # Added missing f-string

    def disconnect(self):
        print("MongoDB connection closed.")


# --- Testing Challenge 2 ---
db1 = PostgreSQL()
db1.connect()
db1.execute_query("SELECT * FROM users;")
db1.disconnect()

db2 = MongoDB()
db2.connect()
db2.execute_query("db.users.find()")
db2.disconnect()


# =============================================================
# Challenge 3: File Storage Providers
# =============================================================
# Standard interface for swapping local file storage with cloud (AWS S3)

class StorageProvider(ABC):
    @abstractmethod
    def upload_file(self, file_name):
        pass

    @abstractmethod
    def delete_file(self, file_name):
        pass


class LocalStorage(StorageProvider):
    def upload_file(self, file_name):
        print(f"Uploading {file_name} to local storage...")

    def delete_file(self, file_name):
        print(f"Deleting {file_name} from local storage...")


class AWSS3Storage(StorageProvider):
    def upload_file(self, file_name):
        print(f"Uploading {file_name} to AWS S3...")

    def delete_file(self, file_name):
        print(f"Deleting {file_name} from AWS S3...")


# --- Testing Challenge 3 ---
s1 = LocalStorage()
s1.upload_file("example.txt")

s2 = AWSS3Storage()
s2.upload_file("example.txt")