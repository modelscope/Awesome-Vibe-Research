<p align="center">
  <img src="assets/cover.png" alt="Awesome Vibe Research" width="800"/>
</p>

<h1 align="center">🔬 Awesome Vibe Research</h1>

<p align="center">
  <em>An open, community-driven repository for AI-assisted scientific research</em><br/>
  Curating agents, skills, workflows, tools & best practices across the entire research lifecycle
</p>

<p align="center">
  <a href="./README.md">🇨🇳 中文版</a> | <strong>🇬🇧 English</strong>
</p>

<p align="center">
  <a href="#0--end-to-end-automated-research">🧪 End-to-End</a> •
  <a href="#1--topic-discovery--problem-definition">🔭 Topic Discovery</a> •
  <a href="#2--literature-research-retrieval-reading-review--citation-networks">📚 Literature</a> •
  <a href="#3--method-design">🧩 Method Design</a> •
  <a href="#4--experiment-execution--analysis">⚗️ Experiments</a> •
  <a href="#5--scientific-visualization-figures-plots--visual-communication">📊 Visualization</a> •
  <a href="#6--paper-writing-submission--peer-review">✍️ Writing</a> •
  <a href="#7--reproduction-release--archiving">📦 Reproduction</a> •
  <a href="#8--dissemination-teaching--impact-analysis">📡 Dissemination</a> •
  <a href="#-how-to-contribute">🤝 Contribute</a>
</p>

---

We focus on AI-assisted capabilities that are **reusable** across research workflows, **verifiable** by peers, **evolvable** over time, and **state-of-the-art** in performance.

This repository grew out of the "Doing Research with Agents" seminar series. We aim to consolidate speakers' hands-on experience, audience feedback, open-source projects, and reusable workflows into a community-maintained knowledge base.

---

## 🗺️ Research Lifecycle Map

The table below shows our **9-stage** decomposition of the research lifecycle. Each stage lists "typical questions" and "types of AI-assisted components that can be distilled." The main body expands each stage into a curated project table.

> 💡 **See something missing? Just add a row to the relevant table!**

| Stage | Typical Questions | Scope |
|:---:|---|---|
| 🔄 0. End-to-End | Spans multiple stages below | — |
| 🔭 1. Topic Discovery & Problem Definition | What's happening in this field? What problems are worth pursuing? | trend scanner, paper radar, venue tracker; idea generator, novelty checker, hypothesis workflow |
| 📚 2. Literature Research | How to find, read, compare, and synthesize related work? | literature review workflow, paper reading skill, citation graph agent |
| 🧩 3. Method Design | How to design the approach, experiments, and evaluation metrics? | experiment design skill, ablation planner, protocol checker |
| ⚗️ 4. Experiment Execution & Analysis | How to code, run experiments, and log failures? Are results reliable? | experiment runner, statistical analysis skill, failure analysis workflow, robustness checker |
| 📊 5. Visualization | Do the figures clearly communicate the scientific question? | figure generation agent, visualization critique skill |
| ✍️ 6. Paper Writing | How to structure the paper, manage citations, supplement experiments? | paper writing workflow, citation verifier, rebuttal assistant |
| 📦 7. Reproduction & Release | How to enable others to reproduce and use your work? | artifact packaging workflow, model card, data card, reproducibility checklist |
| 📡 8. Dissemination & Impact | How to track impact after publication? How to build academic influence? | impact analysis tool, social summary skill, citation monitor |

---

## 0 🔄 End-to-End Automated Research

End-to-end systems from idea to paper. Agents spanning three or more stages go here; single-stage tools belong in their respective section.

| Project | Description | Type | Stars | Link | Demo | Paper |
|---|---|---|---|---|---|---|
| AI-Scientist | End-to-end automated scientific discovery: idea generation, experiments, paper writing, and peer review | agent | <!--stars:SakanaAI/AI-Scientist-->⭐&nbsp;14k<!--/stars--> | [GitHub](https://github.com/SakanaAI/AI-Scientist) | - | [Nature 2024](https://modelscope.cn/papers/2408.06292/) |
| AI-Scientist-v2 | Agentic tree search for automated research, template-free, targeting general ML exploration | agent | <!--stars:SakanaAI/AI-Scientist-v2-->⭐&nbsp;6.6k<!--/stars--> | [GitHub](https://github.com/SakanaAI/AI-Scientist-v2) | - | [arXiv 2025](https://modelscope.cn/papers/2504.08066/) |
| EvoScientist | Multi-agent AI scientist with persistent memory, skill evolution, and end-to-end research collaboration | agent | <!--stars:EvoScientist/EvoScientist-->⭐&nbsp;3.6k<!--/stars--> | [GitHub](https://github.com/EvoScientist/EvoScientist) | [Demo](https://evoscientist.ai) | [arXiv 2025](https://modelscope.cn/papers/2603.08127/) |
| nature-skills | Skills for Nature-grade academic writing and scientific figure creation | skill | <!--stars:Yuan1z0825/nature-skills-->⭐&nbsp;20.9k<!--/stars--> | [GitHub](https://github.com/Yuan1z0825/nature-skills) · [ModelScope Skills](https://modelscope.cn/collections/stn54999/nature-skills) | - | - |
| AutoResearchClaw | Autonomous, self-evolving multi-stage research pipeline from idea to paper artifacts | agent | <!--stars:aiming-lab/AutoResearchClaw-->⭐&nbsp;13.5k<!--/stars--> | [GitHub](https://github.com/aiming-lab/AutoResearchClaw) | [Demo](https://openclaw.ai) | [arXiv 2025](https://modelscope.cn/papers/2605.22662/) |
| autoresearch | Andrej Karpathy's autonomous ML research agent running experiments on a single GPU | agent | <!--stars:karpathy/autoresearch-->⭐&nbsp;87.4k<!--/stars--> | [GitHub](https://github.com/karpathy/autoresearch) | - | - |
| Auto Claude Code Research in Sleep | Automated Claude Code research workflow for unattended experiment execution | skill | <!--stars:wanshuiyin/Auto-claude-code-research-in-sleep-->⭐&nbsp;12.3k<!--/stars--> | [GitHub](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | - | - |
| AgentLaboratory | End-to-end autonomous research workflow with LLM-powered specialized agents for literature review through report writing | agent | <!--stars:SamuelSchmidgall/AgentLaboratory-->⭐&nbsp;5.7k<!--/stars--> | [GitHub](https://github.com/SamuelSchmidgall/AgentLaboratory) | - | - |
| Aether | Open-source AI research environment with unified web & desktop experience, powered by research-focused agents and skills | agent/app | <!--stars:Science-Discovery/Aether-->⭐&nbsp;65<!--/stars--> | [GitHub](https://github.com/Science-Discovery/Aether) | - | - |
| EurekAgent | Environment-engineered autonomous research system for metric-driven tasks, coordinating Claude Code sessions to propose, implement, evaluate, and iterate solutions | agent | <!--stars:THU-Team-Eureka/EurekAgent-->⭐&nbsp;55<!--/stars--> | [GitHub](https://github.com/THU-Team-Eureka/EurekAgent) | - | [arXiv 2026](https://arxiv.org/abs/2606.13662) |

---

## 1 🔭 Topic Discovery & Problem Definition

Trend tracking, research inspiration, novelty verification, hypothesis generation. When overlapping with literature search, the deciding factor is: "Does it output a viable research question?"

| Project | Description | Type | Stars | Link | Demo | Paper |
|---|---|---|---|---|---|---|
| SciAgentsDiscovery | MIT open-source scientific discovery system combining knowledge graphs and multi-agent collaboration for cross-domain hypothesis generation | agent | <!--stars:lamm-mit/SciAgentsDiscovery-->⭐&nbsp;615<!--/stars--> | [GitHub](https://github.com/lamm-mit/SciAgentsDiscovery) | - | [arXiv 2024](https://arxiv.org/abs/2409.05556) |
| AutoDiscovery | AllenAI open-ended scientific discovery framework using Bayesian Surprise to find testable hypotheses from data | benchmark/workflow | <!--stars:allenai/autodiscovery-neurips-->⭐&nbsp;185<!--/stars--> | [GitHub](https://github.com/allenai/autodiscovery-neurips) | - | [NeurIPS 2024](https://arxiv.org/abs/2406.13266) |

---

## 2 📚 Literature Research: Retrieval, Reading, Review & Citation Networks

Literature search, RAG Q&A, automated survey generation, citation graph analysis. Pure writing/polishing tools go in Stage 6.

| Project | Description | Type | Stars | Link | Demo | Paper |
|---|---|---|---|---|---|---|
| STORM | Stanford's open-source knowledge curation system generating cited reports via multi-perspective question generation | agent | <!--stars:stanford-oval/storm-->⭐&nbsp;28.5k<!--/stars--> | [GitHub](https://github.com/stanford-oval/storm) | [Demo](https://storm.genie.stanford.edu) | [NAACL 2024](https://modelscope.cn/papers/2402.14207/) |
| paperseek | A researcher-oriented literature discovery tool supporting natural language queries with iterative search expansion | agent/skill | <!--stars:MingfengHong/paperseek-->⭐&nbsp;36<!--/stars--> | [GitHub](https://github.com/MingfengHong/paperseek) | [paperseek.xyz](https://www.paperseek.xyz/) | - |
| OpenAlex Search Skill | OpenAlex is an open global scholarly graph covering works, authors, institutions, venues, and citations. This Codex skill packages OpenAlex works search into a reusable command-line workflow; recommended defaults are title + abstract Boolean search, `include_xpac=true`, and stemming enabled, with optional customization through semantic mode, citation sorting, year filters, XPAC/stemming switches, and JSON output. | skill | <!--stars:XiaokunDuan/openalex_search-->⭐&nbsp;0<!--/stars--> | [GitHub](https://github.com/XiaokunDuan/openalex_search) | [Skill](https://github.com/XiaokunDuan/openalex_search/blob/main/openalex_search/SKILL.md) | - |
| Lune | MCP server providing agentic search over top-tier papers, with grounding for both academic literature and research best practices | agent/tool | <!--stars:RetrogradeLabs/lune-mcp-server-->⭐&nbsp;2<!--/stars--> | [GitHub](https://github.com/RetrogradeLabs/lune-mcp-server) | [Demo](https://luneresearch.com) | - |
| PaperQA2 | High-accuracy RAG system for scientific papers, producing evidence-grounded answers with citations | python pkg | <!--stars:Future-House/paper-qa-->⭐&nbsp;8.7k<!--/stars--> | [GitHub](https://github.com/Future-House/paper-qa) | - | - |
| OpenScholar | Retrieval-augmented scientific literature synthesis system for generating scholarly answers grounded in open corpora | agent/model | <!--stars:AkariAsai/OpenScholar-->⭐&nbsp;1.5k<!--/stars--> | [GitHub](https://github.com/AkariAsai/OpenScholar) | - | [arXiv 2024](https://arxiv.org/abs/2411.14199) |
| paper-search-mcp | MCP/CLI/Skill for agent-facing paper search across arXiv, PubMed, bioRxiv, Semantic Scholar, OpenAlex, and more | tool/skill | <!--stars:openags/paper-search-mcp-->⭐&nbsp;1.9k<!--/stars--> | [GitHub](https://github.com/openags/paper-search-mcp) | - | - |
| Zotero-GPT | AI literature-reading plugin inside Zotero, supporting summarization, Q&A, tagging, and note assistance | plugin | <!--stars:MuiseDestiny/zotero-gpt-->⭐&nbsp;7.2k<!--/stars--> | [GitHub](https://github.com/MuiseDestiny/zotero-gpt) | - | - |

---

## 3 🧩 Method Design

Experiment planning, evaluation metric design, ablation planning, protocol checking. Pure coding and experiment running go in Stage 4.

| Project | Description | Type | Stars | Link | Demo | Paper |
|---|---|---|---|---|---|---|
| Curie | Automated and rigorous scientific experimentation agent, spanning hypothesis clarification, execution, analysis, and reporting | agent/workflow | <!--stars:Just-Curieous/Curie-->⭐&nbsp;363<!--/stars--> | [GitHub](https://github.com/Just-Curieous/Curie) | - | [arXiv 2025](https://arxiv.org/abs/2502.16069) |

---

## 4 ⚗️ Experiment Execution & Analysis

Coding, experiment running, statistical analysis, failure analysis, robustness checking. Dataset construction goes in Stage 2/3; visualization in Stage 5.

| Project | Description | Type | Stars | Link | Demo | Paper |
|---|---|---|---|---|---|---|
| RD-Agent | Automates high-value R&D processes for data and models — letting AI drive data-driven AI | agent | <!--stars:microsoft/RD-Agent-->⭐&nbsp;13.5k<!--/stars--> | [GitHub](https://github.com/microsoft/RD-Agent) | - | [arXiv 2025](https://arxiv.org/abs/2505.14738) |
| EurekAgent | Execution environment for metric-driven research tasks, supporting Claude Code sessions for implementation, Docker-isolated evaluation, logging, and iterative optimization | agent | <!--stars:THU-Team-Eureka/EurekAgent-->⭐&nbsp;55<!--/stars--> | [GitHub](https://github.com/THU-Team-Eureka/EurekAgent) | - | [arXiv 2026](https://arxiv.org/abs/2606.13662) |

---

## 5 📊 Scientific Visualization: Figures, Plots & Visual Communication

Publication-quality figures, schematic generation, data dashboards. Slides/posters go in Stage 8.

| Project | Description | Type | Stars | Link | Demo | Paper |
|---|---|---|---|---|---|---|
| PaperBanana | Multi-agent framework for automated academic illustration, generating publication-ready charts from text descriptions | agent | <!--stars:dwzhu-pku/PaperBanana-->⭐&nbsp;6.6k<!--/stars--> | [GitHub](https://github.com/dwzhu-pku/PaperBanana) | [Demo](https://dwzhu-pku.github.io/PaperBanana/) | [arXiv 2025](https://modelscope.cn/papers/2601.23265/) |

---

## 6 ✍️ Paper Writing, Submission & Peer Review

Drafting, polishing, citation verification, LaTeX assistance, rebuttal, reviewing. Survey generation goes in Stage 2.

| Project | Description | Type | Stars | Link | Demo | Paper |
|---|---|---|---|---|---|---|
| Academic Research Skills | Claude Code skill suite covering academic writing, polishing, submission checks, and publication workflow | skill | <!--stars:Imbad0202/academic-research-skills-->⭐&nbsp;32.5k<!--/stars--> | [GitHub](https://github.com/Imbad0202/academic-research-skills) | - | - |
| RefChecker | Academic reference validation tool for checking citation existence, metadata errors, and likely fabricated references | tool | <!--stars:markrussinovich/refchecker-->⭐&nbsp;402<!--/stars--> | [GitHub](https://github.com/markrussinovich/refchecker) | - | - |

---

## 7 📦 Reproduction, Release & Archiving

Code reproduction, demo experience, model & dataset publishing.

| Project | Description | Type | Link | Guide |
|---|---|---|---|---|
| ModelScope Studios | Host research demo reproduction, release, and hands-on experience | platform | [ModelScope Studio](https://modelscope.cn/studios) | [Docs](https://modelscope.cn/docs/studios/intro) |
| ModelScope Notebook | Free cloud Jupyter with GPU, persistent storage, and AI coding assistance | platform | [Gallery](https://modelscope.cn/gallery) | [Guide](https://modelscope.cn/learn/434367) |
| ModelScope AI for Science | Open-source AI4Science model hub covering life, earth, material, and social sciences | platform | [Nexa Models](https://modelscope.cn/nexa/models) | [Docs](https://modelscope.cn/docs/nexa/intro) |
| Paper2Code | Multi-agent system converting academic papers into runnable code repositories | agent | [GitHub](https://github.com/going-doer/Paper2Code) | [Quick Start](https://github.com/going-doer/Paper2Code#-quick-start) |
| data-to-paper | Multi-AI-agent system that autonomously produces verifiable papers from raw data | python pkg | [GitHub](https://github.com/Technion-Kishony-lab/data-to-paper) | - |
| Manage AI Research Projects | Agent Skill for Claude Code/Codex to scaffold reproducible research projects, audit metadata and result traceability, and record AI workflow assets | skill | [GitHub](https://github.com/Devin-jun/Manage-AI-Research) | [README](https://github.com/Devin-jun/Manage-AI-Research/blob/main/README.md) |
| Research Network | Agent-native protocol and toolkit for verifiable AI-assisted research assets: package papers, skills, workflows, code, and evidence from a Git workspace, then resolve them back through a live index, web UI, and CLI. Useful for reproducible release, archiving, and agent skill distribution. | protocol/tool | [GitHub](https://github.com/Euraxluo/research-network) · [Demo](https://research-network-web.vercel.app) | [Use CLI](https://research-network-web.vercel.app/use-cli.html) |

---

## 8 📡 Dissemination, Teaching & Impact Analysis

Slides, posters, blog posts, social media outreach, citation analysis, academic influence tools.

| Project | Description | Type | Stars | Link | Demo/Practice | Paper |
|---|---|---|---|---|---|---|
| CitationClaw | Agent-powered explainable citation impact mining for post-publication analysis | tool | <!--stars:VisionXLab/CitationClaw-->⭐&nbsp;307<!--/stars--> | [GitHub](https://github.com/VisionXLab/CitationClaw) | [ModelScope Studio](https://modelscope.cn/studios/fork?target=VisionXLab/CitationClaw) | - |
| ModelScope AI Super Resume | Build your research profile to showcase models, datasets, papers, demos, and academic influence | platform | - | [ModelScope](https://modelscope.cn/) | Examples: [VoyagerX](https://modelscope.cn/profile/VoyagerX) · [chenxie95](https://modelscope.cn/profile/chenxie95) | - |

---

## 🏆 Best Practices

| Title | Summary | Article | Demo |
|---|---|---|---|
| DIY Your Protein — AlphaFold3 Inference | Hands-on tutorial for protein structure prediction with AlphaFold3 on ModelScope | [Learn](https://modelscope.cn/learn/5526) | [Studio](https://modelscope.cn/studios/Z_biosketch/af3_infer_test/summary) |
| AI-Ready Remote Sensing: From Open Data to Open-Source Ecosystem | AI-Ready data intro and how ModelScope improves AI readiness for remote sensing research | [Learn](https://modelscope.cn/learn/434003) | - |
| Open Source GeoAI Practice with ModelScope | APGARSS tutorial collection: open-source GeoAI practice based on ModelScope | [Learn](https://modelscope.cn/learn/434198) | - |
| [PaperSeek - Literature Search with Natural Language](https://github.com/MingfengHong/paperseek) | A practical workflow for natural-language literature search, automatic query expansion, and candidate paper collection | [Learn](https://modelscope.cn/learn/434408) | [Studio](https://modelscope.cn/studios/HongMingfeng/PaperSeek) |

---

## 📋 Inclusion Criteria

What we look for:

- ✅ Clearly targets scientific research scenarios (not general-purpose AI assistants)
- ✅ Has runnable code or a reusable workflow
- ✅ Actively maintained (updated within the last 6 months)
- ✅ Clear documentation or README for onboarding
- ✅ Addresses real research pain points with demonstrated use cases
- ✅ Open source or has a free tier

Bonus points: backed by a paper · has a live demo · cited by the research community · validated in real projects

---

## 🤝 How to Contribute

Beyond recommending existing open-source projects, we **especially encourage** you to distill AI-assisted workflows you've actually run in your own research.

**Contribution types:**

- 🔗 **Recommend a Resource**: Suggest a tool/paper/agent/skill you've used — just add a row to the relevant stage table with a one-line description of your use case.
- 📝 **Share a Best Practice**: Share a reusable workflow you've built, for example:
  - A real research scenario ("I used it for literature review in XXX, saving ~X hours")
  - Failure cases & boundaries ("Doesn't work well in Y scenario because of Z")

**How to contribute:** Add a row at the end of the relevant stage table, and fill in a link in the "Demo/Practice" column. We recommend publishing on [ModelScope Learn](https://modelscope.cn/learn) with the `#vibe-research` tag for discoverability; external links are also welcome. If your practice spans multiple stages, place it in the most core stage and note "also covers stage X" in the description.

**About the Stars column:**
- Stars are automatically maintained by GitHub Action — **just add the marker on first submission**, and they will be updated automatically
- When adding a new project, fill the `Stars` column with:
  ```
  `<!--stars:OWNER/REPO-->⭐ updating<!--/stars-->`
  ```
  For example:
  ```
  | DeepScientist | Local-first autonomous research studio... | agent | <!--stars:ResearAI/DeepScientist-->⭐&nbsp;3.1k<!--/stars--> | [GitHub](...) | [Demo](...) | [arXiv 2025](...) |
  ```
- Update frequency:
  - **Scheduled**: Daily at 2:00 AM (UTC)
  - **Immediate**: Triggered right after a PR is merged to `main` if `README.md` is changed
- If the GitHub API is temporarily unavailable, the script automatically keeps the previous star count — no blank values

---

## 🙏 Acknowledgments

Thanks to all contributors for their participation and sharing!

<p align="center">
  <a href="https://github.com/modelscope/Awesome-Vibe-Research/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=modelscope/Awesome-Vibe-Research" />
  </a>
</p>

---

<p align="center">
  <a href="https://modelscope.cn">
    <img src="https://img.shields.io/badge/ModelScope-Community-blueviolet?style=flat-square" alt="ModelScope"/>
  </a>
  <a href="https://github.com/modelscope/Awesome-Vibe-Research">
    <img src="https://img.shields.io/github/stars/modelscope/Awesome-Vibe-Research?style=social" alt="GitHub stars"/>
  </a>
  <a href="https://github.com/modelscope/Awesome-Vibe-Research/issues">
    <img src="https://img.shields.io/github/issues/modelscope/Awesome-Vibe-Research?style=flat-square" alt="Issues"/>
  </a>
</p>
