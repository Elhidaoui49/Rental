#!/usr/bin/env python3
"""
French Learning — Plan Customizer

Allows users to edit and customize their learning plan.
"""

class PlanCustomizer:
    """Customize learning plan based on user preferences"""

    # Available levels and their grammar focus
    LEVELS = {
        "A2": {
            "grammar_focus": ["présent", "passé_composé", "imparfait", "futur_proche", "articles"],
            "vocab_level": "basic",
            "speaking_time": "1-2 min"
        },
        "B1": {
            "grammar_focus": ["futur_simple", "pronoms", "negation", "questions", "connecteurs"],
            "vocab_level": "intermediate",
            "speaking_time": "2-3 min"
        },
        "B2": {
            "grammar_focus": ["conditionnel", "subjonctif", "discours_indirect", "nuances"],
            "vocab_level": "advanced",
            "speaking_time": "3-5 min"
        }
    }

    # Available intensities (hours per day)
    INTENSITIES = {
        "30min": {"morning": "15 min", "afternoon": "15 min"},
        "1h": {"morning": "30 min", "afternoon": "30 min"},
        "2h": {"morning": "1h", "afternoon": "1h"},
        "3h": {"morning": "1h30", "afternoon": "1h30"}
    }

    def __init__(self, current_day=1, current_level="A2", current_intensity="2h"):
        """Initialize with current plan settings"""
        self.current_day = current_day
        self.current_level = current_level
        self.current_intensity = current_intensity

    def edit_level(self, new_level):
        """Edit learning level"""
        if new_level in self.LEVELS:
            self.current_level = new_level
            return self._format_level_change(new_level)
        else:
            return f"❌ Niveau invalide. Choisissez: {', '.join(self.LEVELS.keys())}"

    def edit_intensity(self, new_intensity):
        """Edit daily study intensity"""
        if new_intensity in self.INTENSITIES:
            self.current_intensity = new_intensity
            return self._format_intensity_change(new_intensity)
        else:
            return f"❌ Intensité invalide. Choisissez: {', '.join(self.INTENSITIES.keys())}"

    def edit_schedule(self, morning_time, evening_time):
        """Edit notification schedule"""
        return self._format_schedule_change(morning_time, evening_time)

    def skip_to_day(self, target_day):
        """Skip to specific day"""
        if target_day > self.current_day:
            days_skipped = target_day - self.current_day
            self.current_day = target_day
            return self._format_skip(target_day, days_skipped)
        else:
            return f"❌ Le jour {target_day} est déjà passé."

    def reset_plan(self):
        """Reset plan to day 1"""
        self.current_day = 1
        self.current_level = "A2"
        self.current_intensity = "2h"
        return self._format_reset()

    def get_current_plan(self):
        """Get current plan summary"""
        return self._format_plan_summary()

    def _format_level_change(self, new_level):
        """Format level change message"""
        level_info = self.LEVELS[new_level]
        msg = f"✅ **Niveau modifié: {new_level}**\n\n"
        msg += f"📚 Grammaire: {', '.join(level_info['grammar_focus'])}\n"
        msg += f"📖 Vocabulaire: {level_info['vocab_level']}\n"
        msg += f"🗣️ Objectif de parole: {level_info['speaking_time']}\n"
        msg += f"\n📅 Jour actuel: {self.current_day}"
        return msg

    def _format_intensity_change(self, new_intensity):
        """Format intensity change message"""
        intensity_info = self.INTENSITIES[new_intensity]
        msg = f"✅ **Intensité modifiée: {new_intensity}/jour**\n\n"
        msg += f"🌅 Matin: {intensity_info['morning']}\n"
        msg += f"🌞 Après-midi: {intensity_info['afternoon']}\n"
        msg += f"\n📅 Jour actuel: {self.current_day}"
        return msg

    def _format_schedule_change(self, morning_time, evening_time):
        """Format schedule change message"""
        msg = f"✅ **Horaire modifié**\n\n"
        msg += f"🌅 Notification matinale: {morning_time}\n"
        msg += f"🌙 Notification du soir: {evening_time}\n"
        msg += f"\n💡 Vous recevrez votre leçon à {morning_time}"
        return msg

    def _format_skip(self, target_day, days_skipped):
        """Format skip confirmation message"""
        msg = f"⚠️ **Saut au jour {target_day}**\n\n"
        msg += f"Vous allez sauter: Jours {self.current_day}-{target_day-1} ({days_skipped} jours)\n\n"
        msg += "⚠️ Avertissement:\n"
        msg += "- Vous manquerez {days_skipped} leçons de grammaire\n"
        msg += "- {days_skipped * 10} mots de vocabulaire\n"
        msg += "- {days_skipped} exercices de pratique\n\n"
        msg += "Continuer ? Oui/Non"
        return msg

    def _format_reset(self):
        """Format reset confirmation message"""
        msg = f"🔄 **Réinitialiser le plan ?**\n\n"
        msg += "Cela va:\n"
        msg += "- Retourner au jour 1\n"
        msg += "- Supprimer tout progrès enregistré\n"
        msg += "- Recommencer avec le niveau A2\n\n"
        msg += "Confirmer : Oui/Non"
        return msg

    def _format_plan_summary(self):
        """Format current plan summary"""
        msg = f"📊 **Plan Actuel**\n\n"
        msg += f"🎯 Niveau: {self.current_level}\n"
        msg += f"📅 Jour: {self.current_day}\n"
        msg += f"⏱️ Intensité: {self.current_intensity}/jour\n\n"
        msg += "Modifier:\n"
        msg += "/edit_plan niveau [A2/B1/B2]\n"
        msg += "/edit_plan intensité [30min/1h/2h/3h]\n"
        msg += "/edit_plan jour [numéro]\n"
        msg += "/schedule\n"
        msg += "/reset"
        return msg


def main():
    """Test plan customization"""
    customizer = PlanCustomizer()

    print("=" * 60)
    print("Plan Customization Test")
    print("=" * 60)
    print()

    # Test 1: Edit level
    print("Test 1: Edit level to B1")
    print(customizer.edit_level("B1"))
    print()

    # Test 2: Edit intensity
    print("Test 2: Edit intensity to 3h")
    print(customizer.edit_intensity("3h"))
    print()

    # Test 3: Skip to day
    print("Test 3: Skip to day 20")
    print(customizer.skip_to_day(20))
    print()

    # Test 4: Schedule change
    print("Test 4: Edit schedule")
    print(customizer.edit_schedule("8h", "21h"))
    print()

    # Test 5: Plan summary
    print("Test 5: Current plan summary")
    print(customizer.get_current_plan())
    print()


if __name__ == "__main__":
    main()
