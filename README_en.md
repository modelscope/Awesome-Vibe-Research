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
| AI-Scientist | End-to-end automated scientific discovery: idea generation, experiments, paper writing, and peer review | agent | [![GitHub stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=social)](https://github.com/SakanaAI/AI-Scientist) | [GitHub](https://github.com/SakanaAI/AI-Scientist) | - | [Nature 2024](https://modelscope.cn/papers/2408.06292/) |
| AI-Scientist-v2 | Agentic tree search for automated research, template-free, targeting general ML exploration | agent | [![GitHub stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=social)](https://github.com/SakanaAI/AI-Scientist-v2) | [GitHub](https://github.com/SakanaAI/AI-Scientist-v2) | - | [arXiv 2025](https://modelscope.cn/papers/2504.08066/) |
| EvoScientist | Multi-agent AI scientist with persistent memory, skill evolution, and end-to-end research collaboration | agent | [![GitHub stars](https://img.shields.io/github/stars/EvoScientist/EvoScientist?style=social)](https://github.com/EvoScientist/EvoScientist) | [GitHub](https://github.com/EvoScientist/EvoScientist) | [Demo](https://evoscientist.ai) | [arXiv 2025](https://modelscope.cn/papers/2603.08127/) |
| nature-skills | Skills for Nature-grade academic writing and scientific figure creation | skill | [![GitHub stars](https://img.shields.io/github/stars/Yuan1z0825/nature-skills?style=social)](https://github.com/Yuan1z0825/nature-skills) | [GitHub](https://github.com/Yuan1z0825/nature-skills) · [ModelScope Skills](https://modelscope.cn/collections/stn54999/nature-skills) | - | - |
| AutoResearchClaw | Autonomous, self-evolving multi-stage research pipeline from idea to paper artifacts | agent | [![GitHub stars](https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=social)](https://github.com/aiming-lab/AutoResearchClaw) | [GitHub](https://github.com/aiming-lab/AutoResearchClaw) | [Demo](https://openclaw.ai) | [arXiv 2025](https://modelscope.cn/papers/2605.22662/) |
| autoresearch | Andrej Karpathy's autonomous ML research agent running experiments on a single GPU | agent | [![GitHub stars](https://img.shields.io/github/stars/karpathy/autoresearch?style=social)](https://github.com/karpathy/autoresearch) | [GitHub](https://github.com/karpathy/autoresearch) | - | - |
| Auto Claude Code Research in Sleep | Automated Claude Code research workflow for unattended experiment execution | skill | [![GitHub stars](https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=social)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | [GitHub](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | - | - |
| AgentLaboratory | End-to-end autonomous research workflow with LLM-powered specialized agents for literature review through report writing | agent | [![GitHub stars](https://img.shields.io/github/stars/SamuelSchmidgall/AgentLaboratory?style=social)](https://github.com/SamuelSchmidgall/AgentLaboratory) | [GitHub](https://github.com/SamuelSchmidgall/AgentLaboratory) | - | - |
| Aether | Open-source AI research environment with unified web & desktop experience, powered by research-focused agents and skills | agent/app | [![GitHub stars](https://img.shields.io/github/stars/Science-Discovery/Aether?style=social)](https://github.com/Science-Discovery/Aether) | [GitHub](https://github.com/Science-Discovery/Aether) | - | - |

---

## 1 🔭 Topic Discovery & Problem Definition

Trend tracking, research inspiration, novelty verification, hypothesis generation. When overlapping with literature search, the deciding factor is: "Does it output a viable research question?"

*🚧 No entries yet — contributions welcome!*

---

## 2 📚 Literature Research: Retrieval, Reading, Review & Citation Networks

Literature search, RAG Q&A, automated survey generation, citation graph analysis. Pure writing/polishing tools go in Stage 6.

| Project | Description | Type | Stars | Link | Demo | Paper |
|---|---|---|---|---|---|---|
| STORM | Stanford's open-source knowledge curation system generating cited reports via multi-perspective question generation | agent | [![GitHub stars](https://img.shields.io/github/stars/stanford-oval/storm?style=social)](https://github.com/stanford-oval/storm) | [GitHub](https://github.com/stanford-oval/storm) | [Demo](https://storm.genie.stanford.edu) | [NAACL 2024](https://modelscope.cn/papers/2402.14207/) |
| paperseek | A researcher-oriented literature discovery tool supporting natural language queries with iterative search expansion | agent/skill | [![GitHub stars](https://img.shields.io/github/stars/MingfengHong/paperseek?style=social)](https://github.com/MingfengHong/paperseek) | [GitHub](https://github.com/MingfengHong/paperseek) | [paperseek.xyz](https://www.paperseek.xyz/) | - |
| Lune | MCP server providing agentic search over top-tier papers, with grounding for both academic literature and research best practices | agent/tool | [![GitHub stars](https://img.shields.io/github/stars/RetrogradeLabs/lune-mcp-server?style=social)](https://github.com/RetrogradeLabs/lune-mcp-server) | [GitHub](https://github.com/RetrogradeLabs/lune-mcp-server) | [Demo](https://luneresearch.com) | - |

---

## 3 🧩 Method Design

Experiment planning, evaluation metric design, ablation planning, protocol checking. Pure coding and experiment running go in Stage 4.

*🚧 No entries yet — contributions welcome!*

---

## 4 ⚗️ Experiment Execution & Analysis

Coding, experiment running, statistical analysis, failure analysis, robustness checking. Dataset construction goes in Stage 2/3; visualization in Stage 5.

| Project | Description | Type | Stars | Link | Demo | Paper |
|---|---|---|---|---|---|---|
| RD-Agent | Automates high-value R&D processes for data and models — letting AI drive data-driven AI | agent | [![GitHub stars](https://img.shields.io/github/stars/microsoft/RD-Agent?style=social)](https://github.com/microsoft/RD-Agent) | [GitHub](https://github.com/microsoft/RD-Agent) | - | [arXiv 2025](https://arxiv.org/abs/2505.14738) |

---

## 5 📊 Scientific Visualization: Figures, Plots & Visual Communication

Publication-quality figures, schematic generation, data dashboards. Slides/posters go in Stage 8.

| Project | Description | Type | Stars | Link | Demo | Paper |
|---|---|---|---|---|---|---|
| PaperBanana | Multi-agent framework for automated academic illustration, generating publication-ready charts from text descriptions | agent | [![GitHub stars](https://img.shields.io/github/stars/dwzhu-pku/PaperBanana?style=social)](https://github.com/dwzhu-pku/PaperBanana) | [GitHub](https://github.com/dwzhu-pku/PaperBanana) | [Demo](https://dwzhu-pku.github.io/PaperBanana/) | [arXiv 2025](https://modelscope.cn/papers/2601.23265/) |

---

## 6 ✍️ Paper Writing, Submission & Peer Review

Drafting, polishing, citation verification, LaTeX assistance, rebuttal, reviewing. Survey generation goes in Stage 2.

| Project | Description | Type | Stars | Link | Demo | Paper |
|---|---|---|---|---|---|---|
| Academic Research Skills | Claude Code skill suite covering academic writing, polishing, submission checks, and publication workflow | skill | [![GitHub stars](https://img.shields.io/github/stars/Imbad0202/academic-research-skills?style=social)](https://github.com/Imbad0202/academic-research-skills) | [GitHub](https://github.com/Imbad0202/academic-research-skills) | - | - |

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

---

## 8 📡 Dissemination, Teaching & Impact Analysis

Slides, posters, blog posts, social media outreach, citation analysis, academic influence tools.

| Project | Description | Type | Stars | Link | Demo/Practice | Paper |
|---|---|---|---|---|---|---|
| CitationClaw | Agent-powered explainable citation impact mining for post-publication analysis | tool | [![GitHub stars](https://img.shields.io/github/stars/VisionXLab/CitationClaw?style=social)](https://github.com/VisionXLab/CitationClaw) | [GitHub](https://github.com/VisionXLab/CitationClaw) | [ModelScope Studio](https://modelscope.cn/studios/fork?target=VisionXLab/CitationClaw) | - |
| ModelScope AI Super Resume | Build your research profile to showcase models, datasets, papers, demos, and academic influence | platform | - | [ModelScope](https://modelscope.cn/) | Examples: [VoyagerX](https://modelscope.cn/profile/VoyagerX) · [chenxie95](https://modelscope.cn/profile/chenxie95) | - |

---

## 🏆 Best Practices

| Title | Summary | Article | Demo |
|---|---|---|---|
| DIY Your Protein — AlphaFold3 Inference | Hands-on tutorial for protein structure prediction with AlphaFold3 on ModelScope | [Learn](https://modelscope.cn/learn/5526) | [Studio](https://modelscope.cn/studios/Z_biosketch/af3_infer_test/summary) |
| AI-Ready Remote Sensing: From Open Data to Open-Source Ecosystem | AI-Ready data intro and how ModelScope improves AI readiness for remote sensing research | [Learn](https://modelscope.cn/learn/434003) | - |
| Open Source GeoAI Practice with ModelScope | APGARSS tutorial collection: open-source GeoAI practice based on ModelScope | [Learn](https://modelscope.cn/learn/434198) | - |

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
