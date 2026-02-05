# Guide de Configuration — Doxo French Bot

**Bot Telegram:** DoxoFrenchBot (daily_doxo_bot)
**Token:** `8599447054:AAFM6Xv-Q2TMLS8j6jhOITxFU6os7KT4vJo`

---

## 1. Vérifier le Bot

**Ouvre Telegram et teste:**

1. Ouvre ton bot: `@daily_doxo_bot`
2. Envoie: `/start`
3. Le bot devrait répondre avec un message

---

## 2. Structure des Notifications

Le bot enverra 2 messages par jour:

### 🌅 Matin (9:00 AM)
```
📚 Leçon du Jour
- Grammaire du jour
- Vocabulaire (10 mots)
- Exercice de pratique
```

### 🌙 Soir (20:00 PM)
```
📝 Rappel du Soir
- Avez-vous pratiqué ?
- Révision rapide
- Motivation
```

---

## 3. Commandes du Bot

| Commande | Description |
|----------|-------------|
| `/start` | Commencer les leçons |
| `/lesson` | Leçon du jour |
| `/vocab` | Vocabulaire du jour |
| `/grammar` | Règle de grammaire |
| `/exercise` | Exercice de pratique |
| `/progress` | Voir ton progrès |
| `/edit_plan` | Modifier le plan d'apprentissage |
| `/schedule` | Voir/Modifier l'horaire des notifications |
| `/reset` | Recommencer le plan (retour jour 1) |

---

## 4. Première Leçon (Jour 1)

**Si le bot est configuré, la première leçon sera:**

```
📚 Leçon 1: Verbes fréquents (er)

🌅 Matin — 1 heure

⏱️ 20 min — Grammaire
Verbes en -er: je parle, tu parles, il/elle parle, nous parlons, vous parlez, ils/elles parlent

⏱️ 20 min — Vocabulaire (Travailler)
1. Travailler — Je travaille dans une entreprise
2. L'entreprise — L'entreprise est grande
3. Le bureau — Mon bureau est au 2ème étage
4. Le collègue — Mon collègue est sympa
5. Le patron — Le patron arrive demain

⏱️ 20 min — Écoute
Écoute un court dialogue français

🌞 Après-midi — 1 heure

⏱️ 20 min — Parler
Raconte ta journée en français (2 minutes)

⏱️ 20 min — Écrire
Écris 5 phrases sur ton travail

⏱️ 20 min — Lecture
Lis un texte court, note les structures

💪 Exercice du jour
Écris 10 phrases en utilisant des verbes en -er (parler, travailler, manger, finir, etc.)

🚨 Règle d'or
Consistances > Perfection. Parle avant d'être "prêt" !
```

---

## 5. Utilisation Quotidienne

**Routine recommandée:**

**📅 Matin (9:00):**
- Reçois la leçon du jour
- Lis la grammaire (20 min)
- Apprends le vocabulaire (20 min)
- Écoute un dialogue (20 min)

**🕐 Après-midi (17:00):**
- Parle pendant 2 minutes (monologue)
- Écris 5-10 phrases
- Lis un texte court

**🌙 Soir (20:00):**
- Reçois le rappel du soir
- Réponds: Oui/Non pour avoir pratiqué
- Note les erreurs à corriger

---

## 6. Progrès Mensuel

**Mois 1 (A2 → B1):**
- Objectif: Parler sans bloquer
- Moins d'erreurs graves
- Grammaire de base maîtrisée

**Mois 2 (B1):**
- Objectif: Connecter les idées
- Expliquer et comparer
- Parler 2-3 minutes sans pause

**Mois 3-5 (B1 → B2):**
- Objectif: Défendre une opinion
- Nuancer
- Vocabulaire précis

---

## 7. Modifier le Plan d'Apprentissage

### Commande `/edit_plan`

Pour modifier ton plan, envoie:
```
/edit_plan
```

**Options:**

**1. Changer le niveau:**
```
/edit_plan niveau B1
/edit_plan niveau B2
```

**2. Changer l'intensité:**
```
/edit_plan 2h
/edit_plan 1h
```

**3. Sauter des jours:**
```
/edit_plan jour 10
/edit_plan jour 20
```

**4. Changer l'horaire des notifications:**
```
/edit_plan matin 8h
/edit_plan soir 21h
```

**5. Personnaliser les thèmes:**
```
/edit_plan thème business
/edit_plan thème santé
```

### Commande `/schedule`

Pour voir ou modifier l'horaire:
```
/schedule
```

**Réponses:**
- Notification matinale: 9h00 (ou modifié)
- Notification du soir: 20h00 (ou modifié)
- Temps total d'étude: 2h/jour (ou modifié)

**Modifier l'horaire:**
```
/schedule matin 8h soir 21h
```

---

## 8. Personnalisation Avancée

Si tu veux un plan complètement personnalisé, dis-moi:

**Options:**
1. **Objectif spécifique:** "Je veux passer un examen DELF B2 en 3 mois"
2. **Thème spécifique:** "Je veux apprendre le français pour le business"
3. **Format spécifique:** "Je veux des leçons de 30 minutes, pas 1 heure"
4. **Pays/Région:** "Je veux apprendre le français de France / du Québec"

**Exemple de demande:**
```
/edit_plan
Objectif: DELF B2 en 3 mois
Thème: Business international
Format: Leçons courtes (30 min)
```

Je vais créer un plan personnalisé pour toi.

---

## 9. Problèmes et Solutions

**Problème: Bot ne répond pas**
- Solution: Vérifie que le token est correct
- Solution: Redémarre le bot

**Problème: Notifications pas reçues**
- Solution: Vérifie que le bot a les permissions
- Solution: Vérifie tes réglages Telegram

**Problème: Leçon trop difficile**
- Solution: Dis-moi "facile" et je simplifie
- Solution: Révision des leçons précédentes

---

## 8. Contact Support

**Pour toute question ou problème:**
- Message le bot: `/help`
- Me contacter via ce chat
- Créer un issue sur GitHub

---

## 9. Prochaines Étapes

**1. Teste le bot maintenant:**
```
Ouvre @daily_doxo_bot
Envoie: /start
```

**2. Si fonctionne:**
- Tu recevras la première leçon demain matin à 9h

**3. Si ne fonctionne pas:**
- Dis-moi et je corrigerai la configuration

---

**Bon courage ! Tu progresses déjà 💪**

---

*Créé par: DOXO*
*Date: 2026-02-05*
