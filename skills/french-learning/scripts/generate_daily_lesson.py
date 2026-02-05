#!/usr/bin/env python3
"""
French Learning — Daily Lesson Generator

Generates structured daily lessons with grammar, vocabulary, and exercises.
"""

import random
from datetime import datetime

class LessonGenerator:
    """Generate daily French lessons based on month/day progression"""

    # Month 1: A2 → B1 (Foundations)
    MONTH_1_LESSONS = [
        # Week 1: Présent
        {
            "day": 1,
            "title": "Verbes fréquents (er)",
            "grammar": "Verbes en -er: je parle, tu parles, il/elle parle, nous parlons, vous parlez, ils/elles parlent",
            "vocab_theme": "Travailler (work)",
            "vocab_words": [
                {"word": "Travailler", "context": "Je travaille dans une entreprise"},
                {"word": "L'entreprise", "context": "L'entreprise est grande"},
                {"word": "Le bureau", "context": "Mon bureau est au 2ème étage"},
                {"word": "Le collègue", "context": "Mon collègue est sympa"},
                {"word": "Le patron", "context": "Le patron arrive demain"},
                {"word": "Le salaire", "context": "Mon salaire augmente"},
                {"word": "L'emploi", "context": "Je cherche un emploi"},
                {"word": "La carrière", "context": "Ma carrière avance bien"},
                {"word": "La réunion", "context": "Nous avons une réunion"},
                {"word": "Le projet", "context": "Le projet est terminé"}
            ],
            "exercise": "Écris 10 phrases en utilisant des verbes en -er (parler, travailler, manger, finir, etc.)"
        },
        {
            "day": 2,
            "title": "Verbes fréquents (irréguliers)",
            "grammar": "Avoir, être, aller, faire: j'ai, tu as, il a / je suis, tu es, il est / je vais, tu vas, il va / je fais, tu fais, il fait",
            "vocab_theme": "Vie quotidienne (daily life)",
            "vocab_words": [
                {"word": "Se réveiller", "context": "Je me réveille à 7h"},
                {"word": "Se lever", "context": "Je me lève et je prends une douche"},
                {"word": "Prendre", "context": "Je prends le petit-déjeuner"},
                {"word": "Aller", "context": "Je vais au travail"},
                {"word": "Rentrer", "context": "Je rentre à 19h"},
                {"word": "Cuisiner", "context": "Je cuisine le dîner"},
                {"word": "Manger", "context": "Je mange avec ma famille"},
                {"word": "Regarder", "context": "Je regarde la télé"},
                {"word": "Lire", "context": "Je lis un livre avant de dormir"},
                {"word": "Dormir", "context": "Je dors 8 heures par nuit"}
            ],
            "exercise": "Décris ta journée d'hier en utilisant au moins 5 verbes irréguliers"
        },
        # ... more lessons would be added here
    ]

    def __init__(self, day=None):
        """Initialize with specific day or current day"""
        self.day = day if day else 1

    def get_lesson(self):
        """Get lesson for current day (Month 1 for now)"""
        # For now, just return first lesson
        if self.day <= len(self.MONTH_1_LESSONS):
            return self.MONTH_1_LESSONS[self.day - 1]
        else:
            return self._generate_generic_lesson()

    def _generate_generic_lesson(self):
        """Generate a generic lesson when day exceeds pre-defined lessons"""
        return {
            "day": self.day,
            "title": "Révision et Pratique",
            "grammar": "Révision des temps principaux: présent, passé composé, imparfait",
            "vocab_theme": "Révision",
            "vocab_words": self._get_random_vocab(),
            "exercise": "Pratique libre: écris une histoire de 100 mots"
        }

    def _get_random_vocab(self):
        """Get random vocabulary words"""
        themes = [
            "Travailler", "Famille", "Sentiments", "Voyages", "Santé",
            "Technology", "Culture", "Business"
        ]
        return [{"word": theme, "context": f"Vocabulaire sur {theme}"} for theme in themes[:5]]

    def format_lesson(self, lesson):
        """Format lesson for Telegram message"""
        msg = f"📚 **Leçon {lesson['day']}: {lesson['title']}**\n\n"
        msg += f"🌅 **Matin — 1 heure**\n"
        msg += f"⏱️ 20 min — Grammaire\n{lesson['grammar']}\n\n"
        msg += f"⏱️ 20 min — Vocabulaire ({lesson['vocab_theme']})\n"
        for i, v in enumerate(lesson['vocab_words'][:5], 1):
            msg += f"{i}. {v['word']}\n   {v['context']}\n"
        msg += f"\n⏱️ 20 min — Écoute\nÉcoute un court dialogue français\n\n"
        msg += f"🌞 **Après-midi — 1 heure**\n"
        msg += f"⏱️ 20 min — Parler\nRaconte ta journée (2 minutes)\n\n"
        msg += f"⏱️ 20 min — Écrire\nÉcris 5-10 phrases sur un thème réel\n\n"
        msg += f"⏱️ 20 min — Lecture\nLis un texte court, note les structures\n\n"
        msg += f"💪 **Exercice du jour**\n{lesson['exercise']}\n\n"
        msg += f"🚨 **Règle d'or**\nConsistances > Perfection. Parle avant d'être \"prêt\" !"
        return msg


def main():
    """Generate and print daily lesson"""
    generator = LessonGenerator()
    lesson = generator.get_lesson()
    formatted = generator.format_lesson(lesson)

    print("=" * 60)
    print("French Learning — Daily Lesson")
    print("=" * 60)
    print()
    print(formatted)
    print()


if __name__ == "__main__":
    main()
