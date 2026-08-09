from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGODB_URL")

if not MONGO_URL:
    raise ValueError("MONGODB_URL not found in .env file")

app = FastAPI()

client = AsyncIOMotorClient(MONGO_URL)

@app.get("/health")
async def health_check():
    try:
        await client.admin.command("ping")
        return {
            "status": "ok",
            "mongodb": "Connected ✅"
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"MongoDB connection failed: {str(e)}"
        )