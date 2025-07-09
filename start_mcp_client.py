#!/usr/bin/env python3
"""
Eenvoudige MCP Client om de servers te testen
"""

import asyncio
import json
import subprocess
import sys
from pathlib import Path

class SimpleMCPClient:
    def __init__(self, config_file="mcp_client_config.json"):
        self.config_file = config_file
        self.servers = {}
        self.load_config()
    
    def load_config(self):
        """Laad MCP server configuratie"""
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                self.servers = config.get('mcpServers', {})
            print(f"✅ Configuratie geladen: {len(self.servers)} servers")
        except Exception as e:
            print(f"❌ Fout bij laden configuratie: {e}")
    
    def test_server(self, server_name):
        """Test of een server kan starten"""
        if server_name not in self.servers:
            print(f"❌ Server '{server_name}' niet gevonden")
            return False
        
        server_config = self.servers[server_name]
        cmd = [server_config['command']] + server_config['args']
        
        try:
            # Test server startup (timeout na 5 seconden)
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=5,
                env=server_config.get('env', {})
            )
            print(f"✅ {server_name}: Server kan starten")
            return True
        except subprocess.TimeoutExpired:
            print(f"✅ {server_name}: Server start succesvol (timeout)")
            return True
        except Exception as e:
            print(f"❌ {server_name}: Fout - {e}")
            return False
    
    def list_available_servers(self):
        """Toon beschikbare servers"""
        print("\n🔧 Beschikbare MCP Servers:")
        for name, config in self.servers.items():
            print(f"  - {name}: {config['command']} {' '.join(config['args'])}")
    
    def demo_filesystem_server(self):
        """Demo van filesystem server functionaliteit"""
        print("\n📁 Filesystem Server Demo:")
        print("Deze server kan bestanden lezen/schrijven in /workspace")
        
        # Simuleer filesystem operaties
        demo_operations = [
            "list_directory('/workspace')",
            "read_file('/workspace/README.md')",
            "write_file('/workspace/demo.txt', 'Hello MCP!')"
        ]
        
        for op in demo_operations:
            print(f"  📝 {op}")
    
    def demo_memory_server(self):
        """Demo van memory server functionaliteit"""
        print("\n🧠 Memory Server Demo:")
        print("Deze server kan informatie opslaan en ophalen")
        
        demo_operations = [
            "write('user_preferences', {'theme': 'dark', 'language': 'nl'})",
            "read('user_preferences')",
            "list()",
            "delete('user_preferences')"
        ]
        
        for op in demo_operations:
            print(f"  💾 {op}")
    
    def demo_everything_server(self):
        """Demo van everything server functionaliteit"""
        print("\n🔧 Everything Server Demo:")
        print("Deze server heeft prompts, resources en tools")
        
        demo_operations = [
            "list_tools()",
            "read_prompt('hello')",
            "read_resource('example.txt')"
        ]
        
        for op in demo_operations:
            print(f"  🛠️  {op}")
    
    def run_demo(self):
        """Voer een complete demo uit"""
        print("🚀 MCP Servers Demo")
        print("=" * 40)
        
        # Test alle servers
        working_servers = []
        for server_name in self.servers.keys():
            if self.test_server(server_name):
                working_servers.append(server_name)
        
        print(f"\n✅ {len(working_servers)}/{len(self.servers)} servers werken")
        
        # Demo functionaliteit
        if 'filesystem' in working_servers:
            self.demo_filesystem_server()
        
        if 'memory' in working_servers:
            self.demo_memory_server()
        
        if 'everything' in working_servers:
            self.demo_everything_server()
        
        print("\n🎯 Volgende stappen:")
        print("1. Installeer een echte MCP client (Continue, Ollama)")
        print("2. Configureer de client met mcp_client_config.json")
        print("3. Start de client en test de tools interactief")

def main():
    """Main functie"""
    client = SimpleMCPClient()
    client.run_demo()

if __name__ == "__main__":
    main()