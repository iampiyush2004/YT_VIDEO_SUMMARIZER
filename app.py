import streamlit as st
from dotenv import load_dotenv

load_dotenv() ##load all the nevironment variables
import os
from google import genai
from youtube_transcript_api import YouTubeTranscriptApi

# Setup the Gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """


## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        # Extract video ID more robustly
        if "v=" in youtube_video_url:
            video_id = youtube_video_url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in youtube_video_url:
            video_id = youtube_video_url.split("youtu.be/")[1].split("?")[0]
        else:
            raise ValueError("Invalid YouTube URL")

        api = YouTubeTranscriptApi()
        list_transcripts = api.list(video_id)
        
        # Try to find English, then just take the first available if English not found
        try:
            transcript_data = list_transcripts.find_transcript(['en']).fetch()
        except Exception:
            # If English not found, let's just take the first one available
            available_transcripts = list(list_transcripts)
            if not available_transcripts:
                raise ValueError("No transcripts found for this video.")
            transcript_data = available_transcripts[0].fetch()

        transcript = " ".join([i.text for i in transcript_data])

        return transcript

    except Exception as e:
        raise e
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite", # Using the latest recommended model
        contents=prompt + transcript_text
    )
    return response.text

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    # Extract video ID for thumbnail
    if "v=" in youtube_link:
        video_id = youtube_link.split("v=")[1].split("&")[0]
    elif "youtu.be/" in youtube_link:
        video_id = youtube_link.split("youtu.be/")[1].split("?")[0]
    else:
        video_id = None

    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

if st.button("Get Detailed Notes"):
    try:
        transcript_text=extract_transcript_details(youtube_link)

        if transcript_text:
            summary=generate_gemini_content(transcript_text,prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)
    except Exception as e:
        st.error(f"Error: {str(e)}")




