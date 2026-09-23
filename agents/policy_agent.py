from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class PolicyAgent:

    def review(self, claim):
        knowledge_file = Path("knowledge/policy_notes.txt")

        if not knowledge_file.exists():
            return "No policy knowledge source was found."

        text = knowledge_file.read_text(encoding="utf-8")

        paragraphs = [
            paragraph.strip()
            for paragraph in text.split("\n\n")
            if paragraph.strip()
        ]

        if not paragraphs:
            return "The policy knowledge source is empty."

        documents = paragraphs + [claim]

        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform(documents)

        claim_vector = vectors[-1]
        policy_vectors = vectors[:-1]

        similarities = cosine_similarity(
            claim_vector,
            policy_vectors
        ).flatten()

        top_indices = similarities.argsort()[-3:][::-1]

        relevant = []

        for index in top_indices:
            if similarities[index] > 0:
                relevant.append(paragraphs[index])

        if relevant:
            return (
                "Policy Review\n"
                "-------------\n"
                "Relevant policy information:\n\n"
                + "\n\n".join(relevant)
            )

        return "No relevant policy information was found."