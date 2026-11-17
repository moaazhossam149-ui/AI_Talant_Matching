import pdfplumber
import spacy

# تحميل موديل الذكاء الاصطناعي للغة الإنجليزية
nlp = spacy.load("en_core_web_sm")


def extract_skills_from_cv(pdf_path):
    # 1. استخراج النص من الـ PDF (اللي عملناه امبارح)
    extracted_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"

    # 2. تحليل النص بالذكاء الاصطناعي
    doc = nlp(extracted_text)

    # قائمة المهارات البرمجية والتقنية المستهدفة للبحث عنها
    target_skills = [
        "python", "java", "c++", "javascript", "react", "next.js",
        "nlp", "machine learning", "ai", "git", "github", "sql",
        "fastapi", "django", "postgresql", "spacy", "pandas", "scikit-learn"
    ]

    found_skills = set()

    # البحث عن المهارات داخل نص السيرة الذاتية (بغض النظر عن الحروف الكبيرة والصغيرة)
    text_lower = extracted_text.lower()
    for skill in target_skills:
        if skill in text_lower:
            found_skills.add(skill.capitalize())

    return extracted_text, list(found_skills)


if __name__ == "__main__":
    # اختيار ملف الـ CV للتجربة
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    pdf_file = filedialog.askopenfilename(title="اختر ملف السيرة الذاتية (PDF)", filetypes=[("PDF files", "*.pdf")])

    if pdf_file:
        print("جاري تحليل السيرة الذاتية واستخراج المهارات بالذكاء الاصطناعي...\n")
        full_text, skills = extract_skills_from_cv(pdf_file)

        print("=" * 40)
        print(" 🎯 المهارات المستخرجة تلقائياً (AI Skill Extraction):")
        print("=" * 40)
        for s in skills:
            print(f"- {s}")
        print("=" * 40)