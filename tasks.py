import numpy as np

# База знаний: вероятность болезни при симптоме 
probabilities = {
    "грипп": {"кашель": 0.8, "температура": 0.9, "головная боль": 0.6},
    "простуда": {"кашель": 0.6, "чихание": 0.7, "насморк": 0.9},
    "аллергия": {"чихание": 0.8, "насморк": 0.7, "сыпь": 0.5}
}


def diagnose(symptoms):
    disease_scores = {}

    # Подсчет вероятности для каждой болезни
    for disease, symptom_probs in probabilities.items():
        score = np.prod([symptom_probs.get(symptom, 0.1) for symptom in symptoms])
        disease_scores[disease] = score
    # Выбирается болезнь с наибольшей вероятностью
    best_match = max(disease_scores, key=disease_scores.get)
    return f"Наиболее вероятная болезнь: {best_match} ({disease_scores[best_match]:.2f} вероятность)"


# Пользователь вводит симптомы
user_symptoms = input("Введите симптомы через запятую: ").lower().split(", ")
print(diagnose(user_symptoms))
