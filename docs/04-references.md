# References - Annotated Reading List

The sources behind this repo, grouped by topic. All URLs were verified to load in October 2026. Start with the ⭐ items.

---

## Code review fundamentals
- ⭐ **Google Engineering Practices - Code Review**: https://google.github.io/eng-practices/review/ - The canonical, free playbook. See the sub-pages: [standard](https://google.github.io/eng-practices/review/reviewer/standard.html), [speed](https://google.github.io/eng-practices/review/reviewer/speed.html), [what to look for](https://google.github.io/eng-practices/review/reviewer/), [writing comments](https://google.github.io/eng-practices/review/reviewer/comments.html), [handling comments](https://google.github.io/eng-practices/review/developer/handling-comments.html), [pushback](https://google.github.io/eng-practices/review/reviewer/pushback.html).
- ⭐ **SmartBear/Cisco - Best Practices for Peer Code Review**: https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/ - Source of the numbers: review ≤200-400 lines, ≤60 min/session, lightweight ≈ formal at <20% cost.
- **Modern Code Review: A Case Study at Google** (Sadowski et al., 2018) - https://sback.it/publications/icse2018seip.pdf - Review's real value is education, knowledge transfer, and ownership.
- ⭐ **Conventional Comments**: https://conventionalcomments.org/ - The comment-labeling standard we use.

## Learning the mechanics (for beginners)
- ⭐ **GitHub Skills: Introduction to GitHub**: https://github.com/skills/introduction-to-github
- ⭐ **GitHub Skills: Review Pull Requests**: https://github.com/skills/review-pull-requests
- **GitHub flow**: https://docs.github.com/en/get-started/using-github/github-flow
- **About pull request reviews**: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
- **Understanding GitHub Actions** (CI) - https://docs.github.com/en/actions/about-github-actions/understanding-github-actions
- **pre-commit** (hooks) - https://pre-commit.com/

## Research software specifically
- ⭐ **The Turing Way - Code Reviewing for Research**: https://book.the-turing-way.org/reproducible-research/reviewing - Review framed for solo/small research teams. Also: [CI for research](https://book.the-turing-way.org/reproducible-research/ci).
- **Best Practices for Scientific Computing** (Wilson et al., 2014) - https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745
- **Good Enough Practices in Scientific Computing** (Wilson et al., 2017) - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510 - Honest about dropping formal review for solo work (→ use substitutes).
- **US-RSE**: https://us-rse.org/ - The US research software engineer community (peers, code-review working group).

## The AI era
- ⭐ **Addy Osmani - Code Review in the Age of AI**: https://addyo.substack.com/p/code-review-in-the-age-of-ai
- ⭐ **Addy Osmani - The 70% Problem**: https://addyo.substack.com/p/the-70-problem-hard-truths-about
- **DORA - 2024 State of DevOps**: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report - AI adoption vs. throughput/stability.
- **Veracode - 2025 GenAI Code Security Report**: https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/ - ~45% of AI code had security flaws.
- **METR - AI impact on experienced devs (RCT)**: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ - 19% slower, felt 20% faster (automation bias).
- **GitHub - Responsible use of Copilot code review**: https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-review - Augment, do not replace.
- **Nate Goethel (Mews), "Code generation is now cheap, code review still isn't"**: https://developers.mews.com/code-generation-is-cheap-review-remains-costly/ - Risk-tiered review (label blast radius; lighter review on low-risk PRs) and metrics to detect rubber-stamping.
- **Daz - Code Review in the Age of AI-Augmented Development**: https://daz.is/blog/code-review-ai-augmented-development/ - The coherence problem, reviewing the plan before generation, context-sizing, and AI deviation reports.
- **Alex Ashitkin - Code reviews in the AI era**: https://medium.com/@xqmbiuy/code-reviews-in-the-ai-era-12698f863924 - Review as live guidance of the agent, and the author/reviewer effort imbalance. (Paywalled.)
- **Kamali, Tuna, Haratian & Tuzun (2026) - Rethinking Code Review in the Age of AI: A Vision for Agentic Code Review**: https://arxiv.org/abs/2605.17548 - A research vision for agentic, lifecycle-wide review; source of the "human control point", alignment/scope, and impact framing. (Vision paper, not an empirical study.)

## Security, adversarial & health data
- ⭐ **OWASP Code Review Guide**: https://owasp.org/www-project-code-review-guide/
- **OWASP Top 10 (2025)**: https://owasp.org/www-project-top-ten/
- **OWASP Top 10 for LLM Applications (2025)**: https://genai.owasp.org/llm-top-10/
- **Threat Modeling AI/ML Systems**: Microsoft - https://learn.microsoft.com/en-us/security/engineering/threat-modeling-aiml
- **STRIDE (Threat Modeling Tool)**: Microsoft - https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats
- **Threat Modeling Process**: OWASP - https://community.owasp.org/Threat_Modeling_Process
- **Red/Blue team definitions**: NIST - https://csrc.nist.gov/glossary/term/red_team
- **GenAI Red Teaming Guide**: OWASP - https://genai.owasp.org/resource/genai-red-teaming-guide/
- **Security Champions Guide**: OWASP - https://owasp.org/www-project-security-champions-guide/
- **Microsoft AI Red Team**: https://learn.microsoft.com/en-us/security/ai-red-team/
- **AWS HealthLake - Data Protection**: https://docs.aws.amazon.com/healthlake/latest/devguide/data-protection.html
- **NIST SP 800-66 Rev. 2** (implementing the HIPAA Security Rule, 2024) - https://csrc.nist.gov/pubs/sp/800/66/r2/final
- **gitleaks**: https://github.com/gitleaks/gitleaks · **TruffleHog**: https://github.com/trufflesecurity/trufflehog

## ML reproducibility (for ML projects)
- **The ML Test Score** (Breck et al., Google) - https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/
- **Model Cards** (Mitchell et al.) - https://arxiv.org/abs/1810.03993
- **Datasheets for Datasets** (Gebru et al.) - https://arxiv.org/abs/1803.09010
- **FDA/MHRA - Good Machine Learning Practice (GMLP)**: https://www.fda.gov/medical-devices/artificial-intelligence-enabled-medical-devices/good-machine-learning-practice-medical-device-development-guiding-principles

> **Verify-before-publish note:** a few canonical sources block automated fetching and were not content-verified (HHS HIPAA Security Rule hub, IEC 62304/ISO, and the FAIR4RS/Nature article). Click them manually before citing on a public slide.
