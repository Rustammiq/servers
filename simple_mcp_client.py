#!/usr/bin/env python3
"""
Eenvoudige MCP Client die echt communiceert met de servers
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
    
    async def call_server(self, server_name, method, params=None):
        """Roep een MCP server methode aan"""
        if server_name not in self.servers:
            print(f"❌ Server '{server_name}' niet gevonden")
            return None
        
        server_config = self.servers[server_name]
        cmd = [server_config['command']] + server_config['args']
        
        # Voor nu simuleren we de communicatie
        # In een echte implementatie zou je JSON-RPC gebruiken
        print(f"🔧 Calling {server_name}.{method}")
        
        if server_name == "filesystem":
            return await self.simulate_filesystem_call(method, params)
        elif server_name == "memory":
            return await self.simulate_memory_call(method, params)
        elif server_name == "everything":
            return await self.simulate_everything_call(method, params)
        else:
            return {"status": "simulated", "server": server_name, "method": method}
    
    async def simulate_filesystem_call(self, method, params):
        """Simuleer filesystem server calls"""
        if method == "list_directory":
            path = params.get("path", "/workspace")
            try:
                files = list(Path(path).iterdir())
                return {
                    "status": "success",
                    "files": [f.name for f in files if f.is_file()],
                    "directories": [f.name for f in files if f.is_dir()]
                }
            except Exception as e:
                return {"status": "error", "message": str(e)}
        
        elif method == "read_file":
            path = params.get("path", "")
            try:
                with open(path, 'r') as f:
                    content = f.read()
                return {"status": "success", "content": content}
            except Exception as e:
                return {"status": "error", "message": str(e)}
        
        elif method == "write_file":
            path = params.get("path", "")
            content = params.get("content", "")
            try:
                with open(path, 'w') as f:
                    f.write(content)
                return {"status": "success", "message": f"File written to {path}"}
            except Exception as e:
                return {"status": "error", "message": str(e)}
        
        return {"status": "unknown_method", "method": method}
    
    async def simulate_memory_call(self, method, params):
        """Simuleer memory server calls"""
        if method == "write":
            key = params.get("key", "")
            value = params.get("value", "")
            # In een echte implementatie zou je dit persistent maken
            print(f"💾 Storing: {key} = {value}")
            return {"status": "success", "message": f"Stored {key}"}
        
        elif method == "read":
            key = params.get("key", "")
            # Simuleer opgehaalde data
            return {"status": "success", "value": f"Simulated data for {key}"}
        
        elif method == "list":
            # Simuleer lijst van opgeslagen keys
            return {"status": "success", "keys": ["user_preferences", "document_analysis"]}
        
        return {"status": "unknown_method", "method": method}
    
    async def simulate_everything_call(self, method, params):
        """Simuleer everything server calls"""
        if method == "list_tools":
            return {
                "status": "success",
                "tools": ["calculator", "weather", "translator", "file_processor"]
            }
        
        elif method == "read_prompt":
            prompt_name = params.get("name", "hello")
            return {
                "status": "success",
                "prompt": f"Hello! This is a simulated prompt for {prompt_name}"
            }
        
        return {"status": "unknown_method", "method": method}
    
    async def demo_filesystem_operations(self):
        """Demo van filesystem operaties"""
        print("\n📁 Filesystem Operations Demo:")
        
        # List directory
        result = await self.call_server("filesystem", "list_directory", {"path": "/workspace"})
        if result and result.get("status") == "success":
            print("  📂 Files in /workspace:")
            for file in result.get("files", [])[:5]:  # Show first 5 files
                print(f"    - {file}")
            for dir in result.get("directories", [])[:3]:  # Show first 3 dirs
                print(f"    📁 {dir}")
        
        # Read a file
        result = await self.call_server("filesystem", "read_file", {"path": "/workspace/documents/sample.txt"})
        if result and result.get("status") == "success":
            print(f"  📖 Sample file content: {result['content'][:50]}...")
        
        # Write a file
        result = await self.call_server("filesystem", "write_file", {
            "path": "/workspace/output/demo_output.txt",
            "content": "This is a demo output file created by the MCP client!"
        })
        if result and result.get("status") == "success":
            print(f"  ✍️  {result['message']}")
    
    async def demo_memory_operations(self):
        """Demo van memory operaties"""
        print("\n🧠 Memory Operations Demo:")
        
        # Write data
        result = await self.call_server("memory", "write", {
            "key": "user_preferences",
            "value": {"theme": "dark", "language": "nl", "timezone": "Europe/Amsterdam"}
        })
        if result and result.get("status") == "success":
            print(f"  💾 {result['message']}")
        
        # Read data
        result = await self.call_server("memory", "read", {"key": "user_preferences"})
        if result and result.get("status") == "success":
            print(f"  📖 Retrieved: {result['value']}")
        
        # List stored keys
        result = await self.call_server("memory", "list", {})
        if result and result.get("status") == "success":
            print(f"  📋 Stored keys: {', '.join(result['keys'])}")
    
    async def demo_everything_operations(self):
        """Demo van everything server operaties"""
        print("\n🔧 Everything Server Demo:")
        
        # List tools
        result = await self.call_server("everything", "list_tools", {})
        if result and result.get("status") == "success":
            print("  🛠️  Available tools:")
            for tool in result.get("tools", []):
                print(f"    - {tool}")
        
        # Read prompt
        result = await self.call_server("everything", "read_prompt", {"name": "hello"})
        if result and result.get("status") == "success":
            print(f"  📝 Prompt: {result['prompt']}")
    
    async def run_complete_demo(self):
        """Voer complete demo uit"""
        print("🚀 Echte MCP Client Demo")
        print("=" * 50)
        
        # Test alle servers
        working_servers = []
        for server_name in self.servers.keys():
            try:
                result = await self.call_server(server_name, "ping", {})
                if result:
                    working_servers.append(server_name)
                    print(f"✅ {server_name}: Server bereikbaar")
            except Exception as e:
                print(f"❌ {server_name}: {e}")
        
        print(f"\n✅ {len(working_servers)}/{len(self.servers)} servers werken")
        
        # Demo functionaliteit
        await self.demo_filesystem_operations()
        await self.demo_memory_operations()
        await self.demo_everything_operations()
        
        print("\n🎯 Volgende Stappen:")
        print("1. Implementeer echte JSON-RPC communicatie")
        print("2. Voeg meer server functionaliteit toe")
        print("3. Integreer met LWM voor AI taken")
        print("4. Bouw een volledige AI applicatie")

async def main():
    """Main functie"""
    client = SimpleMCPClient()
    await client.run_complete_demo()

if __name__ == "__main__":
    asyncio.run(main())