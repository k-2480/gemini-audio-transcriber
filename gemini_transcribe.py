import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai

parser = argparse.ArgumentParser(description="Transcribe a Japanese audio file with speaker-separated paragraphs using Gemini.")
parser.add_argument("--input", dest="input_file")
parser.add_argument("--output", dest="output_file")
args = parser.parse_args()

if not args.input_file or not args.output_file:
    parser.print_usage()
    sys.exit("Error: Both --input and --output arguments are required.")

if not os.path.isfile(args.input_file):
    sys.exit(f"Error: The input file '{args.input_file}' does not exist.")

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

client = genai.Client(api_key=GOOGLE_API_KEY)

print(f"Uploading the file: {args.input_file}")

myfile = client.files.upload(file=args.input_file)

print("Transcribing the audio...")

prompt = (
    "Transcribe this audio clip into Japanese. Identify different speakers and format the transcript accordingly. "
    "Each speaker's dialogue should be separated into distinct paragraphs with line breaks between turns. "
    "Do not summarize—transcribe as faithfully as possible. "
    "If possible, label each speaker as 'Speaker 1', 'Speaker 2', etc."
    "Important: Do not insert any extra spaces between Japanese words. The output should be written in natural Japanese, as it would appear in a book or article. No unnecessary spacing."
)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=[prompt, myfile]
)

with open(args.output_file, "w", encoding="utf-8") as file:
    file.write(response.text)

print(f"Done. Transcribed file saved as '{args.output_file}'")