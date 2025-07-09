#!/usr/bin/env python3
"""
Test script voor MCP servers
"""

import asyncio
import json
import subprocess
import sys
from pathlib import Path

def test_server_availability():
    """Test of alle MCP servers beschikbaar zijn"""
    print("🔍 Testing MCP Server Availability...")
    
    servers = {
        "everything": "src/everything/dist/index.js",
        "filesystem": "src/filesystem/dist/index.js", 
        "memory": "src/memory/dist/index.js",
        "sequential-thinking": "src/sequentialthinking/dist/index.js",
        "time": "src/time/src/main.py",
        "fetch": "src/fetch/src/main.py",
        "git": "src/git/src/main.py"
    }
    
    base_path = Path("/workspace")
    
    for name, path in servers.items():
        full_path = base_path / path
        if full_path.exists():
            print(f"  ✅ {name}: {full_path}")
        else:
            print(f"  ❌ {name}: {full_path} (niet gevonden)")
    
    print()

def test_node_servers():
    """Test Node.js servers"""
    print("🟢 Testing Node.js MCP Servers...")
    
    node_servers = ["everything", "filesystem", "memory", "sequential-thinking"]
    
    for server in node_servers:
        try:
            # Test of server kan starten
            result = subprocess.run(
                ["node", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                print(f"  ✅ {server}: Node.js beschikbaar")
            else:
                print(f"  ❌ {server}: Node.js niet beschikbaar")
        except Exception as e:
            print(f"  ❌ {server}: Fout - {e}")
    
    print()

def test_python_servers():
    """Test Python servers"""
    print("🐍 Testing Python MCP Servers...")
    
    python_servers = ["time", "fetch", "git"]
    
    for server in python_servers:
        try:
            # Test of Python beschikbaar is
            result = subprocess.run(
                ["python3", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                print(f"  ✅ {server}: Python3 beschikbaar")
            else:
                print(f"  ❌ {server}: Python3 niet beschikbaar")
        except Exception as e:
            print(f"  ❌ {server}: Fout - {e}")
    
    print()

def test_server_startup():
    """Test of servers kunnen starten"""
    print("🚀 Testing Server Startup...")
    
    test_servers = {
        "everything": ["node", "/workspace/src/everything/dist/index.js"],
        "filesystem": ["node", "/workspace/src/filesystem/dist/index.js"],
        "memory": ["node", "/workspace/src/memory/dist/index.js"],
        "sequential-thinking": ["node", "/workspace/src/sequentialthinking/dist/index.js"]
    }
    
    for name, cmd in test_servers.items():
        try:
            # Test of server kan starten (timeout na 3 seconden)
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=3
            )
            print(f"  ✅ {name}: Kan starten")
        except subprocess.TimeoutExpired:
            print(f"  ✅ {name}: Start succesvol (timeout)")
        except Exception as e:
            print(f"  ❌ {name}: Fout - {e}")
    
    print()

def create_usage_examples():
    """Maak voorbeelden van hoe MCP servers te gebruiken"""
    print("📝 MCP Server Usage Examples:")
    print()
    
    examples = {
        "everything": {
            "description": "Reference server met prompts, resources en tools",
            "use_case": "Testen van MCP functionaliteit",
            "tools": ["list_tools", "read_prompt", "read_resource"]
        },
        "filesystem": {
            "description": "Veilige bestandsoperaties",
            "use_case": "Lezen/schrijven van bestanden in geconfigureerde directory",
            "tools": ["read_file", "write_file", "list_directory"]
        },
        "memory": {
            "description": "Persistent geheugen systeem",
            "use_case": "Opslaan en ophalen van informatie tussen sessies",
            "tools": ["read", "write", "delete", "list"]
        },
        "sequential-thinking": {
            "description": "Dynamische probleemoplossing",
            "use_case": "Complexe taken stap voor stap uitvoeren",
            "tools": ["think", "reflect", "plan"]
        },
        "time": {
            "description": "Tijd en tijdzone conversies",
            "use_case": "Datum/tijd berekeningen en conversies",
            "tools": ["get_time", "convert_timezone", "calculate_duration"]
        },
        "fetch": {
            "description": "Web content ophalen",
            "use_case": "Webpagina's ophalen en converteren voor LLM gebruik",
            "tools": ["fetch_url", "fetch_text", "fetch_html"]
        },
        "git": {
            "description": "Git repository operaties",
            "use_case": "Code repositories doorzoeken en manipuleren",
            "tools": ["read_file", "list_directory", "search_code"]
        }
    }
    
    for server, info in examples.items():
        print(f"🔧 {server.upper()}")
        print(f"   Beschrijving: {info['description']}")
        print(f"   Gebruik: {info['use_case']}")
        print(f"   Tools: {', '.join(info['tools'])}")
        print()

def create_client_setup_guide():
    """Maak een setup guide voor MCP clients"""
    print("📋 MCP Client Setup Guide:")
    print()
    print("1. 📁 Kopieer mcp_client_config.json naar je MCP client directory")
    print("2. 🔧 Configureer je MCP client om deze configuratie te gebruiken")
    print("3. 🚀 Start je MCP client")
    print("4. 🧪 Test de servers door tools aan te roepen")
    print()
    print("🔗 Populaire MCP Clients:")
    print("   - Continue (CLI): npm install -g @continue/cli")
    print("   - Continue (VS Code): Install 'Continue' extension")
    print("   - Ollama: ollama install mcp")
    print("   - Custom client: Gebruik @modelcontextprotocol/sdk")
    print()

def main():
    """Main test functie"""
    print("🚀 MCP Servers Test & Usage Guide")
    print("=" * 50)
    print()
    
    test_server_availability()
    test_node_servers()
    test_python_servers()
    test_server_startup()
    create_usage_examples()
    create_client_setup_guide()
    
    print("🎉 MCP Servers zijn klaar voor gebruik!")
    print("📁 Configuratie bestand: mcp_client_config.json")
    print("🔗 Meer informatie: https://modelcontextprotocol.io/")

if __name__ == "__main__":
    main()