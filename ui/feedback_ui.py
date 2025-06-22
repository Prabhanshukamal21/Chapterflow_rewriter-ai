from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from Storage.chroma_utils import get_latest_version, add_version

app = FastAPI()
templates = Jinja2Templates(directory="ui/templates")

@app.get("/", response_class=HTMLResponse)
async def review_page(request: Request):
    try:
        latest_text = get_latest_version("ai_writer_v1")
    except Exception as e:
        latest_text = "⚠️ Error loading chapter: " + str(e)
    return templates.TemplateResponse("review.html", {"request": request, "text": latest_text})

@app.post("/submit")
async def submit_review(review: str = Form(...)):
    try:
        add_version("ai_writer_v1", review, {"stage": "human-reviewed"})
        return {"message": "✅ Review submitted successfully!"}
    except Exception as e:
        return {"error": f"❌ Failed to submit review: {e}"}

if __name__ == "__main__":
    uvicorn.run("ui.feedback_ui:app", host="127.0.0.1", port=8000, reload=True)