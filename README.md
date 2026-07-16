<p align="center">
  <a href="#russian">🇷🇺 Русский</a> &nbsp;|&nbsp; <a href="#english">🇬🇧 English</a>
</p>

<h1 align="center">🔥 aiflow</h1>

<p align="center">
  <b>AI Workflow Runner — YAML configs, any model, one terminal</b>
</p>

<p align="center">
  <a href="#-quick-start">🚀 Quick Start</a> •
  <a href="#-examples">📚 Examples</a> •
  <a href="#-why-aiflow">❓ Why aiflow</a>
</p>

<p align="center">
  <a href="https://github.com/zad111ak-ai/aiflow/stargazers"><img src="https://img.shields.io/github/stars/zad111ak-ai/aiflow?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/zad111ak-ai/aiflow/graphs/contributors"><img src="https://img.shields.io/github/contributors/zad111ak-ai/aiflow" alt="GitHub contributors"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
</p>

<p align="center">
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="License"/>
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-green?style=flat-square" alt="Python 3.8+"/>
</p>

---

<a id="russian"></a>
## 🔥 Что такое aiflow

**aiflow** запускает AI-воркфлоу, описанные в YAML-файле.

**Без aiflow:**
1. Открыл ChatGPT → вставил промпт → скопировал результат
2. Открыл другую модель → вставил контекст → повторил
3. Вручную сохранил в файлы

**С aiflow:**
```bash
aiflow run research.yml topic="AI агенты"
```
→ `research.md` + `article.md` + `social-posts.md`

---

### Почему aiflow

В отличие от других AI CLI (aichat, shell_gpt, fabric), которые привязывают к одному провайдеру:

**aiflow роутит через [OmniRoute](https://github.com/zad111ak-ai/omniroute)** — AI-шлюз с **680+ моделями** от **29+ провайдеров**.

Выбирай любую модель для каждого шага:
- `auto/best-chat` — лучшая модель
- `auto/best-reasoning` — для сложных задач
- `groq/llama-3.1-8b-instant` — быстрая и дешёвая
- `deepseek/deepseek-chat` — DeepSeek
- `auto/best-coding` — генерация кода

Одна точка входа, все модели. Без регистрации на 10 сервисах.

---

### 🚀 Быстрый старт

```bash
pip install aiflow
# Или:
git clone https://github.com/zad111ak-ai/aiflow.git
cd aiflow && pip install -r requirements.txt
```

**Требования:** Python 3.8+, OmniRoute на `localhost:3000`.

```bash
# Первый воркфлоу
mkdir -p my-workflows && cd my-workflows

cat > hello.yml << 'EOF'
workflow:
  steps:
    - id: greet
      prompt: "Скажи привет креативно, одно предложение"
      model: auto/best-chat
EOF

aiflow run hello.yml
```

### С переменными

```bash
aiflow run research.yml topic="ИИ агенты в 2026"
```

---

## 📚 Примеры

### 🔬 Исследование → Статья → Соцсети

```yaml
workflow:
  steps:
    - id: research
      prompt: >-
        Глубокое исследование темы {{topic}}. Ключевые факты,
        статистика, тренды, мнения экспертов в markdown.
      model: auto/best-chat
      save: output/{{topic}}-research.md

    - id: article
      prompt: >-
        Напиши блог-пост (800-1000 слов) на тему {{topic}}.
        Профессиональный, но живой стиль.
      model: auto/best-chat
      context_from: research
      save: output/{{topic}}-article.md

    - id: social
      prompt: >-
        Создай 5 постов для соцсетей, каждый до 280 символов.
      model: groq/llama-3.1-8b-instant
      context_from: research
      save: output/{{topic}}-social.txt
```

### 🌐 Мультиязычный перевод

```yaml
workflow:
  steps:
    - id: original
      prompt: "Напиши про {{topic}} на русском"
      model: auto/best-chat
      save: output/ru.md

    - id: english
      prompt: "Переведи на английский"
      context_from: original
      model: auto/best-chat
      save: output/en.md
```

### 💻 Code Review

```yaml
workflow:
  steps:
    - id: fetch_diff
      action: fetch
      url: "{{diff_url}}"
      save: raw/diff.txt

    - id: review
      prompt: "Проверь дифф на баги, уязвимости, производительность"
      model: auto/best-reasoning
      context_from: fetch_diff
      save: output/review.md
```

---

## 📖 YAML-формат

```yaml
workflow:
  steps:
    - id: step_name       # уникальный ID
      prompt: "..."        # промпт с {{переменными}}
      model: model_id      # модель OmniRoute
      system: "..."        # системный промпт (опционально)
      context:             # контекст (опционально)
        - step://step_id   # выход другого шага
        - file://path      # файл
      context_from: id     # шорткат для одного шага
      save: path           # сохранить результат
      action: llm          # llm (по умолчанию) | fetch
      continue_on_error: false
```

### Команды

| Команда | Описание |
|---|---|
| `aiflow run <file.yml>` | Запуск воркфлоу |
| `aiflow run <file.yml> -v key=val` | С переменными |
| `aiflow examples` | Встроенные примеры |
| `aiflow donate` | Крипто-кошельки для донатов |
| `aiflow --version` | Версия |

### Переменные

Передавай через `-v key=value`. Используй в YAML как `{{key}}`.

---

## ⚙️ Переменные окружения

| Переменная | По умолчанию | Описание |
|---|---|---|
| `OMNIROUTE_BASE_URL` | http://localhost:3000/v1 | OmniRoute эндпоинт |
| `OMNIROUTE_API_KEY` | — | API-ключ (если нужен) |
| `AIFLOW_DEFAULT_MODEL` | auto/best-chat | Модель по умолчанию |

---

<a id="english"></a>
## 🇬🇧 English

**aiflow** runs AI prompt chains defined in a single YAML file.

Instead of copy-pasting between tabs for hours, write **one YAML**, run **one command**, get everything done.

### Why aiflow

Routes through [OmniRoute](https://github.com/zad111ak-ai/omniroute) — **680+ models** across **29+ providers**. One endpoint, all models.

### Quick Start

```bash
pip install aiflow

cat > hello.yml << 'EOF'
workflow:
  steps:
    - id: greet
      prompt: "Say hello creatively, one sentence"
      model: auto/best-chat
EOF

aiflow run hello.yml
```

### What it does

- **Research → Article → Social posts** — full content pipeline in 30 seconds
- **Multi-language translation** — one source, multiple targets
- **Web scraping + AI analysis** — fetch + summarize in one step
- **Code review** — fetch diff → review → suggestions

### Requirements

Python 3.8+, OmniRoute at `localhost:3000`.

---

## 💸 Donations / Донаты

| Валюта / Currency | Адрес / Address |
|---|---|
| **BTC** | `bc1qd8sa7e4f696wmcyszuxh9snqt2n66zrhz9g80j` |
| **ETH** | `0xD26f0efE6A8F11e127c3Af3D6163BD458a1693c3` |
| **USDT (TON)** | `UQAoI2i8P9-JeZhvGSUwKnymVyY5cb-1Rg7pdqoWMNena7DP` |
| **SOL** | `99EtqBVTeF5UNp9a1oPi18iVXbXptTG7YQ6JeJvXMUJK` |

---

## 📄 License

MIT © [zad111ak-ai](https://github.com/zad111ak-ai)
