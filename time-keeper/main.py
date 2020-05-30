from datetime import datetime
from fastapi import FastAPI

app = FastAPI(
    title="Time Keeper Container",
    description="This API returns the current datetime in UTC",
    version="1.0.0",
)


@app.get("/")
def get_datetime():
    return {
        "datetime_utc": datetime.utcnow().isoformat()
    }
