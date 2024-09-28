from PIL import Image
import pytesseract
import enum

class OS(enum.Enum):
    Mac = 0
    Windows = 1

class Language(enum.Enum):
    ENG = 'eng'
    RUS = 'rus'
    ITA = 'ita'

class ImageReader:
    def __init__(self, os: OS):
        if os == OS.Windows:
            windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.pytesseract.tesseract_cmd = windows_path
            print('Running on Windows\n')
        elif os == OS.Mac:
            # Set the Tesseract path for macOS if needed
            # For macOS, the path might be different
            pass

    def extract_text(self, image: str, lang: str) -> str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang)
        return extracted_text

if __name__ == '__main__':
    ir = ImageReader(OS.Mac)  # Change the OS argument as needed
    text = ir.extract_text('plpl.jpg', lang=Language.ENG.value)  # Use .value to get the string value from the Enum
    print(text)