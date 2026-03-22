---
name: guido-scale
version: 1.0.0
author: Guido Miranda Mercado (GuiMiran)
repository: https://github.com/GuiMiran/guido-sdd-migration-effort-scale
category: engineering-maturity
compatible_with: [claude, chatgpt, gpt-4o, codex, gemini]
tags:
  - maturity-model
  - sdd
  - spec-driven-development
  - ai-engineering
  - migration-effort
  - qa-engineering
  - organizational-readiness
  - agentic-ai
description: >
  The GUIDO Scale is a unified maturity and migration effort framework that
  measures both organizational readiness and the effort required to migrate
  toward Specification-Driven Development (SDD) in AI-agentic software
  engineering environments. It fills the gap that CMMI and other models leave:
  they measure process maturity but not the effort of transforming toward
  AI-native engineering.
---

# GUIDO Scale Skill

> A Maturity and Migration Effort Model for Specification-Driven Development
> in AI-Agentic Software Engineering.
> Author: Guido Miranda Mercado · Version 1.0 · 2026

The GUIDO Scale answers the question no existing framework does:

> **"How ready are we to transition to Specification-Driven Development,
> and how difficult will that migration be?"**

CMMI measures process capability. DevOps maturity models measure delivery
performance. The GUIDO Scale measures **transformation effort toward AI-native
engineering** — a dimension that did not exist before SDD.

---

## The dual-dimension approach

Every existing maturity model measures only ONE dimension: current process quality.
The GUIDO Scale measures TWO simultaneously:

| Dimension | What it measures |
|-----------|-----------------|
| **Organizational maturity** | Current state of process discipline, documentation, governance, automation, and cultural readiness |
| **Migration effort** | How hard it is to move from the current state to SDD-Native (G5) |

These two dimensions are inversely correlated but not identical. An organization
can have moderate maturity (G3) with low effort if their documentation is strong.
A high-maturity org (G4) can still have cultural resistance that raises effort.
The GUIDO Scale captures both.

---

## The three conceptual foundations

Before assessing any organization, internalize these three principles:

### 1. Documentation as a strategic asset
In AI-driven development, structured specifications become the primary source of truth.
Organizations with stronger documentation practices have significantly lower migration effort.
This is why Spectra (the spec framework) pairs naturally with GUIDO Scale assessment.

### 2. AI amplifies existing process quality
AI does not fix broken processes — it makes them faster. A chaotic organization (G1)
that adopts AI agents gets chaotic automation. A mature organization (G4) that adopts
AI agents gets powerful leverage. The GUIDO Scale makes this visible before the investment.

### 3. Migration requires cultural transformation
Adopting SDD involves not only technological changes but shifts in roles, governance
models, and engineering mindset. Technical readiness is necessary but not sufficient.
The Scale explicitly accounts for cultural readiness as a dimension.

---

## The five GUIDO levels

### G1 — Chaotic State
**Migration effort: Very High**

Characteristics:
- Minimal or no documentation
- Reactive processes — firefighting mode
- High dependency on individual knowledge (key-person risk)
- No standardized workflows
- No governance structures

What this means for SDD migration:
The organization must build documentation culture, process discipline, and governance
from scratch before any meaningful SDD adoption. AI agents at G1 produce chaotic
automation — faster failures, not faster delivery.

Recommended first move: stabilize documentation practices before touching AI tooling.

---

### G2 — Initial Directed State
**Migration effort: High**

Characteristics:
- Project-level documentation (exists but inconsistent)
- Emerging governance structures
- Partial process adoption — some teams follow standards, others don't
- Inconsistent engineering methodologies across the organization

What this means for SDD migration:
Migration is possible but requires substantial process formalization first.
The main risk is that SDD adoption happens in isolated pockets without
organizational alignment, creating fragmented spec quality.

Recommended first move: standardize documentation format and establish
cross-team spec review processes.

---

### G3 — Defined Standards State
**Migration effort: Moderate**

Characteristics:
- Organization-wide process standards defined and followed
- Structured documentation practices in place
- Consistent development methodologies across teams
- Engineering culture exists but is not metrics-driven

What this means for SDD migration:
Organizations at G3 are well positioned for SDD adoption. The foundation
(standards + documentation + consistency) is in place. The gap is moving
from documentation-as-artifact to documentation-as-source-of-truth.

Recommended first move: introduce Spectra framework on one pilot project.
Measure reconstruction success. Scale from there.

---

### G4 — Quantitatively Managed State
**Migration effort: Low**

Characteristics:
- Metrics-driven process management
- Advanced automation pipelines (CI/CD, testing, quality gates)
- Strong governance and compliance controls
- Data-informed engineering decisions

What this means for SDD migration:
AI-agent integration becomes highly efficient at G4. The organization already
measures quality — now it can connect those metrics to spec coverage scores
(SPECTRA-TRACE). The transition is evolutionary, not revolutionary.

Recommended first move: instrument existing pipelines with spec-coverage metrics.
Connect SPECTRA-TRACE to existing dashboards.

---

### G5 — SDD-Native State
**Migration effort: Minimal**

Characteristics:
- Specification-centric workflows as the default mode
- Fully integrated AI orchestration — agents operate on specs autonomously
- Continuous specification evolution — specs update as domain changes
- High adaptability and organizational resilience
- AI-native engineering as standard practice

What this means:
G5 is the target state. Organizations here operate with the full Spectra +
SDD stack. Agents build, maintain, validate, and evolve systems from specs.
SPECTRA-TRACE runs automatically. GUIDO Scale level is maintained through
continuous self-assessment.

---

## What the GUIDO Scale measures — the 6 dimensions

Assess each dimension independently, then derive the overall level:

| Dimension | G1 | G2 | G3 | G4 | G5 |
|-----------|----|----|----|----|-----|
| **Process discipline** | None | Partial | Org-wide | Metrics-driven | Spec-driven |
| **Documentation maturity** | None | Project-level | Structured | Quantified | Source of truth |
| **Governance** | None | Emerging | Defined | Strong controls | AI governance |
| **Automation** | None | Basic | Consistent | Advanced CI/CD | Agent-orchestrated |
| **Cultural readiness** | Resistant | Unaware | Open | Engaged | Native |
| **Migration complexity** | Very High | High | Moderate | Low | Minimal |

The overall GUIDO level is the lowest dimension that consistently applies.
A single weak dimension pulls the entire level down. This is intentional —
the bottleneck dimension determines real migration effort.

---

## How to perform a GUIDO Scale assessment

### Step 1 — Collect evidence per dimension
For each of the 6 dimensions, gather:
- Existing documentation samples
- Process artifacts (workflows, standards, runbooks)
- Governance documents (policies, compliance records)
- Automation inventory (CI/CD pipelines, test coverage)
- Cultural indicators (team interviews, adoption of past changes)
- Migration history (how long previous process changes took)

### Step 2 — Score each dimension independently
Assign G1–G5 to each dimension based on the evidence.
Do not average — identify the bottleneck dimension.

### Step 3 — Determine the overall GUIDO level
The overall level = the bottleneck dimension level.
Document why the bottleneck dimension limits the whole organization.

### Step 4 — Map the migration path
For each dimension below G5, define:
- **What needs to change** (specific gaps)
- **Who owns the change** (role/team)
- **Estimated effort** (weeks/months/quarters)
- **Success criteria** (how you'll know the dimension moved up)

### Step 5 — Prioritize by leverage
Not all dimensions have equal migration cost. Prioritize the dimension
that unblocks the most others. Documentation maturity is often the
highest-leverage starting point because it directly enables Spectra adoption.

### Step 6 — Reassess after each major change
The GUIDO Scale is not a one-time assessment. Reassess after:
- Major process changes
- New team formation
- Significant tooling changes
- AI agent adoption milestones

---

## Strategic outcomes of SDD adoption by GUIDO level

Organizations that successfully migrate to G5 gain:

- **Accelerated development cycles** — agents build from specs without ambiguity
- **Improved software quality** — SPECTRA-TRACE detects gaps before they become bugs
- **Reduced technical debt** — specs are always updated before code
- **Enhanced regulatory compliance** — regulations live in specs (Layer 03), never forgotten
- **Sustainable competitive advantage** — the spec corpus grows with every iteration

---

## Integration with Spectra and SDD

The GUIDO Scale is the diagnostic layer of the full ecosystem:

```
GUIDO Scale Assessment
  → determines readiness level (G1–G5)
  → maps effort to reach G5
  → identifies bottleneck dimensions

SDD Methodology
  → provides the working philosophy (spec first, code second)
  → activated once GUIDO assessment shows G3+ readiness

Spectra Framework
  → provides the concrete implementation of SDD
  → 13 layers, SPECTRA-TRACE, reconstructability test
  → fully activated at G3, native at G5

SPECTRA-TRACE
  → provides continuous measurement of spec coverage
  → feeds back into GUIDO level tracking
  → closes the loop: assessment → adoption → measurement → reassessment
```

**The virtuous cycle**: each successful Spectra iteration raises the GUIDO level.
GUIDO level rises reduce migration effort for the next Spectra initiative.
Over time, the organization converges on G5 through accumulated spec quality.

---

## When to activate this skill

Activate GUIDO Scale when the user:
- Asks "how ready are we for AI agents / SDD?"
- Asks "how much effort will it take to adopt Spectra / SDD?"
- Needs to build a migration roadmap toward AI-native engineering
- Is planning an AI transformation strategy
- Needs to assess engineering maturity for governance purposes
- Asks about digital modernization or enterprise architecture readiness
- Mentions CMMI, DevOps maturity, or similar frameworks in the context of AI adoption
- Asks "where are we on the GUIDO Scale?"

---

## Quick reference — assessment questions per dimension

Use these questions to quickly orient an organization's GUIDO level:

**Process discipline**
- Do all teams follow the same engineering process? (G3+)
- Is the process measured with metrics? (G4+)
- Is the process spec-driven? (G5)

**Documentation maturity**
- Does documentation exist and get maintained? (G2+)
- Is there a single source of truth for every system? (G3+)
- Can a new agent reconstruct the system from docs alone? (G5 — Spectra)

**Governance**
- Are there defined policies and someone enforcing them? (G3+)
- Are compliance controls automated and measured? (G4+)
- Is AI agent behavior governed by specs? (G5)

**Automation**
- Is there CI/CD? (G3+)
- Are quality gates automated and metric-driven? (G4+)
- Do AI agents run autonomously on specs? (G5)

**Cultural readiness**
- Are teams open to changing how they work? (G3)
- Are teams actively engaged in process improvement? (G4)
- Is spec-first thinking the default instinct? (G5)

---

## Core rules for AI agents using this skill

1. **Never assign G5 without evidence of spec-centric workflows.** G5 is rare and specific.
2. **The bottleneck rules.** One G1 dimension = G1 organization, regardless of other dimensions.
3. **Assessment before prescription.** Always assess current level before recommending tools or processes.
4. **Effort is not linear.** G1→G2 often takes longer than G3→G4 because it requires cultural change, not just tooling.
5. **Spectra is the path from G3 to G5.** For organizations at G1–G2, prepare the ground first.
6. **Reassessment is mandatory.** A GUIDO level without a date is not useful — it decays.

---

## Resources

- Repository: https://github.com/GuiMiran/guido-sdd-migration-effort-scale
- Whitepaper: https://github.com/GuiMiran/guido-sdd-migration-effort-scale/blob/main/whitepaper/GUIDO-Scale-Whitepaper.md
- Spectra framework: https://github.com/GuiMiran/spectra
- Assessment tools: https://github.com/GuiMiran/guido-sdd-migration-effort-scale/tree/main/assessment

---

## Citation

Miranda, G. (2026). *The GUIDO Scale: A Maturity and Migration Effort Model
for Specification-Driven Development*. GitHub Repository.
https://github.com/GuiMiran/guido-sdd-migration-effort-scale

*Licensed under CC BY 4.0 — free to use, share and adapt with attribution.*
*Created by Guido Miranda Mercado · Senior Quality Engineering Leader*
*AI-Driven Software Quality Strategist*
