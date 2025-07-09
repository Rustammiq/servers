# 🚀 Gebruikersgids: MCP Servers & Large World Model (LWM)

## 📋 Overzicht

Deze gids laat je zien hoe je beide systemen kunt gebruiken:
- **MCP Servers**: Model Context Protocol servers voor uitbreidbare AI functionaliteit
- **LWM**: Large World Model voor video en tekst verwerking

---

## 🔧 MCP Servers Gebruiken

### 1. Beschikbare Servers

**✅ Werkende Node.js Servers:**
- **Everything**: Reference server met prompts, resources en tools
- **Filesystem**: Veilige bestandsoperaties in `/workspace`
- **Memory**: Persistent geheugen systeem
- **Sequential-thinking**: Dynamische probleemoplossing

**⚠️ Python Servers (niet gevonden):**
- **Time**: Tijd en tijdzone conversies
- **Fetch**: Web content ophalen
- **Git**: Git repository operaties

### 2. MCP Client Setup

#### Option A: Continue CLI
```bash
# Installeer Continue CLI
npm install -g @continue/cli

# Start met MCP configuratie
continue --config mcp_client_config.json
```

#### Option B: Continue VS Code Extension
1. Installeer "Continue" extension in VS Code
2. Kopieer `mcp_client_config.json` naar je workspace
3. Configureer de extension om deze configuratie te gebruiken

#### Option C: Ollama met MCP Plugin
```bash
# Installeer Ollama MCP plugin
ollama install mcp

# Start Ollama met MCP servers
ollama serve --mcp-config mcp_client_config.json
```

### 3. Server Configuratie

Het `mcp_client_config.json` bestand bevat:
```json
{
  "mcpServers": {
    "everything": {
      "command": "node",
      "args": ["/workspace/src/everything/dist/index.js"],
      "env": {}
    },
    "filesystem": {
      "command": "node", 
      "args": ["/workspace/src/filesystem/dist/index.js"],
      "env": {
        "MCP_FILESYSTEM_ROOT": "/workspace"
      }
    },
    "memory": {
      "command": "node",
      "args": ["/workspace/src/memory/dist/index.js"],
      "env": {}
    },
    "sequential-thinking": {
      "command": "node",
      "args": ["/workspace/src/sequentialthinking/dist/index.js"],
      "env": {}
    }
  }
}
```

### 4. Server Tools

**Everything Server:**
- `list_tools`: Toon alle beschikbare tools
- `read_prompt`: Lees prompt templates
- `read_resource`: Lees resources

**Filesystem Server:**
- `read_file`: Lees bestand inhoud
- `write_file`: Schrijf naar bestand
- `list_directory`: Toon directory inhoud

**Memory Server:**
- `read`: Lees opgeslagen informatie
- `write`: Schrijf informatie
- `delete`: Verwijder informatie
- `list`: Toon alle opgeslagen items

**Sequential-thinking Server:**
- `think`: Voer denkproces uit
- `reflect`: Reflecteer op resultaten
- `plan`: Maak actieplan

---

## 🚀 Large World Model (LWM) Gebruiken

### 1. Environment Setup

```bash
# Ga naar LWM directory
cd /Users/innovars_lab/servers/LWM

# Activeer Python environment
source lwm_env/bin/activate

# Test installatie
python test_lwm.py
```

### 2. Beschikbare Model Sizes

| Model | Parameters | Hidden Size | Layers | Use Case |
|-------|------------|-------------|--------|----------|
| 200M  | 200M       | 1024d       | 14     | Debugging |
| 1B    | 1B         | 2048d       | 22     | Small tasks |
| 3B    | 3B         | 3200d       | 26     | Medium tasks |
| 7B    | 7B         | 4096d       | 32     | Standard |
| 13B   | 13B        | 5120d       | 40     | High quality |
| 30B   | 30B        | 6656d       | 60     | Advanced |
| 65B   | 65B        | 8192d       | 80     | Research |
| Debug  | ~1M        | 256d        | 2      | Testing |

### 3. Basis Gebruik

```python
import sys
sys.path.append('.')
from lwm.llama import LLaMAConfig, FlaxLLaMAForCausalLM

# Laad configuratie
config = LLaMAConfig(**LLAMA_STANDARD_CONFIGS['debug'])
print(f"Model: {config.hidden_size}d, {config.num_hidden_layers} layers")

# Maak model (zonder weights)
model = FlaxLLaMAForCausalLM(config)
print("Model architecture created successfully!")
```

### 4. Training Scripts

Bekijk de `scripts/` directory voor training voorbeelden:
- `run_train_text.sh`: Tekst training
- `run_train_vision_text.sh`: Video + tekst training
- `run_vision_chat.sh`: Vision chat interface

### 5. Inference

```python
# Voor inference heb je pre-trained weights nodig
# Download weights van de officiële LWM repository
# Zie README.md voor download instructies
```

---

## 🧪 Testen

### MCP Servers Testen
```bash
python3 test_mcp_servers.py
```

### LWM Testen
```bash
cd /Users/innovars_lab/servers/LWM
source lwm_env/bin/activate
python test_lwm.py
```

---

## 🔧 Troubleshooting

### MCP Servers
- **Servers niet gevonden**: Run `npm run build` in `/workspace`
- **Node.js fout**: Installeer Node.js 18+
- **Python fout**: Gebruik `python3` in plaats van `python`

### LWM
- **Import fout**: Activeer het Python environment
- **Memory fout**: Gebruik kleinere model size (debug/200M)
- **GPU fout**: LWM werkt ook op CPU

---

## 📚 Meer Informatie

- **MCP**: https://modelcontextprotocol.io/
- **LWM**: https://github.com/LargeWorldModel/LWM
- **Continue**: https://continue.dev/
- **Ollama**: https://ollama.ai/

---

## 🎯 Volgende Stappen

1. **MCP Servers**: Configureer je favoriete MCP client
2. **LWM**: Download pre-trained weights voor inference
3. **Training**: Bekijk de training scripts voor custom modellen
4. **Integratie**: Combineer MCP servers met LWM voor geavanceerde AI applicaties

---

**🎉 Gefeliciteerd! Je hebt nu beide systemen werkend!**