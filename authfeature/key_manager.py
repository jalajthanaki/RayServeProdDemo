import uuid
from .redis_client import redis_client

KEY_PREFIX = "api_key:"
USAGE_PREFIX = "usage:"

class APIKeyManager:
    @staticmethod
    def create_key() -> str:
        key = str(uuid.uuid4())
        redis_client.set(KEY_PREFIX + key, "active")
        redis_client.set(USAGE_PREFIX + key, 0)
        return key

    @staticmethod
    def list_keys():
        keys = redis_client.keys(KEY_PREFIX + "*")
        return [k.replace(KEY_PREFIX, "") for k in keys]

    @staticmethod
    def delete_key(key: str) -> bool:
        key_deleted = redis_client.delete(KEY_PREFIX + key)
        usage_deleted = redis_client.delete(USAGE_PREFIX + key)
        return key_deleted > 0

    @staticmethod
    def increment_usage(key: str) -> int:
        if redis_client.exists(KEY_PREFIX + key):
            return redis_client.incr(USAGE_PREFIX + key)
        else:
            return -1

    @staticmethod
    def get_usage(key: str) -> int:
        usage = redis_client.get(USAGE_PREFIX + key)
        return int(usage) if usage else 0
