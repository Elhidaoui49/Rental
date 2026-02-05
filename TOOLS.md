# TOOLS.md - Local Notes

## GitHub

- **Username:** Elhidaoui49
- **Main Repo:** https://github.com/Elhidaoui49/Rental.git
- **Token:** Classic PAT (never commit to git)
- **Setup:**
  ```bash
  git config user.email "Elhidaoui49@users.noreply.github.com"
  git config user.name "Elhidaoui49"
  ```

## Odoo

- **Version:** 18.0
- **Python:** `pip install -r requirements.txt`
- **Module Scaffold:**
  ```bash
  odoo scaffold <module_name> /path/to/addons
  ```
- **Common Commands:**
  ```bash
  odoo -c odoo.conf --dev all  # Dev mode
  odoo -u rental_module -d database  # Update module
  ```

## Traccar (GPS)

- **Website:** https://www.traccar.org/
- **Repo:** https://github.com/traccar/traccar
- **API Base:** `http://<traccar-server>:8082/api`
- **Auth:** Bearer token
- **Key Endpoints:**
  - `GET /api/positions` - Latest positions
  - `GET /api/devices` - Vehicle list
  - `GET /api/devices/{id}` - Vehicle details
  - `GET /api/geofences` - Geofence zones

## Fleet Management

### Core Odoo Modules
- `fleet` - Vehicle management
- `fleet_vehicle_costs` - Cost tracking
- `fleet_vehicle_logs_services` - Maintenance logs

### Custom Modules (Planned)
- `rental_core` - Core rental logic
- `rental_maintenance` - Advanced maintenance
- `rental_fuel` - Fuel tracking
- `rental_gps` - GPS/Traccar integration
- `rental_tco` - TCO calculations
- `rental_report` - Advanced reporting

## Database

- **Engine:** PostgreSQL
- **Connection:** Defined in `odoo.conf`
- **Backup:**
  ```bash
  pg_dump -U odoo -d database > backup.sql
  ```

## Development Workflow

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/module-name

# Commit and push
git add .
git commit -m "feat: description"
git push -u origin feature/module-name
```

### Odoo Module Development
1. Scaffold: `odoo scaffold rental_module addons/`
2. Define models in `models/`
3. Create views in `views/`
4. Add security in `security/`
5. Update `__manifest__.py`
6. Update module: `odoo -u rental_module -d db`

## TCO Calculation

**Formula:**
```
TCO = (Purchase Cost + Fuel + Maintenance + Insurance +
       Tires + Heavy Costs + Residual Value)
     / Total Mileage
```

**Odoo Fields:**
- `fleet.vehicle.purchase_cost`
- `fleet.vehicle.cost` (linked records)
- `fleet.vehicle.odometer` (mileage)

---

*Last updated: 2026-02-05*
