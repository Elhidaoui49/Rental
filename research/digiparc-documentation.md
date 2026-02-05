# Digiparc - Documentation Technique & Analyse Fonctionnelle

**Source:** https://digiparc.com
**Type:** ERP SaaS / On-Premise pour gestion de flotte automobile
**Analyse:** 2026-02-05

---

## 1. Vue d'Ensemble

Digiparc est une plateforme ERP complète pour la gestion de flotte automobile, centralisant:

- Maintenance
- Carburant
- Sinistres
- RH chauffeurs
- Workflows personnalisés
- Géolocalisation GPS

**Modèle de déploiement:**
- SaaS (Cloud)
- On-Premise (serveurs clients)

---

## 2. Modules & Fonctionnalités

### 2.1 Maintenance

**Fonctionnalités:**
- Suivi des interventions techniques
- Planification de maintenance préventive
- Historique complet par véhicule
- Alertes préventives
- Analyse des coûts par poste de dépense
- Rapports détaillés sur pannes, entretiens, coûts

**Objectifs:**
- Améliorer la disponibilité de la flotte
- Réduire les temps d'arrêt
- Optimiser les coûts de maintenance

### 2.2 Carburant

**Fonctionnalités:**
- Suivi en temps réel de la consommation
- Analyse des comportements de conduite
- Détection d'anomalies de consommation
- Rapports sur performances de la flotte

### 2.3 Sinistres / Accidents

**Fonctionnalités:**
- Gestion des déclarations de sinistre
- Suivi des dossiers d'assurance
- Historique par véhicule

### 2.4 Gestion des Chauffeurs (RH)

**Fonctionnalités:**
- Profils chauffeurs
- Suivi des comportements de conduite
- Assignation de véhicules
- Gestion des temps de travail

### 2.5 Transport / Missions

**Fonctionnalités:**
- Planification des missions
- Suivi des trajets
- Organisation des transports
- Chevauchement des missions (évité)
- Interface client professionnelle

### 2.6 Géolocalisation GPS

**Fonctionnalités:**
- Suivi en temps réel (24h/24)
- Position exacte sur carte interactive
- Géolocalisation de véhicules légers et lourds
- Analyse des comportements de conduite
- **GEOFENCING:** Zones géographiques personnalisées
  - Alertes entrée/sortie de zones
  - Alertes dépassement de vitesse
- Rapports consommation de carburant
- Historique des trajets

**Avantages:**
- Visibilité complète sur la flotte
- Réactivité face aux anomalies
- Sécurité des conducteurs

### 2.7 Workflows Personnalisés

**Fonctionnalités:**
- Workflows sur-mesure
- Champs personnalisés
- Paramétrage fin selon métier
- Automatisation des processus

---

## 3. Caractéristiques Techniques

### 3.1 Architecture

- **Cloud Native:** SaaS accessibles via navigateur
- **On-Premise:** Déploiement sur serveurs clients (infrastructures critiques/souveraines)
- **Multi-device:** Accès mobile, desktop

### 3.2 Sécurité

- **Datacenters:** Tier-4 certifiés ISO
- **Chiffrement:** Bout-en-bout
- **Redondance:** Géographique horaire
- **Conformité:** Évolutive avec législation

### 3.3 UX / Interface

- Design moderne et intuitif
- Formation en minutes pour équipes opérationnelles
- Dashboard en temps réel
- Rapports personnalisables

---

## 4. Avantages Clés

### 4.1 Centralisation
- Single Source of Truth
- 100% de l'activité flotte centralisée
- Plus de fichiers Excel dispersés
- Données fiables en temps réel

### 4.2 Productivité
- Automatisation des processus
- Rapports disponibles en un clic
- Décisions basées sur données récentes
- Réduction des tâches papier

### 4.3 ROI / Coûts

**Réduction des coûts:**
- TCO (Total Cost of Ownership) optimisé
- Maîtrise des dépenses carburant
- Optimisation des coûts de maintenance
- Réduction des temps d'inactivité

**Time-to-Value:**
- Opérationnel en jours (pas mois)
- Migration rapide des données existantes
- Économies dès la première semaine

### 4.4 Innovation Continue

- Mises à jour automatiques
- Nouvelles fonctionnalités IA
- Améliorations hebdomadaires
- Sans frais cachés

---

## 5. Segments Client

**Cible:** Entreprises gestionnaires de flottes

**Secteurs d'activité:**
- Transport logistique
- Location de véhicules
- Services publics
- Entreprises avec flotte commerciale

**Scale:** Centaines d'entreprises dans le monde

---

## 6. Positionnement Concurrentiel

### 6.1 Forces

- ERP complet (pas juste GPS)
- UX moderne (vs ERPs austères)
- Flexibilité métier élevée
- Customer Success dédié
- Innovation continue

### 6.2 Différenciation

- **Cloud + On-Premise:** Flexibilité de déploiement
- **Sécurité bancaire:** Tier-4 ISO
- **Workflows sur-mesure:** Adaptation métier
- **Time-to-Value:** Jours, pas mois

---

## 7. Intégration Technique (Hypothétique)

### 7.1 API Potentielles

Pour intégration avec Odoo ou autres systèmes:

```
Véhicules:
- GET /vehicles - Liste véhicules
- POST /vehicles - Création véhicule
- PUT /vehicles/{id} - Mise à jour

Maintenance:
- GET /vehicles/{id}/maintenance - Historique
- POST /maintenance - Créer intervention

GPS:
- GET /vehicles/{id}/location - Position temps réel
- GET /vehicles/{id}/trips - Historique trajets

Carburant:
- GET /vehicles/{id}/fuel - Consommation
```

### 7.2 Webhooks Probables

```
events:
- vehicle.maintenance.due
- vehicle.geofence.exit
- vehicle.accident.reported
- fuel.anomaly.detected
```

---

## 8. Points d'Attention pour Implémentation Odoo

### 8.1 Modules Odoo Correspondants

**Fleet Management (standard Odoo):**
- `fleet` - Gestion de véhicules
- `fleet_vehicle_costs` - Coûts
- `fleet_vehicle_logs_services` - Maintenance

**À étendre/compléter:**
- **Géolocalisation:** Intégration GPS tiers (ex: GPS Trackit, Traccar)
- **Maintenance avancée:** Planification préventive
- **Carburant:** Suivi consommation détaillé
- **Workflows:** Studio / Automation
- **Rapports avancés:** BI / Reporting

### 8.2 Gaps à combler

| Digiparc | Odoo Standard | Gap |
|----------|---------------|-----|
| Géolocalisation temps réel | ❌ | Intégration GPS requis |
| Geofencing avancé | ❌ | Custom / API externe |
| Workflows sur-mesure | ⚠️ Studio | Limité vs Digiparc |
| TCO analytics | ⚠️ Basic | BI / Reporting avancé |
| Mobile app dédiée chauffeurs | ❌ | Odoo Mobile limité |

### 8.3 Roadmap Suggérée Odoo

**Phase 1: Core Fleet (Odoo standard)**
- Activer module `fleet`
- Configurer véhicules, chauffeurs
- Suivi coûts basiques

**Phase 2: Maintenance**
- Planification préventive
- Historique interventions
- Alertes maintenance

**Phase 3: Intégration GPS**
- API Traccar ou similaire
- Géolocalisation temps réel
- Historique trajets

**Phase 4: Reporting & TCO**
- Rapports personnalisés
- Dashboard TCO
- Export données

**Phase 5: Workflows & Mobile**
- Automation avancée
- Application mobile chauffeurs
- Intégration CRM / Vente

---

## 9. Questions Ouvertes

Pour documentation complète, nécessité de:

1. **Documentation API:** Disponible? Public ou client-only?
2. **Pricing:** Modèle SaaS, on-premise?
3. **Limitations:** Nombre max véhicules, users?
4. **Intégrations:** Connecteurs existants (comptabilité, CRM)?
5. **SLA:** Temps réponse support, uptime garanti?

---

## 10. Conclusion

Digiparc est une solution ERP mature pour gestion de flotte avec:
- Fort positionnement UX
- Sécurité bancaire
- Flexibilité métier
- Innovation continue

**Pour Odoo Rental:**
- Reproduire l'ensemble des fonctionnalités est ambitieux
- Focus sur gaps spécifiques (GPS, workflows avancés)
- Intégration GPS tiers clé pour temps réel
- Reporting TCO différenciant

---

**Document généré par:** DOXO
**Date:** 2026-02-05
**Version:** 1.0
