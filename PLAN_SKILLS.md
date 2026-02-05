# Skills Plan - Expert Odoo Technical Consultant (15+ Years)

**Target Role:** Senior Odoo Technical Architect / Consultant
**Experience Level:** 15+ years
**Date:** 2026-02-05

---

## Executive Summary

This skill set is designed for an expert Odoo consultant who needs to:
- Develop complex Odoo modules quickly
- Troubleshoot and debug efficiently
- Integrate Odoo with external systems
- Optimize performance at scale
- Handle migrations and upgrades
- Provide technical leadership

**Total Skills Planned:** 9 skills
**Estimated Implementation Time:** 2-3 weeks

---

## Skill Matrix

| Skill | Priority | Est. Time | Dependencies | Business Impact |
|-------|----------|------------|--------------|-----------------|
| `odoo-module-builder` | P0 | 3-4 days | - | Foundation - module scaffolding |
| `odoo-debug` | P0 | 2-3 days | - | Daily debugging |
| `odoo-integration` | P1 | 4-5 days | - | Client integrations |
| `odoo-migration` | P1 | 3-4 days | `odoo-module-builder` | Upgrades |
| `odoo-perf` | P2 | 3-4 days | - | Performance |
| `odoo-api` | P2 | 2-3 days | `odoo-integration` | API development |
| `odoo-security` | P2 | 2-3 days | - | Hardening |
| `odoo-deploy` | P3 | 2-3 days | - | DevOps |
| `odoo-consulting` | P3 | 1-2 days | - | Business analysis |

---

## Skill Specifications

### 1. `odoo-module-builder` (P0)
**Description:** Rapid Odoo module scaffolding with best practices for Odoo 18.0+. Use when creating new modules, customizing existing ones, or extending Odoo functionality with models, views, security, and migrations.

**Scope:**
- Scaffold module structure (`__init__.py`, `__manifest__.py`, models/, views/, etc.)
- Define models with proper inheritance (Model.TransientModel, AbstractModel)
- Create views (tree, form, kanban, calendar, graph, pivot)
- Write security rules (ir.rule, ir.model.access.csv)
- Generate XML data files (records, actions, menus)
- Add automated migrations (hooks)

**Concrete Examples:**
- "Create a rental_contract module with contract model and status workflow"
- "Extend fleet.vehicle to add GPS tracking fields"
- "Generate a maintenance schedule model with scheduled actions"
- "Add a wizard for bulk vehicle assignment"

**Resources:**
- `scripts/scaffold_module.py` — CLI to scaffold module
- `references/model_patterns.md` — Common model patterns (many2one, one2many, computed fields)
- `references/view_examples.md` — View templates and widgets
- `assets/manifest_template.py` — __manifest__.py template

---

### 2. `odoo-debug` (P0)
**Description:** Systematic Odoo debugging workflow for production and development issues. Use when investigating errors, crashes, performance issues, or unexpected behavior in Odoo instances.

**Scope:**
- Log analysis (odoo.log, /var/log/, syslog)
- Stack trace decoding and error classification
- Database debugging (pg_stat_statements, deadlock analysis)
- Python debugger integration (pdb, ipdb)
- JavaScript debugging (browser console, OWL dev tools)
- Memory leak detection and profiling

**Concrete Examples:**
- "Odoo crashes on module load — investigate logs"
- "Transaction deadlock detected during high load"
- "RPC call failing in production — debug server response"
- "Memory usage growing over time — profile and identify leaks"

**Resources:**
- `scripts/analyze_logs.py` — Parse and filter odoo.log
- `scripts/profiling.py` — Memory/CPU profiling hooks
- `references/error_codes.md` — Common Odoo error patterns
- `references/debugging_checklist.md` — Systematic debugging process

---

### 3. `odoo-integration` (P1)
**Description:** Connect Odoo with external systems via REST API, SOAP, message queues, and scheduled jobs. Use when integrating Odoo with third-party ERPs, payment gateways, shipping carriers, or custom APIs.

**Scope:**
- External API clients (requests, zeep for SOAP)
- REST API development (controllers, JSON-RPC)
- Message queues (Celery, RabbitMQ, Redis Queue)
- Webhooks (incoming, outgoing)
- Authentication flows (OAuth2, API keys, JWT)
- Error handling and retry logic

**Concrete Examples:**
- "Integrate Odoo with WooCommerce for product sync"
- "Connect to Traccar GPS API for vehicle tracking"
- "Build REST API endpoint for mobile app"
- "Set up webhook handler for Stripe payments"

**Resources:**
- `scripts/api_client_template.py` — Reusable API client pattern
- `scripts/webhook_handler.py` — Webhook validation and routing
- `references/integration_patterns.md` — Queue patterns, idempotency
- `references/auth_flows.md` — OAuth2, JWT examples

---

### 4. `odoo-migration` (P1)
**Description:** Migrate Odoo instances between versions, databases, or environments. Use for upgrades (e.g., 17→18), data imports, or staging→production sync.

**Scope:**
- Pre-migration analysis (module compatibility, custom code review)
- OpenUpgrade workflow (if applicable)
- Data migration scripts (Python)
- Module updates and conflicts resolution
- Post-migration validation and testing
- Rollback procedures

**Concrete Examples:**
- "Migrate Odoo 17 database to 18.0"
- "Import legacy CRM data into Odoo"
- "Sync staging changes to production safely"
- "Upgrade rental module with data migration"

**Resources:**
- `scripts/analyze_dependencies.py` — Check module dependencies
- `scripts/migrate_data.py` — Data transformation templates
- `references/migration_checklist.md` — Step-by-step upgrade process
- `references/upgrade_notes.md` — Version-specific changes

---

### 5. `odoo-perf` (P2)
**Description:** Optimize Odoo performance for high-load environments. Use when instances are slow, database queries are inefficient, or scaling is needed.

**Scope:**
- Query optimization (EXPLAIN ANALYZE, indexing)
- Caching strategies (Redis, Memcached, ORM cache)
- Database tuning (postgresql.conf, connection pooling)
- Python profiling (cProfile, line_profiler)
- Frontend optimization (bundle size, lazy loading)
- Load testing and benchmarking

**Concrete Examples:**
- "Database queries slow — optimize indexes and queries"
- "High CPU usage during report generation"
- "Frontend slow loading — optimize bundles"
- "Scale Odoo for 1000+ concurrent users"

**Resources:**
- `scripts/analyze_queries.py` — Identify slow queries
- `scripts/profile_odoo.py` — Profiling decorator
- `references/perf_patterns.md` — Caching, batch operations
- `references/postgresql_tuning.md` — pg_conf tuning guide

---

### 6. `odoo-api` (P2)
**Description:** Build and consume Odoo REST APIs and external API integrations. Use when creating API endpoints for mobile apps, external systems, or microservices.

**Scope:**
- Controller development (http.Controller)
- Authentication (api_key, JWT, OAuth2)
- Rate limiting and CORS
- API versioning
- Documentation (OpenAPI/Swagger)
- Error handling and validation

**Concrete Examples:**
- "Create REST API for rental contracts"
- "Build authenticated endpoint for mobile app"
- "Add rate limiting to public API"
- "Generate OpenAPI docs for endpoints"

**Resources:**
- `scripts/api_decorator.py` — Reusable auth/limiting decorator
- `scripts/swagger_gen.py` — Generate OpenAPI docs
- `references/api_patterns.md` — REST design patterns
- `references/auth_methods.md` — API authentication methods

---

### 7. `odoo-security` (P2)
**Description:** Secure Odoo instances against vulnerabilities and enforce access controls. Use when auditing security, hardening deployments, or implementing complex access rules.

**Scope:**
- Security audits (known vulnerabilities, dependencies)
- Access rules and record rules
- CSRF/XSS protection
- SQL injection prevention
- File upload validation
- Secret management (encryption, environment variables)

**Concrete Examples:**
- "Audit rental module for security vulnerabilities"
- "Implement multi-tenant data isolation with record rules"
- "Secure file upload endpoints"
- "Rotate secrets in production"

**Resources:**
- `scripts/security_audit.py` — Scan for common vulnerabilities
- `references/security_checklist.md` — OWASP-based checklist
- `references/access_rules.md` — Record rule patterns
- `references/encryption.md` — Secret management

---

### 8. `odoo-deploy` (P2 → P3)
**Description:** Deploy and manage Odoo instances using Docker, Kubernetes, or traditional methods. Use when setting up new instances, scaling, or managing multi-environment deployments.

**Scope:**
- Docker containerization (Dockerfile, docker-compose)
- Kubernetes deployment (Helm charts, Ingress)
- Database backups and disaster recovery
- SSL/TLS configuration
- Load balancing (Nginx, HAProxy)
- Monitoring and alerting (Prometheus, Grafana)

**Concrete Examples:**
- "Deploy Odoo 18 to Docker Swarm"
- "Set up multi-environment (dev/stage/prod)"
- "Configure automated backups with pg_dump"
- "Scale Odoo horizontally with Kubernetes"

**Resources:**
- `scripts/deploy_docker.py` — Docker deployment automation
- `scripts/backup_odoo.py` — Automated backup script
- `references/docker_patterns.md` — Dockerfile templates
- `references/k8s_helm.md` — Kubernetes deployment guide

---

### 9. `odoo-consulting` (P3)
**Description:** Guide Odoo business analysis, requirements gathering, and solution design. Use when architecting solutions for clients, scoping projects, or conducting technical assessments.

**Scope:**
- Requirements elicitation (workshops, interviews)
- Gap analysis (Odoo vs custom needs)
- Solution architecture design
- Estimation and planning
- Technical proposal writing
- Knowledge transfer and training

**Concrete Examples:**
- "Analyze client needs and propose Odoo modules"
- "Design architecture for rental business + WooCommerce"
- "Estimate development effort for TCO analytics module"
- "Create technical proposal for GPS integration"

**Resources:**
- `references/requirements_template.md` — Requirements gathering template
- `references/gap_analysis_framework.md` — Analysis methodology
- `references/estimation_guide.md` — Effort estimation patterns
- `references/proposal_template.md` — Technical proposal structure

---

## Implementation Roadmap

### Week 1: Foundation Skills
- Day 1-4: `odoo-module-builder`
- Day 5-7: `odoo-debug`

**Deliverables:**
- Module scaffolding CLI tested on rental_core
- Debug workflow validated on sample errors

### Week 2: Core Integration
- Day 1-5: `odoo-integration`
- Day 6-9: `odoo-migration`

**Deliverables:**
- Traccar API integration tested
- WooCommerce sync module prototype
- Migration script for dummy data

### Week 3: Advanced Skills (P2)
- Day 1-4: `odoo-perf`
- Day 5-7: `odoo-api` or `odoo-security`

**Deliverables:**
- Performance profiling on demo Odoo
- REST API endpoint for rental contracts
- Security audit checklist

### Week 4 (Optional): Completion
- Day 1-3: Remaining P2/P3 skills
- Day 4-5: Testing and validation across all skills

---

## Validation Criteria

Each skill must pass:

1. **Functional Test:** Skill works on 3+ real examples
2. **Integration Test:** Works with other skills (e.g., `odoo-module-builder` + `odoo-integration`)
3. **Token Efficiency:** SKILL.md < 500 lines, references loaded on-demand
4. **Documentation:** Clear "when to use" in description
5. **Reusability:** Scripts tested and deterministic

---

## Business Impact

**Immediate (Weeks 1-2):**
- 50% faster module development
- Systematic debugging (less time lost)
- Integration work streamlined

**Medium-term (Weeks 3-4):**
- Performance optimization capability
- Security hardening
- API development ready

**Long-term:**
- Competitive advantage as expert consultant
- Reduced technical debt
- Knowledge preservation in skills

---

## Questions for Validation

Before implementation, validate:

1. **Priorities:** Is P0/P1/P2 ranking correct for your use case?
2. **Scope:** Are there missing skills for expert consulting?
3. **Resources:** Do you need specific tools/platforms covered (e.g., AWS, specific payment gateways)?
4. **Timeframe:** 3 weeks acceptable? Skills can be delivered incrementally.

---

**Plan created by:** DOXO
**Date:** 2026-02-05
**Version:** 1.0
