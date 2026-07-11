<p align="center">
  <img src="logo.svg" width="180" alt="aiflow logo"/>
</p>

<h1 align="center">🔥 aiflow</h1>

<p align="center">
  <b>AI Workflow Runner — YAML configs, any model, one terminal</b>
  <br>
  Write workflows. Pick models. Get results.
</p>

<p align="center">
  <a href="#-quick-start">🚀 Quick Start</a> •
  <a href="#-examples">📚 Examples</a> •
  <a href="#-why-aiflow">❓ Why aiflow</a> •
  <a href="#-docs">📖 Docs</a>
</p>

<p align="center">
  <a href="https://github.com/zad111ak-ai/aiflow/actions">
    <img src="https://github.com/zad111ak-ai/aiflow/actions/workflows/ci.yml/badge.svg" alt="CI"/>
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="License"/>
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-green?style=flat-square" alt="Python 3.8+"/>
  <a href="https://github.com/zad111ak-ai/aiflow/releases">
    <img src="https://img.shields.io/github/v/release/zad111ak-ai/aiflow?style=flat-square" alt="Release"/>
  </a>
  <a href="https://github.com/zad111ak-ai/aiflow/stargazers">
    <img src="https://img.shields.io/github/stars/zad111ak-ai/aiflow?style=flat-square" alt="Stars"/>
  </a>
  <a href=".github/FUNDING.yml"><img src="https://img.shields.io/badge/sponsor-donate-purple?style=flat-square" alt="Sponsor"/></a>
</p>

---

## ❓ Why aiflow

**aiflow** runs AI prompt chains defined in a single YAML file.

Instead of:
1. Open ChatGPT → paste prompt → wait → copy result
2. Open another model → paste context → repeat
3. Manually save to files

…you write **one YAML**, run **one command**, get everything done.

**Without aiflow:** hours of manual copy-paste between tabs.  
**With aiflow:** 30 seconds and your research → article → social posts are ready.

---

## ✨ What makes it different

Unlike other AI CLI tools (aichat, shell_gpt, fabric) that lock you into one provider:

**aiflow routes through [OmniRoute](https://github.com/zad111ak-ai/omniroute)** — an AI gateway with **680+ models** across **29+ providers**.

Pick any model per step in YAML:
- `auto/best-chat` — best available chat model
- `auto/best-reasoning` — for complex reasoning tasks
- `groq/llama-3.1-8b-instant` — fast & cheap
- `deepseek/deepseek-chat` — DeepSeek
- `auto/best-coding` — code generation

No signing up for 10 services. One endpoint, all models.

---

## 🚀 Quick Start

### Installation

```bash
pip install aiflow
```

Or clone it:

```bash
git clone https://github.com/zad111ak-ai/aiflow.git
cd aiflow
pip install -r requirements.txt
```

**Requirements:** Python 3.8+, running OmniRoute at `localhost:3000`.

### Your first workflow

```bash
mkdir -p my-workflows && cd my-workflows

cat > hello.yml << 'EOF'
workflow:
  steps:
    - id: greet
      prompt: "Say hello creatively, one sentence"
      model: auto/best-chat
EOF

aiflow run hello.yml
```

### With variables

```bash
aiflow run research.yml topic="AI agents in 2026"
```

---

## 📚 Examples

### 🔬 Research → Article → Social posts

Full content pipeline in one go.

```yaml
workflow:
  steps:
    - id: research
      prompt: >-
        Deep research on {{topic}}. Provide key facts, stats,
        trends, and expert opinions in structured markdown.
      model: auto/best-chat
      save: output/{{topic}}-research.md

    - id: article
      prompt: >-
        Write a compelling blog post (800-1000 words) about {{topic}}.
        Professional yet engaging tone.
      model: auto/best-chat
      context_from: research
      save: output/{{topic}}-article.md

    - id: social
      prompt: >-
        Create 5 social posts about this topic, each max 280 chars.
      model: groq/llama-3.1-8b-instant
      context_from: research
      save: output/{{topic}}-social.txt
```

```bash
aiflow run research.yml topic="Quantum computing"
# → output/Quantum computing-research.md
# → output/Quantum computing-article.md
# → output/Quantum computing-social.txt
```

### 🌐 Multi-language translation

```yaml
workflow:
  steps:
    - id: original
      prompt: "Write about {{topic}} in Russian"
      model: auto/best-chat
      save: output/original.md

    - id: to_english
      prompt: "Translate to English"
      context_from: original
      model: auto/best-chat
      save: output/english.md

    - id: to_chinese
      prompt: "Translate to Chinese"
      context_from: original
      model: auto/best-chat
      save: output/chinese.md
```

### 📡 Web scraping + AI analysis

```yaml
workflow:
  steps:
    - id: fetch
      action: fetch
      url: "https://news.ycombinator.com/"
      save: raw/hackernews.md

    - id: analyze
      prompt: "Summarize top 10 posts, identify trends"
      context_from: fetch
      model: auto/best-chat
```

### 💻 Code review

```yaml
workflow:
  steps:
    - id: fetch_diff
      action: fetch
      url: "{{diff_url}}"
      save: raw/diff.txt

    - id: review
      prompt: >-
        Review this code diff for bugs, security vulnerabilities,
        performance issues. Suggest improvements.
      model: auto/best-reasoning
      context_from: fetch_diff
      save: output/review.md
```

### See all examples

```bash
aiflow examples
```

---

## 📖 Docs

### Workflow YAML format

```yaml
workflow:               # required
  steps:                # required, at least 1
    - id: step_name     # unique step identifier
      prompt: "..."     # prompt with {{variables}}
      model: model_id   # OmniRoute model ID
      system: "..."     # optional system prompt
      context:          # optional context sources
        - step://step_id    # output from another step
        - file://path       # content from a file
      context_from: step_id  # shorthand for single step
      save: path        # optional, save output to file
      action: llm       # optional: llm (default) | fetch
      continue_on_error: false
```

### Commands

| Command | Description |
|---|---|
| `aiflow run <file.yml>` | Run a workflow |
| `aiflow run <file.yml> -v key=val` | Run with variables |
| `aiflow examples` | Show built-in examples |
| `aiflow donate` | Show donation addresses |
| `aiflow --version` | Show version |

### Variables

Pass variables with `-v key=value`. Use them in YAML as `{{key}}`.

Variables get resolved in: `prompt`, `context` (strings), `save` path, `url` (for fetch actions).

---

## ⚙️ Environment

| Variable | Default | Description |
|---|---|---|
| `OMNIROUTE_BASE_URL` | http://localhost:3000/v1 | OmniRoute endpoint |
| `OMNIROUTE_API_KEY` | — | API key (if required) |
| `AIFLOW_DEFAULT_MODEL` | auto/best-chat | Default model |

Copy `.env.example` to `.env` and configure.

---

## 💖 Support

If aiflow saves you time, consider a donation:

**TON:** `UQBLEYICSbxKZAajJspddpVYEFtvCcnp7gUpHDZpTChqqAoC`

**USDT (TON):** `UQAoI2i8P9-JeZhvGSUwKnymVyY5cb-1Rg7pdqoWMNena7DP`

**Ethereum (ERC-20):** `0xD26f0efE6A8F11e127c3Af3D6163BD458a1693c3`

**Bitcoin:** `bc1qd8sa7e4f696wmcyszuxh9snqt2n66zrhz9g80j`

Or just ⭐ the repo — that helps too!

---

## 📄 License

MIT © [zad111ak-ai](https://github.com/zad111ak-ai)
