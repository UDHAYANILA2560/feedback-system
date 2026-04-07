def analyze_feedback(feedback_text: str) -> str:
    """
    Simple sentiment analysis: positive, neutral, negative
    Mimics the JS version.
    """
    text = feedback_text.lower()
    positive_words = ["tasty", "delicious", "yummy", "fresh", "hot", "crispy", "juicy", "soft",
 "flavorful", "spicy", "well-cooked", "perfectly cooked", "hygienic",
 "clean", "aromatic", "rich", "mouthwatering", "satisfying",
 "excellent", "good", "awesome", "amazing", "fantastic", "nice",
 "pleasant", "authentic"]
    negative_words = ["bad", "tasteless", "bland", "stale", "cold", "burnt", "overcooked",
 "undercooked", "oily", "too spicy", "too salty", "too sweet",
 "hard", "soggy", "dry", "smelly", "unhygienic", "dirty",
 "poor", "worst", "awful", "terrible", "disappointing",
 "not good", "low quality","yuck","salty"]

    if any(word in text for word in positive_words):
        return "😊 Positive"
    elif any(word in text for word in negative_words):
        return "😞 Negative"
    else:
        return "😐 Neutral"