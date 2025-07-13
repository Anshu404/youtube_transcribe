# # Importing necessary libraries
# import streamlit as st  # Used to build web apps easily in Python
# from dotenv import load_dotenv  # For loading environment variables from .env file

# # Load all environment variables (like API keys) from .env file
# load_dotenv()

# import os  # For interacting with environment variables and OS-level functions
# import google.generativeai as genai  # Google Gemini AI SDK for text generation

# from youtube_transcript_api import YouTubeTranscriptApi  # Library to extract transcripts from YouTube videos

# # Configure the Gemini API using the key stored in .env file
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Define the system prompt to guide Gemini on how to summarize the transcript
# prompt = """You are Yotube video summarizer. You will be taking the transcript text
# and summarizing the entire video and providing the important summary in points
# within 250 words. Please provide the summary of the text given here:  """


# # Function to extract transcript from a given YouTube video URL
# def extract_transcript_details(youtube_video_url):
#     try:
#         # Extract video ID from the URL (assuming format is https://www.youtube.com/watch?v=VIDEO_ID)
#         video_id = youtube_video_url.split("=")[1]
        
#         # Use the YouTubeTranscriptApi to get the transcript as a list of text snippets
# # Use the YouTubeTranscriptApi to get the transcript in English or English-UK
#         # Use the YouTubeTranscriptApi to get the transcript in English or English-UK
#         transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'en-GB'])

#         # Concatenate all snippets into one long string of text
#         transcript = ""
#         for i in transcript_text:
#             transcript += " " + i["text"]

#         return transcript  # Return the full transcript string

#     except Exception as e:
#         # Raise any errors that occur (e.g., no captions available)
#         raise e


# # Function to generate a summary using Google Gemini Pro model
# def generate_gemini_content(transcript_text, prompt):
#     # Load Gemini Pro model
#     model = genai.GenerativeModel("gemini-2.5-pro")

#     # Send prompt + transcript to Gemini and get the response
#     response = model.generate_content(prompt + transcript_text)

#     return response.text  # Return the generated summary


# # Streamlit UI section starts here
# st.title("YouTube Transcript to Detailed Notes Converter")  # Title on the app interface

# # Create a text input box for the user to paste YouTube video link
# youtube_link = st.text_input("Enter YouTube Video Link:")

# # If the user enters a link, extract and display video thumbnail
# if youtube_link:
#     video_id = youtube_link.split("=")[1]  # Extract video ID from the URL
#     print(video_id)  # For debugging in terminal (optional)
    
#     # Show video thumbnail using video ID (0.jpg is the default thumbnail)
#     st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

# # Button that, when clicked, triggers the transcript extraction and summary generation
# if st.button("Get Detailed Notes"):
#     # Step 1: Extract transcript from video
#     transcript_text = extract_transcript_details(youtube_link)

#     if transcript_text:
#         # Step 2: Generate summary from transcript
#         summary = generate_gemini_content(transcript_text, prompt)

#         # Step 3: Display summary in the Streamlit app
#         st.markdown("## Detailed Notes:")
#         st.write(summary)









#extra update with the options 
# Importing necessary libraries
import streamlit as st  # Used to build web apps easily in Python
from dotenv import load_dotenv  # For loading environment variables from .env file

# Load all environment variables (like API keys) from .env file
load_dotenv()

import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt for Gemini
prompt = """You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """

# Function to extract transcript using user-chosen language
def extract_transcript_details(youtube_video_url, language_code):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=[language_code])

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e

# Generate summary using Gemini
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# UI
st.title("YouTube Transcript to Detailed Notes Converter")

youtube_link = st.text_input("Enter YouTube Video Link:")

language_code = "en"  # Default language

# Show thumbnail and dropdown if link is entered
if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

    # Let user choose transcript language
    language_code = st.selectbox("Choose transcript language", 
        ['en', 'en-GB', 'hi', 'fr', 'de', 'es', 'ar', 'zh-Hant', 'ru', 'pt', 'ja', 'ko', 'tr', 'it'])

# On click: generate summary
if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link, language_code)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
