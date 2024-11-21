# pip install googletrans==4.0.0-rc1 PyPDF2

from googletrans import Translator
from PyPDF2 import PdfReader

translator = Translator()

language = {
    "bn": "Bangla",
    "en": "English",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    "la": "Latin",
    "ms": "Malay",
    "ne": "Nepali",
    "ru": "Russian",
    "ar": "Arabic",
    "zh": "Chinese",
    "es": "Spanish"
}

def show_language_options():
    print("Code : Language")
    for code, lang in language.items():
        print(f"{code} => {lang}")
    print()

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def main():
    while True:
        user_code = input("Please input desired language code. To see the language code list enter 'options': ")
        if user_code == "options":
            show_language_options()
            continue
        
        if user_code in language:
            print(f"You have selected {language[user_code]}")
            break
        print("It's not a valid language code!")

    while True:
        choice = input("\nWould you like to (1) translate text or (2) translate from a PDF? (Type 'close' to exit): ")

        if choice.lower() == "close":
            print("\nHave a nice Day!")
            break
        
        if choice == "1":
            string = input("\nWrite the text you want to translate: ")
            translated = translator.translate(string, dest=user_code)
            print(f"\n{language[user_code]} translation: {translated.text}")
            print(f"Pronunciation: {translated.pronunciation}")

        elif choice == "2":
            pdf_path = input("\nEnter the path to the PDF file: ")
            try:
                text = extract_text_from_pdf(pdf_path)
                if text:
                    translated = translator.translate(text, dest=user_code)
                    print(f"\n{language[user_code]} translation: {translated.text}")
                else:
                    print("No text found in the PDF.")
            except Exception as e:
                print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    main()