import os
import exifread
import mutagen
from PIL import Image

def extract_metadata(file_path):
    try:
        # Determine file type based on extension
        ext = os.path.splitext(file_path)[1].lower()

        if ext in ['.jpg', '.jpeg', '.png', '.tiff', '.gif']:
            if ext == '.png':
                # Use Pillow for PNG metadata
                img = Image.open(file_path)
                width, height = img.size
                format = img.format
                print(f"PNG Image: Width={width}, Height={height}, Format={format}")
            else:
                # Extract EXIF data using exifread
                print(f"Processing JPEG file: {file_path}")
                with open(file_path, 'rb') as f:
                    tags = exifread.process_file(f)
                    if tags:
                        print("EXIF Data:")
                        for tag, value in tags.items():
                            print(f"{tag}: {value}")
                    else:
                        print("No EXIF data found.")

        elif ext in ['.mp3', '.wav', '.flac']:
            # Extract audio metadata using mutagen
            audio = mutagen.File(file_path)
            print("Audio Metadata:")
            # Process audio metadata here (print relevant information)
            print(audio.info)

        else:
            print(f"Unsupported file type: {ext}")

    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file path (supported formats:\n JPG, JPEG, PNG, TIFF, GIF, MP3, WAV, FLAC): ").strip("'")
    extract_metadata(file_path)
