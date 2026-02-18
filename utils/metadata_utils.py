from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(uploaded_file):
    try:
        img = Image.open(uploaded_file)
        exif = img._getexif()
        if exif:
            return {TAGS.get(tag): value for tag, value in exif.items()}
        return {}
    except:
        return {}
