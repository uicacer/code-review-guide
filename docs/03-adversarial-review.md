# Adversarial Review - Red/Blue Teaming, Right-Sized

This is **Layer 5** of the [protocol](../PROTOCOL.md): the security pass we add for code touching patient data or secure compute. It explains, in plain words, what "red/blue teaming," "attacker hat," and "STRIDE" mean - and the honest answer to *"should a small research team do this?"*

> New words are in the [Glossary](../GLOSSARY.md).

---

## The short answer first

**Full red/blue "teaming" is overkill for a small team.** It was built for big companies and governments with dedicated attack and defense staff and 24/7 security operations. A solo-to-small research group should not pretend to run that.

**But the adversarial *mindset* is cheap, high-value, and we should absolutely use it**: as a rotating role plus a checklist, not an org chart. Because many projects handle real [PHI](../GLOSSARY.md#health-data-terms) (for example, a clinical FHIR pipeline), the minimum bar is: **a security-focused pass on any change touching data access, authentication, de-identification, or ML inputs/outputs.**

---

## The concepts, in plain words

### "Red team / blue team"
Borrowed from military war-games:
- [**Red team**](../GLOSSARY.md#the-adversarial-redblue-team-terms) = the people who play the **attacker** and try to break in (offense).
- [**Blue team**](../GLOSSARY.md#the-adversarial-redblue-team-terms) = the people who **defend** and try to detect/stop attacks (defense).
- [**Purple team**](../GLOSSARY.md#the-adversarial-redblue-team-terms) = both working together in a loop: red finds a hole → blue fixes it and adds an alert → repeat.

### "Adversarial review" / "attacker hat"
Classic red teaming attacks a *running system*. We do not need that. We borrow only the **mindset** and apply it to the code change in front of us. Putting on the [**attacker hat**](../GLOSSARY.md#the-adversarial-redblue-team-terms) just means: for a few minutes, stop asking "does this work?" and start asking **"how would I abuse this?"** Builders and attackers notice different things - that is the whole value.

### "Threat modeling" and "STRIDE"
[**Threat modeling**](../GLOSSARY.md#the-adversarial-redblue-team-terms) = listing what could go wrong *on purpose*, before it does. To make it doable by non-experts, Microsoft created [**STRIDE**](../GLOSSARY.md#the-adversarial-redblue-team-terms) - six categories of threat you can check one by one. Our **STRIDE-lite** turns it into six yes/no questions on a PR.

### "Security champion"
Instead of a security team, you designate **one person** to carry the security lens into reviews and own the checklist. That is the right-sized staffing model for a small group.

---

## Our lightweight adversarial mini-protocol

1. **Rotating adversary reviewer.** Each sensitive PR gets its normal reviewer **plus** one person whose only job is to answer *"how do I abuse this?"* Rotate weekly so everyone builds the muscle. *(Solo: do a timed 15-minute attacker pass on your own diff, out loud.)*
2. **STRIDE-lite checklist** (six questions, below) on the PR.
3. **PHI/FHIR questions** (below) for any data-path change.
4. **AI-code clause:** flag [AI-generated](../GLOSSARY.md#ai-coding-terms) sections; assume insecure-by-default, and verify any dependency actually exists and is pinned.
5. **Blue-team follow-up:** for each confirmed risk, ask *"would our logs/alerts catch this if it happened?"* If no → file a **detection gap**. (That loop is your miniature purple team.)

### STRIDE-lite - the six questions
- **S**poofing - could someone pretend to be another user or service here?
- **T**ampering - could someone modify data they should not?
- **R**epudiation - if someone did something harmful, is there a log proving it?
- **I**nformation disclosure - could this leak PHI (logs, errors, URLs, test data)?
- **D**enial of service - could someone overwhelm or crash this?
- **E**levation of privilege - could someone gain more access than intended?

---

## Red vs blue on a FHIR / HealthLake pipeline

The same change, seen two ways - each catches different, complementary bugs:

**Red (attacker) asks:**
- Can I craft a [FHIR](../GLOSSARY.md#health-data-terms) request that over-fetches via a too-broad `Patient/*` scope?
- Are [IAM](../GLOSSARY.md#security-terms) roles over-privileged - can one component reach data it should not?
- Does an error message or log line leak PHI?
- Could I poison an ingested dataset, or query the ML model to recover training patients (membership inference)?

**Blue (defender) asks:**
- Is [ePHI encrypted at rest and in transit](../GLOSSARY.md#security-terms)? Are HealthLake/S3/[CloudTrail](../GLOSSARY.md#security-terms) audit logs on *and* reviewed?
- Is access [least-privilege](../GLOSSARY.md#security-terms)?
- Is [de-identification](../GLOSSARY.md#health-data-terms) verified before any non-production use?
- Is there alerting on anomalous bulk reads? Can we roll back a poisoned model?

---

## The AI/ML angle (relevant to ML projects)

Two distinct things, both worth a thought:
- **Red-teaming the ML system itself**: e.g., prompt injection, sensitive-info disclosure, data/model poisoning (see the [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)). Membership-inference on a clinical model is a real patient-privacy risk, not a hypothetical.
- **Red-teaming AI-*generated* code**: treat assistant output adversarially: assume it may ship insecure defaults, skip validation, or invent dependencies. Give it the *same or stronger* attacker pass as human code.

You do not need tooling to start - the mindset + checklist is 90% of the value. If you later want to automate ML red-teaming, Microsoft's PyRIT is a free starting point.

---

## References (verified)
- OWASP Top 10 for LLM Applications (2025) - https://genai.owasp.org/llm-top-10/
- Threat Modeling AI/ML Systems - Microsoft - https://learn.microsoft.com/en-us/security/engineering/threat-modeling-aiml
- STRIDE / Threat Modeling Tool - Microsoft - https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats
- Threat Modeling Process - OWASP - https://community.owasp.org/Threat_Modeling_Process
- Red/Blue team definitions - NIST - https://csrc.nist.gov/glossary/term/red_team
- GenAI Red Teaming Guide - OWASP - https://genai.owasp.org/resource/genai-red-teaming-guide/
- Security Champions Guide - OWASP - https://owasp.org/www-project-security-champions-guide/
- Microsoft AI Red Team - https://learn.microsoft.com/en-us/security/ai-red-team/

More in the full [references](04-references.md).
