from transformers import pipeline

# Load once (cached after first run)
classifier = pipeline(
    task="zero-shot-classification",
    model="facebook/bart-large-mnli"
)

CATEGORIES = [
    "Medical",
    "Family Emergency",
    "Busy / Work",
    "Transportation Issue",
    "Personal Reason",
    "Out of Station / Travel",
    "Other / Unclear"
]

def classify_excuse(transcript: str) -> str:
    """
    Takes transcript text and returns best matching category
    """
    if not transcript or transcript.strip() == "":
        return "Other / Unclear"

    result = classifier(
        transcript,
        candidate_labels=CATEGORIES
    )

    # highest confidence label
    return result["labels"][0]
