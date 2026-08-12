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

# =============================================================
# Challenge 4: Notification Engine
# =============================================================
# Multi-channel notification engine with a polymorphic batch dispatcher

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, recipient, message):
        pass


class EmailService(NotificationService):
    def send_notification(self, recipient, message):
        print(f"Sending Email to {recipient}: {message}")


class SMSService(NotificationService):
    def send_notification(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")


class WhatsAppService(NotificationService):
    def send_notification(self, recipient, message):
        print(f"Sending WhatsApp message to {recipient}: {message}")


# Helper function to broadcast message across all enabled channels
def send_bulk_alerts(services_list, recipient, message):
    for service in services_list:
        service.send_notification(recipient, message)


# --- Testing Challenge 4 ---
channels = [EmailService(), SMSService(), WhatsAppService()]
send_bulk_alerts(channels, "user@example.com / 03491943858", "System Maintenance at 12:00 AM")

# =============================================================
# Challenge 5: AI Model Wrapper
# =============================================================

class LLMProvider(ABC):
    @abstractmethod
    def generate_response(self, prompt):
        pass

    @abstractmethod
    def get_token_count(self, text):
        pass


class OpenAIProvider(LLMProvider):
    def generate_response(self, prompt):
        return f"[OpenAI GPT-4o]: Responding to '{prompt}'..."

    def get_token_count(self, text):
        return len(text) // 4


class GeminiProvider(LLMProvider):
    def generate_response(self, prompt):
        return f"[Google Gemini 1.5]: Responding to '{prompt}'..."

    def get_token_count(self, text):
        return len(text) // 4


# --- Testing Challenge 5 ---
ai1 = OpenAIProvider()
print(ai1.generate_response("Explain FastAPI in 1 line"))
print(f"Token Count: {ai1.get_token_count('Explain FastAPI in 1 line')}")

print("-" * 40)

ai2 = GeminiProvider()
print(ai2.generate_response("Explain FastAPI in 1 line"))
print(f"Token Count: {ai2.get_token_count('Explain FastAPI in 1 line')}")