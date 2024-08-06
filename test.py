import exifread

def test_exifread(file_path):
  try:
    with open(file_path, 'rb') as f:
      tags = exifread.process_file(f)
      if tags:
        print("EXIF data found using test script!")
      else:
        print("No EXIF data found using test script.")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  file_path = "/home/elliot/Pictures/IMG_1296.jpg"
  test_exifread(file_path)
