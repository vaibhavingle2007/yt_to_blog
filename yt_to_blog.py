import os
import subprocess
import whisper
import uuid
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file for API key
load_dotenv()
NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY")

# Initialize Nebius-compatible client
client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=NEBIUS_API_KEY
)

def download_audio(video_url):
    output_file = f"audio_{uuid.uuid4().hex}.mp3"
    command = [
        "yt-dlp", "-x", "--audio-format", "mp3", video_url, "-o", output_file
    ]
    print(f"Downloading audio from: {video_url}")
    subprocess.run(command, check=True)
    return output_file

def transcribe_audio(audio_path):
    print("Transcribing audio using Whisper...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

def generate_blog(transcript, mood):
    print(f"Generating blog post in '{mood}' tone...")

    tone_prompts = {
        "professional": "Write a professional blog post. Use formal language, structured headings, and an informative tone suitable for business or industry readers.",
        "casual": "Write a casual, friendly blog post. Use an informal, conversational tone as if speaking to a friend. Include emojis if appropriate.",
        "academic": "Write an academic blog post. Use formal, precise language with structured arguments and paragraph formatting. Avoid casual expressions."
    }

    prompt = f"""
You are a skilled blog writer. {tone_prompts[mood]}

Below is a transcript of a YouTube video. Convert it into a well-written blog post with headings, paragraphs, and logical structure.

Transcript:
{transcript}
"""

    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-70B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content

def save_blog(blog_text):
    filename = f"blog_{uuid.uuid4().hex}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(blog_text)
    print(f"Blog saved to: {filename}")

def main():
    try:
        video_url = input("Enter YouTube Video URL: ").strip()

        print("\nSelect a writing tone:")
        print("1. Professional")
        print("2. Casual")
        print("3. Academic")
        mood_option = input("Enter 1 / 2 / 3: ").strip()

        mood_map = {
            "1": "professional",
            "2": "casual",
            "3": "academic"
        }

        mood = mood_map.get(mood_option, "professional")  # default to professional

        audio_file = download_audio(video_url)
        transcript = transcribe_audio(audio_file)
        blog_post = generate_blog(transcript, mood)
        save_blog(blog_post)

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
