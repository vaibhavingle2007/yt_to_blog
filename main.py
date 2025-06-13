from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from converter import YouTubeToBlogConverter
import os

app = FastAPI()
converter = YouTubeToBlogConverter()

class BlogRequest(BaseModel):
    video_url: str
    tone: str  # Options: "professional", "casual", "academic"

@app.post("/generate-blog")
def generate_blog(request: BlogRequest):
    try:
        # Step 1: Download audio and get video title
        audio_file, video_title = converter.download_audio(request.video_url)

        # Step 2: Transcribe the audio
        transcript = converter.transcribe_audio(audio_file)

        # Step 3: Generate blog from transcript
        blog_post = converter.generate_blog(transcript, request.tone)

        # Step 4: Return the blog and video title
        return {
            "title": video_title,
            "blog": blog_post
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
