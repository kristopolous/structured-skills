# Structured Skills (ss)

**Structured Skills** is a minimal interpreted language and virtual machine (VM) for orchestrating LLM-powered programs. It gives LLMs the equivalent of structured programming—loops, conditionals, variables, function calls—while keeping the model strictly out of control flow decisions.

## 🚀 The Core Insight

LLMs fail at long multi-step tasks not because they lack intelligence, but because they hold too much state and make too many implicit decisions. Structured Skills solves this by making the VM own all control flow. The LLM does only two things:
1. **Decode** one line of "vibe" syntax into a machine opcode.
2. **Execute** bounded inference when explicitly asked.

The result is a system where complex research, analysis, and automation tasks can be expressed in 10-20 lines of near-English code and executed reliably on small local models.

## 🛠️ Setup

### Prerequisites
- Python 3.11+
- [direnv](https://direnv.net/) (recommended)

### Installation
1. Clone the repository and enter the directory.
2. If using `direnv`, run `direnv allow` to set up the virtual environment.
3. Install dependencies in editable mode:
   ```bash
   pip install -e .
   ```

### Configuration
Structured Skills requires a `config.toml` file. Use the provided template:
```bash
cp config.toml.example config.toml
```
Edit `config.toml` to point to your LLM provider (OpenAI, llama.cpp, Ollama, etc.).

## 📖 Usage

Run your `.ss` scripts using the root entry point:
```bash
./ss <your_script.ss>
```

### Example Vibe Script
```ss
import brave-search from mcp_servers.json

def research $topic:
    $urls = %brave-search.search $topic
    $notes = []
    for each $url in $urls:
        $page = %brave-search.fetch $url
        %append $notes $page
    end
    return $notes
end

$results = %research "Post-quantum cryptography"
$summary = infer "summarize $results"
```

## 🧪 Testing

The `tests/` directory contains deterministic test scripts and data to verify VM integrity:
- `tests/test_extraction.ss`: Extracts locations from structured text files.
- `tests/test_math.ss`: Performs arithmetic on numbers read from files.

Run them to ensure your setup is working:
```bash
./ss tests/test_extraction.ss
./ss tests/test_math.ss
```

## 🏗️ Architecture

- **`ss`**: Root entry point (Python script).
- **`src/ss/vm.py`**: The stack-based virtual machine.
- **`src/ss/decoder.py`**: The "Vibe" decoder (Regex + LLM).
- **`src/ss/config.py`**: Config loader (Single source of truth).
- **`src/ss/mcp.py`**: Tool layer for MCP servers.
- **`config.toml`**: Your local LLM configuration (Ignored by git).

## 📄 License
Draft - April 2026
