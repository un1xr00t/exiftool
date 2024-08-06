## exiftool.py: Extract Metadata from Various File Formats

This Python script, `exiftool.py`, assists in extracting metadata from various file formats, including:

* **Images:** JPG, JPEG, PNG, TIFF, GIF
* **Audio:** MP3, WAV, FLAC

**Features:**

*  Reads EXIF data from JPEG images using the `exifread` library.
*  Retrieves basic information from PNG images using the `PIL` (Python Imaging Library).
*  Extracts metadata from audio files using the `mutagen` library.

**Usage:**

1. **Prerequisites:**
    * Python 3.x (ensure you have `pip` installed)
    * Install required libraries:
      ```bash
      pip install exifread mutagen Pillow
      ```

2. **Save the script as `exiftool.py`**

3. **Run the script:**
   ```bash
   python exiftool.py

4. Enter the file path:
The script will prompt you for the file path. Ensure the file is accessible and supported by the script.

Output:
Based on the file type, the script will display relevant metadata.
