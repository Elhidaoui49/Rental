# Research - Digiparc & Odoo Fleet Management

Dossier d'analyse pour module Odoo Rental - Étude concurrentielle Digiparc

---

## Documents

### 1. [digiparc-documentation.md](./digiparc-documentation.md)
Documentation technique complète de Digiparc:
- Vue d'ensemble et modules
- Fonctionnalités détaillées (Maintenance, GPS, Carburant, etc.)
- Architecture et sécurité
- Avantages concurrentiels
- Intégration technique

### 2. [digiparc-analysis.md](./digiparc-analysis.md)
Analyse comparative et roadmap Odoo:
- Feature matrix (Digiparc vs Odoo Fleet)
- Architecture technique recommandée
- Roadmap développement par phase
- Estimation temps et coûts
- Stratégie de lancement
- Technologies recommandées
- Schéma base de données

---

## Résumé Exécutif

**Digiparc:** ERP SaaS pour gestion de flotte avec:
- Maintenance, carburant, sinistres, RH chauffeurs
- Géolocalisation GPS temps réel avec geofencing
- Workflows personnalisés
- TCO analytics
- UX moderne

**Gap Odoo:**
- ✅ Fleet standard (base)
- ❌ GPS natif (nécessite intégration)
- ❌ Carburant tracking (custom)
- ❌ Geofencing (custom/API)
- ⚠️ Workflows limités (Studio)

**Roadmap:**
- MVP: 3 mois (Fleet + Maintenance basique)
- Full parity: 6-12 mois (GPS, TCO, Mobile)

**Stack Recommandé:**
- Odoo 18 + Custom modules
- Traccar (Open Source GPS)
- Flutter/React Native (Mobile)

---

## Prochaines Étapes

1. ✅ Documentation Digiparc complète
2. ✅ Analyse comparative
3. 🔲 Prototype MVP (Week 1-4)
4. 🔲 Setup Traccar GPS
5. 🔲 Développement module rental_core

---

**Généré par:** DOXO
**Date:** 2026-02-05
