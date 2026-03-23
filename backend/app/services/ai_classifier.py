from transformers import pipeline

# Load model once (IMPORTANT — do NOT reload every request)
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

# Your 7 categories
CATEGORIES = [
    "Fever / Illness",
    "Hospitalized / Medical Emergency",
    "Out of Station / Travel",
    "Family Function / Personal Work",
    "Exam / Academic Reason",
    "Busy / Will Attend Later",
    "Other / Unclear Reason"
]


def classify_excuse(transcript: str):
    try:
        if not transcript or transcript.strip() == "":
            return "Uncategorized"

        result = classifier(
            transcript,
            candidate_labels=CATEGORIES
        )

        predicted_category = result["labels"][0]
        confidence = result["scores"][0]

        # Optional confidence threshold
        if confidence < 0.40:
            return "Uncategorized"

        return predicted_category

    except Exception as e:
        print("AI Classification Error:", e)
        return "Uncategorized"
