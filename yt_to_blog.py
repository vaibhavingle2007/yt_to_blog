import os
import subprocess
import whisper
import uuid
from openai import OpenAI
from dotenv import load_dotenv

class YouTubeToBlogConverter:
    def __init__(self):
        load_dotenv()
        self.nebius_api_key = os.getenv("NEBIUS_API_KEY")
        self.client = OpenAI(
            base_url="https://api.studio.nebius.com/v1/",
            api_key=self.nebius_api_key
        )
        self.model = whisper.load_model("base")  # Load Whisper model during initialization

    def download_audio(self, video_url):
        output_file = f"audio_{uuid.uuid4().hex}.mp3"
        
        # Extract title
        command_title = ["yt-dlp", "--get-title", video_url]
        title_process = subprocess.run(command_title, capture_output=True, text=True, check=True)
        video_title = title_process.stdout.strip()

        # Download audio and thumbnail
        command_download = [
            "yt-dlp", "-x", "--audio-format", "mp3", "--write-thumbnail", video_url, "-o", output_file
        ]
        print(f"Downloading audio from: {video_url}")
        subprocess.run(command_download, check=True)
        
        return output_file, video_title

    def transcribe_audio(self, audio_path):
        print("Transcribing audio using Whisper...")
        result = self.model.transcribe(audio_path)
        return result["text"]

    def generate_blog(self, transcript, mood):
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

        response = self.client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-70B-Instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        return response.choices[0].message.content

    def save_blog(self, blog_text):
        filename = f"blog_{uuid.uuid4().hex}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(blog_text)
        print(f"Blog saved to: {filename}")

def main():
    try:
        converter = YouTubeToBlogConverter()  # Instantiate the class

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

        audio_file, video_title = converter.download_audio(video_url)
        transcript = converter.transcribe_audio(audio_file)
        blog_post = converter.generate_blog(transcript, mood)
        converter.save_blog(blog_post)
        
        print(f"Video Title: {video_title}") #printing title

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
