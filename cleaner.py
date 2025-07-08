import asyncio
from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

# List all the collections you want to clean regularly
CLEAN_COLLECTIONS = ["requests", "logs", "join_reqs", "join_reqs2"]

async def clear_mongodb_collections_every_10_minutes():
    while True:
        for collection in CLEAN_COLLECTIONS:
            try:
                result = db[collection].delete_many({})
                print(f"✅ Cleared {result.deleted_count} items from collection: {collection}")
            except Exception as e:
                print(f"❌ Failed to clear collection {collection}: {e}")
        await asyncio.sleep(600)  # 600 seconds = 10 minutes
