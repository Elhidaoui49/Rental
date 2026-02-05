# Digiparc - Analyse Comparative & Stratégie Odoo

**Date:** 2026-02-05
**Par:** DOXO

---

## 1. Comparatif Odoo Fleet vs Digiparc

### 1.1 Feature Matrix

| Fonctionnalité | Digiparc | Odoo Fleet Standard | Gap Odoo |
|----------------|----------|---------------------|----------|
| **Gestion Véhicules** | ✅ | ✅ | - |
| **Maintenance** | ✅ Avancée | ✅ Basic | Planification préventive limitée |
| **Carburant** | ✅ Temps réel | ❌ | Module manquant |
| **Sinistres** | ✅ | ❌ | Custom requis |
| **Chauffeurs** | ✅ Complet | ✅ Basic | RH limité |
| **Géolocalisation** | ✅ Temps réel | ❌ | Intégration GPS requis |
| **Geofencing** | ✅ | ❌ | Custom / API |
| **Workflows** | ✅ Sur-mesure | ⚠️ Studio | Limité |
| **Mobile Chauffeurs** | ✅ App dédiée | ⚠️ Odoo Mobile | Expérience limitée |
| **TCO Analytics** | ✅ Avancé | ⚠️ Basic | BI requis |
| **Reporting** | ✅ Complet | ✅ Basic | Personnalisation |

---

## 2. Architecture Technique Recommandée pour Odoo

### 2.1 Stack Odoo 18

```
Core Modules:
- fleet                    # Gestion véhicules de base
- fleet_vehicle_costs      # Coûts
- fleet_vehicle_logs_services  # Logs maintenance

Custom Modules (à développer):
- rental_core              # Cœur location
- rental_gps               # Intégration GPS (Traccar API)
- rental_maintenance       # Maintenance avancée
- rental_fuel              # Suivi carburant
- rental_tco               # Calcul TCO
- rental_report           # Rapports avancés
- rental_mobile            # API mobile chauffeurs

Intégrations Tiers:
- Traccar (Open Source GPS)  # Géolocalisation
- SendGrid / Mailgun        # Notifications
- Matplotlib / Bokeh        # Graphiques avancés
```

### 2.2 Diagramme Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Frontend                               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                   │
│  │ Odoo Web │  │ Odoo POS │  │ Mobile App│                   │
│  └──────────┘  └──────────┘  └──────────┘                   │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   Odoo 18 Core                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                   │
│  │  Fleet   │  │ Rental   │  │  Report  │                   │
│  └──────────┘  └──────────┘  └──────────┘                   │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Custom Modules (Python)                 │   │
│  │  - GPS Integration (Traccar API)                    │   │
│  │  - TCO Calculation Engine                          │   │
│  │  - Fuel Consumption Logic                          │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                           │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│   Traccar      │ │ PostgreSQL    │ │ Redis Queue   │
│   GPS Server   │ │ (Odoo DB)     │ │ (Async jobs)  │
└────────────────┘ └────────────────┘ └────────────────┘
```

---

## 3. Roadmap Développement

### 3.1 Phase 1: Foundation (Weeks 1-4)

**Objectif:** Base fleet fonctionnelle

**Tâches:**
```bash
# 1. Créer structure module
odoo scaffold rental_module /path/to/addons

# 2. Définir modèles core
# - rental.vehicle (hérite de fleet.vehicle)
# - rental.contract
# - rental.line

# 3. Installer Odoo avec Fleet
pip install -r requirements.txt
```

**Deliverables:**
- Module `rental_core` installé
- CRUD véhicules
- CRUD contrats de location

### 3.2 Phase 2: Maintenance Avancée (Weeks 5-8)

**Fonctionnalités:**
- Planification préventive
- Alertes maintenance
- Historique interventions

**Tâches:**
```python
# rental_maintenance/models/vehicle.py
class VehicleMaintenance(models.Model):
    _name = 'rental.vehicle.maintenance'
    _description = 'Maintenance Schedule'

    vehicle_id = fields.Many2one('rental.vehicle', required=True)
    maintenance_type = fields.Selection([
        ('preventive', 'Préventive'),
        ('corrective', 'Corrective'),
    ], required=True)
    scheduled_date = fields.Datetime(required=True)
    completed = fields.Boolean(default=False)
```

### 3.3 Phase 3: Intégration GPS (Weeks 9-12)

**Stack:** Traccar (Open Source) + API Odoo

**Architecture:**
```
Véhicule GPS Device → Traccar Server → API Odoo
```

**Tâches:**
```python
# rental_gps/models/gps.py
import requests

class TraccarAPI:
    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.headers = {'Authorization': f'Bearer {token}'}

    def get_positions(self):
        """Récupère positions en temps réel"""
        resp = requests.get(
            f'{self.url}/api/positions',
            headers=self.headers
        )
        return resp.json()

    def get_device_info(self, device_id):
        """Info véhicule"""
        resp = requests.get(
            f'{self.url}/api/devices/{device_id}',
            headers=self.headers
        )
        return resp.json()
```

**Cron Odoo:**
```xml
<odoo>
    <data noupdate="1">
        <record id="ir_cron_gps_sync" model="ir.cron">
            <field name="name">GPS Sync</field>
            <field name="model_id" ref="model_rental_gps_log"/>
            <field name="code">model.sync_gps_positions()</field>
            <field name="interval_number">5</field>
            <field name="interval_type">minutes</field>
        </record>
    </data>
</odoo>
```

### 3.4 Phase 4: TCO & Reporting (Weeks 13-16)

**TCO Formula:**
```
TCO = (Coût Achat + Carburant + Maintenance + Assurance +
       Pneus + Poids lourds + Valeur résiduelle)
     / Kilométrage Total
```

**Tâches:**
```python
# rental_tco/models/vehicle.py
class VehicleTCO(models.Model):
    _name = 'rental.vehicle.tco'

    vehicle_id = fields.Many2one('rental.vehicle', required=True)
    purchase_cost = fields.Float()
    fuel_cost = fields.Float(compute='_compute_costs')
    maintenance_cost = fields.Float(compute='_compute_costs')
    insurance_cost = fields.Float(compute='_compute_costs')
    total_cost = fields.Float(compute='_compute_total')
    tco_per_km = fields.Float(compute='_compute_tco')
    mileage = fields.Float()

    def _compute_costs(self):
        # Compute from related records
        pass

    @api.depends('total_cost', 'mileage')
    def _compute_tco(self):
        for rec in self:
            if rec.mileage > 0:
                rec.tco_per_km = rec.total_cost / rec.mileage
```

---

## 4. Estimation Temps & Coûts

### 4.1 Par Phase

| Phase | Durée | Dev Hours | Est. Devs | Coût (Dev) |
|-------|-------|------------|-----------|------------|
| Foundation | 4 sem | 160h | 1 | - |
| Maintenance | 4 sem | 160h | 1 | - |
| GPS | 4 sem | 200h | 1-2 | - |
| TCO/Reporting | 4 sem | 160h | 1 | - |
| Mobile App | 6 sem | 240h | 2 | - |
| Testing/UAT | 2 sem | 80h | - | - |
| **Total** | **24 sem** | **1000h** | - | - |

### 4.2 Coûts Infrastructure

| Composant | Coût Mensuel | Notes |
|-----------|--------------|-------|
| Odoo Cloud | $50-200 | Dépend plan |
| Traccar VPS | $20-50 | 1-2 GB RAM |
| PostgreSQL | Inclus | Dans Odoo |
| Mobile Backend | $10-20 | API hosting |
| **Total** | **$80-270** | Approximatif |

---

## 5. Différenciation vs Digiparc

### 5.1 Avantages Odoo

1. **Open Source:** Pas de license vendor lock-in
2. **Flexibilité:** Custom illimité
3. **Écosystème:** 80,000+ modules
4. **Prix:** Infrastructure self-hosted possible
5. **Intégration:** CRM, Vente, Comptabilité inclus

### 5.2 Points à Renforcer

1. **UX:** Digiparc UX est supérieure (design moderne)
2. **GPS:** Odoo n'a pas GPS natif
3. **Mobile:** App chauffeurs limitée
4. **Support:** Odoo vs Customer Success Digiparc

---

## 6. Stratégie de Lancement

### 6.1 MVP (Minimum Viable Product)

**Fonctionnalités v1:**
- Gestion véhicules + locations
- Maintenance basique
- Rapports simples
- GPS read-only (pas geofencing)

**Go-to-market:** 3 mois

### 6.2 v2 (3-6 mois)

- Maintenance préventive
- Carburant tracking
- GPS temps réel
- Geofencing basic

### 6.3 v3 (6-12 mois)

- TCO analytics avancé
- Workflows sur-mesure
- Mobile app chauffeurs
- Intégrations API tierces

---

## 7. Technologies Recommandées

### 7.1 Backend

```
Python 3.11+
Odoo 18.0
PostgreSQL 16
Redis 7 (Queue)
Celery (Jobs async)
```

### 7.2 Frontend

```
Odoo Web (QWeb)
Odoo OWL Framework (Components)
Bootstrap 5
Vue.js (si custom frontend needed)
```

### 7.3 Mobile

```
Option A: Odoo Mobile (limité)
Option B: Flutter/React Native (recommandé)
  - API REST Odoo
  - Offline mode
  - Push notifications
```

### 7.4 GPS

```
Traccar (Open Source) - Recommandé
- Self-hosted
- REST API
- Supports 5000+ devices
- Geofencing natif

Alternatives:
- GPS Trackit (Paid)
- Fleetio (Paid SaaS)
```

---

## 8. Architecture Base de Données

### 8.1 Schéma Simplifié

```sql
-- Véhicules (extends fleet.vehicle)
CREATE TABLE rental_vehicle (
    id SERIAL PRIMARY KEY,
    gps_device_id VARCHAR(50),
    gps_token VARCHAR(100),
    tco_per_km DECIMAL(10,2),
    last_maintenance_date DATE,
    next_maintenance_date DATE
);

-- Contrats Location
CREATE TABLE rental_contract (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES res_partner(id),
    vehicle_id INTEGER REFERENCES rental_vehicle(id),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    daily_rate DECIMAL(10,2) NOT NULL,
    total_amount DECIMAL(12,2),
    status VARCHAR(20) -- draft, confirmed, active, completed, cancelled
);

-- GPS Logs
CREATE TABLE rental_gps_log (
    id SERIAL PRIMARY KEY,
    vehicle_id INTEGER REFERENCES rental_vehicle(id),
    latitude DECIMAL(10,6) NOT NULL,
    longitude DECIMAL(10,6) NOT NULL,
    speed DECIMAL(6,2),
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    altitude DECIMAL(6,2),
    direction DECIMAL(6,2)
);

-- Maintenance
CREATE TABLE rental_maintenance (
    id SERIAL PRIMARY KEY,
    vehicle_id INTEGER REFERENCES rental_vehicle(id),
    maintenance_type VARCHAR(20), -- preventive, corrective
    description TEXT,
    cost DECIMAL(12,2),
    scheduled_date DATE,
    completed_date DATE,
    mechanic_id INTEGER REFERENCES res_users(id),
    status VARCHAR(20) -- scheduled, in_progress, completed
);

-- Carburant
CREATE TABLE rental_fuel (
    id SERIAL PRIMARY KEY,
    vehicle_id INTEGER REFERENCES rental_vehicle(id),
    quantity_liters DECIMAL(8,2) NOT NULL,
    cost DECIMAL(10,2) NOT NULL,
    station_id INTEGER REFERENCES rental_fuel_station(id),
    date DATE NOT NULL,
    odometer_reading INTEGER NOT NULL,
    consumption_per_100km DECIMAL(6,2)
);
```

---

## 9. Conclusion

### 9.1 Faisabilité

✅ **Faisable:** Reproduire 80% Digiparc avec Odoo + custom

### 9.2 Effort

- **MVP:** 3 mois, 1 dev full-time
- **Full feature parity:** 6-12 mois, 2-3 devs

### 9.3 Recommandation

1. **MVP focus:** Fleet + Maintenance basique
2. **GPS strategy:** Traccar self-hosted (cost-effective)
3. **UX priority:** Investir dans interface mobile
4. **Differentiation:** TCO analytics + workflows Odoo
5. **Pricing:** Compete with Digiparc (SaaS model)

---

**Document généré par:** DOXO
**Date:** 2026-02-05
**Version:** 1.0
