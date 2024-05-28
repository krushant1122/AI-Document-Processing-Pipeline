from PIL import Image
import pytesseract

def image_to_text(image_path):
    try:
        return pytesseract.image_to_string(Image.open(image_path))
    except Exception as e:
        print(f"Error processing image: {e}")
        return ""

if __name__ == "__main__":
    text_from_image = image_to_text('data/sample_image.png')
    print(text_from_image)
