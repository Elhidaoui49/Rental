# MEMORY.md - DOXO's Long-Term Memory

## 2026-02-05

### Workspace Setup
- **GitHub:** `https://github.com/Elhidaoui49/Rental.git`
- **Auth:** Personal Access Token (Classic) stored in git history - use new token for future
- **Workspace:** `/home/Simocrm/.openclaw/workspace`

### Projects

#### SimoCRM Rental Module (Odoo 18.0)
- **Focus:** Fleet management, vehicle rental, used car business
- **Goal:** Compete with Digiparc ERP for fleet management

#### Research Completed
1. **Digiparc Analysis** (`research/digiparc-documentation.md`)
   - Complete feature set: Maintenance, Fuel, Accidents, Driver HR, GPS tracking, Geofencing
   - Cloud SaaS + On-Premise deployment
   - TCO analytics focus
   - Modern UX, workflows customizable

2. **Odoo vs Digiparc Gap Analysis** (`research/digiparc-analysis.md`)
   - Odoo Fleet: Basic vehicle management
   - Missing: GPS, geofencing, advanced fuel tracking, workflows
   - Roadmap: 6 phases, 24 weeks, 1000 dev hours
   - Stack: Odoo 18 + Traccar (GPS) + Flutter (mobile)

### Technical Stack
- **Odoo:** 18.0
- **Python:** pip for packages
- **JS:** pnpm for frontend
- **GPS:** Traccar (Open Source) - https://www.traccar.org/
- **Mobile:** Flutter or React Native (TBD)
- **Database:** PostgreSQL

### GitHub Token Management
- **Current token:** Stored in git history (security risk)
- **Future:** Generate new token, store securely (never commit to git)
- **Repos:**
  - `Elhidaoui49/Rental` - Main project
  - Permissions: admin, push, pull

### Key Decisions
1. **GPS Integration:** Use Traccar (self-hosted, REST API, 5000+ devices)
2. **MVP Priority:** Fleet core + contracts + basic maintenance (3 months)
3. **Architecture:** Odoo core + custom modules + Traccar API
4. **TCO Focus:** Differentiator vs Digiparc - advanced cost analytics

### Workflow Notes
- User: Mohamed (@Elhidaoui49)
- Languages: English, French, Moroccan Darija
- Vibe: Direct, technical, CLI-first
- Context: Polyglot developer (Odoo, Laravel, React, Business Central)

### Files to Reference
- `research/digiparc-documentation.md` - Digiparc feature reference
- `research/digiparc-analysis.md` - Odoo roadmap and architecture
- `IDENTITY.md` - DOXO profile
- `USER.md` - Mohamed profile

---

### Telegram Bot — French Learning

- **Bot name:** DoxoFrenchBot (@daily_doxo_bot)
- **Token:** `8599447054:AAFM6Xv-Q2TMLS8j6jhOITxFU6os7KT4vJo`
- **Purpose:** Daily French lessons (A2 → B2 in 3-5 months)
- **Schedule:** Morning (9:00 AM) + Evening (8:00 PM) notifications
- **Commands:** /start, /lesson, /vocab, /grammar, /exercise, /progress

---

*Last updated: 2026-02-05*
