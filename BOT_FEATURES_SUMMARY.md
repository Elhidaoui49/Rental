# Doxo French Bot — Résumé des Fonctionnalités

**Bot:** @daily_doxo_bot
**Status:** Configuré avec plan customization
**Date:** 2026-02-05

---

## 🎯 Commandes Disponibles

| Commande | Description | Exemple |
|----------|-------------|---------|
| `/start` | Commencer les leçons | `/start` |
| `/lesson` | Leçon du jour | `/lesson` |
| `/vocab` | Vocabulaire du jour | `/vocab` |
| `/grammar` | Règle de grammaire | `/grammar` |
| `/exercise` | Exercice de pratique | `/exercise` |
| `/progress` | Voir ton progrès | `/progress` |
| `/edit_plan` | Modifier le plan | `/edit_plan niveau B1` |
| `/schedule` | Voir/Modifier l'horaire | `/schedule` |
| `/reset` | Recommencer le plan | `/reset` |

---

## 📊 Personnalisation du Plan

### 1. Changer le Niveau

```
/edit_plan niveau B1
/edit_plan niveau B2
```

**Disponible:** A2, B1, B2

**Effet:**
- Adapte la grammaire au niveau
- Ajuste le vocabulaire
- Modifie les objectifs de parole

### 2. Changer l'Intensité

```
/edit_plan intensité 1h
/edit_plan intensité 3h
```

**Disponible:** 30min, 1h, 2h, 3h

**Effet:**
- Matin: 15 min / 30 min / 1h / 1h30
- Après-midi: 15 min / 30 min / 1h / 1h30

### 3. Sauter des Jours

```
/edit_plan jour 20
/edit_plan jour 50
```

**Effet:**
- Saute directement au jour spécifié
- Avertissement sur les leçons manquées

### 4. Modifier l'Horaire

```
/schedule matin 8h soir 21h
```

**Effet:**
- Change l'heure des notifications
- Matin: Leçon du jour
- Soir: Rappel de pratique

### 5. Personnaliser les Thèmes

```
/edit_plan thème business
/edit_plan thème santé
```

**Thèmes disponibles:**
- Business (travail, entreprise)
- Santé (médecine, bien-être)
- Voyages (tourisme, déplacement)
- Famille (relations, maison)
- Sentiments (émotions, opinions)
- Technology (internet, digital)
- Culture (art, musique, cinéma)

### 6. Réinitialiser le Plan

```
/reset
```

**Effet:**
- Retour au jour 1
- Niveau A2 (début)
- Supprime tout progrès

---

## 📅 Notifications Quotidiennes

### 🌅 Matin (9:00 AM)
```
📚 Leçon du Jour

⏱️ 20 min — Grammaire
[Grammar rule with examples]

⏱️ 20 min — Vocabulaire
[10 words with context]

⏱️ 20 min — Écoute
[Audio/Dialogue exercise]

🌞 Après-midi — 1 heure

⏱️ 20 min — Parler
Speak for 2 minutes

⏱️ 20 min — Écrire
Write 5-10 sentences

⏱️ 20 min — Lecture
Read short text

💪 Exercice du jour
[Daily exercise]

🚨 Règle d'or
Consistances > Perfection !
```

### 🌙 Soir (20:00 PM)
```
📝 Rappel du Soir

Avez-vous pratiqué aujourd'hui ?
- Parler: ___ minutes
- Écrire: ___ phrases
- Lecture: ___ minutes

✅ Oui / ❌ Non

Si NON:
- Qu'est-ce qui t'a bloqué ?
- Prochaine action: ___

✨ Continue comme ça !
```

---

## 🎯 Progress Tracking

**Sur `/progress` commande:**

```
📊 Ton Progrès

Niveau: B1 (Jour 15/90)
Jours complétés: 15
Grammaire: 8/20 thèmes couverts
Vocabulaire: 150 mots appris
Exercices: 45 complétés
Temps de parole: 5 heures

Objectif B1: 35% complété
Prochain objectif: B1 solide (Jour 30)

Continue comme ça ! 💪
```

**Métriques suivies:**
- Jours complétés
- Thèmes de grammaire maîtrisés
- Mots de vocabulaire appris
- Exercices complétés
- Heures de parole accumulées

---

## 🎓 Niveaux et Objectifs

### A2 → B1 (Mois 1)
**Objectif:** Parler sans bloquer
- Grammaire de base (temps principaux)
- Vocabulaire quotidien (thèmes simples)
- Moins d'erreurs graves

**Durée:** 1 mois (30 jours)
**Exigence:** 2h/jour

### B1 (Mois 2)
**Objectif:** Connecter les idées
- Futur simple
- Pronoms (COD, COI, y, en)
- Connecteurs logiques
- Parler 2-3 minutes sans pause

**Durée:** 1 mois (30 jours)
**Exigence:** 2h/jour

### B1 → B2 (Mois 3-5)
**Objectif:** Défendre une opinion
- Conditionnel
- Subjonctif (basic)
- Discours indirect
- Nuances et vocabulaire précis
- Langue autonome

**Durée:** 3 mois (90 jours)
**Exigence:** 2h/jour

---

## 🆘 Support et Problèmes

### Problème: Bot ne répond pas

**Solutions:**
1. Vérifie que tu as commencé avec `/start`
2. Vérifie les permissions Telegram
3. Redémarre Telegram

### Problème: Notifications pas reçues

**Solutions:**
1. Vérifie `/schedule` pour confirmer l'horaire
2. Vérifie les réglages Telegram
3. Essaye `/lesson` pour forcer la leçon

### Problème: Leçon trop difficile

**Solutions:**
1. Envoie `/edit_plan niveau A2` pour simplifier
2. Demande `/vocab` avec thème spécifique
3. Dis-moi "facile" et je simplifie

### Problème: Besoin de personnalisation avancée

**Solutions:**
1. Envoie ton objectif: "Je veux DELF B2 en 3 mois"
2. Envoie ton thème: "Je veux français pour business"
3. Je créerai un plan sur mesure

---

## 📚 Ressources Disponibles

**Documents techniques:**
- `BOT_SETUP_GUIDE.md` — Guide de configuration
- `PLAN_SKILLS.md` — Plan des skills Odoo
- `MEMORY.md` — Mémoire à long terme

**Skill French Learning:**
- `skills/french-learning/SKILL.md` — Instructions complètes
- `skills/french-learning/references/LESSON_CALENDAR.md` — Planning jour par jour
- `skills/french-learning/references/GRAMMAR_EXAMPLES.md` — Règles de grammaire
- `skills/french-learning/references/VOCAB_THEMES.md` — Vocabulaire thématique

**Scripts:**
- `generate_daily_lesson.py` — Générateur de leçons
- `customize_plan.py` — Customisation de plan

---

## 🔗 Liens Utiles

**GitHub:** https://github.com/Elhidaoui49/Rental

**Bot Telegram:** @daily_doxo_bot

---

## 💪 Motivation

**"Consistances > Perfection"**

Chaque jour que tu pratiques, tu progresses. Même si c'est difficile, continue:
- 20 minutes de grammaire
- 20 minutes de vocabulaire
- 20 minutes de parole
- 20 minutes d'écriture
- 20 minutes de lecture

**Tu progresses déjà !** 🚀

---

*Créé par: DOXO*
*Date: 2026-02-05*
