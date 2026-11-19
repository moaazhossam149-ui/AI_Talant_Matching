from sentence_transformers import SentenceTransformer, util

# تحميل موديل المطابقة الدلالية الذكي والخفيف
print("جاري تحميل موديل الذكاء الاصطناعي للمطابقة...")
model = SentenceTransformer('all-MiniLM-L6-v2')


def evaluate_candidate_match(candidate_skills, job_description, required_skills):
    """
    دالة لحساب نسبة التوافق الدلالي وتحليل فجوة المهارات
    """
    # 1. حساب نسبة التوافق الدلالي (Semantic Match Score) بين مهارات المطور والوصف الوظيفي
    candidate_text = ", ".join(candidate_skills)

    embedding_cv = model.encode(candidate_text, convert_to_tensor=True)
    embedding_jd = model.encode(job_description, convert_to_tensor=True)

    # حساب التشابه وتحويله لنسبة مئوية من 100%
    semantic_score = util.cos_sim(embedding_cv, embedding_jd).item() * 100

    # 2. تحليل فجوة المهارات (Skill Gap Analysis)
    candidate_lower = {s.lower() for s in candidate_skills}
    required_lower = {s.lower() for s in required_skills}

    matched_skills = candidate_lower.intersection(required_lower)
    missing_skills = required_lower - candidate_lower  # المهارات الناقصة

    return round(semantic_score, 2), matched_skills, missing_skills


if __name__ == "__main__":
    # مهارات المطور اللي استخرجناها من الـ CV في الخطوة السابقة
    developer_skills = ["Python", "FastAPI", "Java", "Postgresql", "Spacy", "Javascript", "Git", "Github", "Pandas",
                        "AI", "NLP"]

    # وصف وظيفي لوظيفة Backend / AI Developer من شركة وهمية
    job_desc = """
    We are looking for a Backend and AI Software Engineer experienced in Python, FastAPI, 
    PostgreSQL, Docker, and Natural Language Processing (NLP) to build smart platforms.
    """

    # المهارات الإجبارية المطلوبة في الوظيفة
    job_required_skills = ["Python", "FastAPI", "PostgreSQL", "Docker", "NLP", "AI", "Git"]

    print("\nجاري مطابقة المطور بالوظيفة وتحليل الفجوات...\n")

    score, matched, missing = evaluate_candidate_match(developer_skills, job_desc, job_required_skills)

    # طباعة التقرير الاحترافي للنتيجة
    print("=" * 50)
    print(f" 🎯 AI Match Score (نسبة التوافق): {score}%")
    print("=" * 50)
    print(" ✅ المهارات المتطابقة (Matched Skills):")
    for s in matched:
        print(f"   - {s.capitalize()}")

    print("\n ❌ المهارات الناقصة / فجوة المهارات (Skill Gap):")
    if missing:
        for s in missing:
            print(f"   - {s.capitalize()} (تحتاج لتطوير أو إثبات في المشروع)")
    else:
        print("   - مبروك! لا توجد فجوات مهارية، المطور مؤهل تماماً للوظيفة.")
    print("=" * 50)