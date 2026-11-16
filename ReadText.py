import pdfplumber
import tkinter as tk
from tkinter import filedialog


def select_and_parse_pdf():
    # إخفاء نافذة تكنبر الرئيسية الصغيرة
    root = tk.Tk()
    root.withdraw()

    # فتح نافذة لاختيار ملف الـ PDF بالماوس
    file_path = filedialog.askopenfilename(
        title="اختر ملف السيرة الذاتية (PDF)",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not file_path:
        print("لم يتم اختيار أي ملف.")
        return

    print(f"تم اختيار الملف: {file_path}")
    print("جاري قراءة السيرة الذاتية...")

    extracted_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"

    print("\n--- تم استخراج النص بنجاح (أول 500 حرف) ---")
    print(extracted_text[:500])


if __name__ == "__main__":
    select_and_parse_pdf()