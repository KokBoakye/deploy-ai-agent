from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import anthropic
import os

app = FastAPI()

class Query(BaseModel):
    message: str

@app.get("/")  
def read_root():
    return {"message": "Hello from your AI Agent!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/chat")
async def chat(query: Query):
    try:
        client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=1000,
            messages=[{"role": "user", "content": query.message}]
        )
        return {"response": message.content[0].text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
