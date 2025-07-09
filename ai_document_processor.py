#!/usr/bin/env python3
"""
AI Document Processor - Combineert MCP servers met LWM
"""

import asyncio
import json
import sys
from pathlib import Path
from datetime import datetime

class AIDocumentProcessor:
    def __init__(self):
        self.config_file = "mcp_client_config.json"
        self.workspace_path = "/workspace"
        self.servers = {}
        self.load_config()
        
    def load_config(self):
        """Laad MCP server configuratie"""
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                self.servers = config.get('mcpServers', {})
            print(f"✅ MCP configuratie geladen: {len(self.servers)} servers")
        except Exception as e:
            print(f"❌ Fout bij laden configuratie: {e}")
    
    async def call_server(self, server_name, method, params=None):
        """Roep een MCP server methode aan"""
        if server_name not in self.servers:
            print(f"❌ Server '{server_name}' niet gevonden")
            return None
        
        # Simuleer server communicatie
        print(f"🔧 Calling {server_name}.{method}")
        
        if server_name == "filesystem":
            return await self.simulate_filesystem_call(method, params)
        elif server_name == "memory":
            return await self.simulate_memory_call(method, params)
        else:
            return {"status": "simulated", "server": server_name, "method": method}
    
    async def simulate_filesystem_call(self, method, params):
        """Simuleer filesystem server calls"""
        if method == "read_file":
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
                Path(path).parent.mkdir(parents=True, exist_ok=True)
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
            print(f"💾 Storing: {key} = {value}")
            return {"status": "success", "message": f"Stored {key}"}
        
        elif method == "read":
            key = params.get("key", "")
            return {"status": "success", "value": f"Simulated data for {key}"}
        
        return {"status": "unknown_method", "method": method}
    
    def simulate_lwm_analysis(self, content):
        """Simuleer LWM tekst analyse"""
        print("🚀 LWM Analysis:")
        
        # Simuleer verschillende soorten analyse
        analysis = {
            "word_count": len(content.split()),
            "sentence_count": len([s for s in content.split('.') if s.strip()]),
            "language": "Nederlands" if any(word in content.lower() for word in ["de", "het", "een", "is", "van"]) else "English",
            "sentiment": "positief" if any(word in content.lower() for word in ["goed", "leuk", "mooi", "geweldig"]) else "neutraal",
            "topics": self.extract_topics(content),
            "summary": self.generate_summary(content)
        }
        
        return analysis
    
    def extract_topics(self, content):
        """Extract topics uit content"""
        topics = []
        content_lower = content.lower()
        
        if any(word in content_lower for word in ["document", "bestand", "file"]):
            topics.append("documenten")
        if any(word in content_lower for word in ["ai", "artificial", "intelligence", "machine"]):
            topics.append("AI/ML")
        if any(word in content_lower for word in ["data", "analyse", "statistiek"]):
            topics.append("data analyse")
        if any(word in content_lower for word in ["video", "film", "beeld"]):
            topics.append("multimedia")
        
        return topics if topics else ["algemeen"]
    
    def generate_summary(self, content):
        """Genereer samenvatting van content"""
        words = content.split()
        if len(words) <= 10:
            return content
        
        # Simuleer samenvatting
        sentences = [s.strip() for s in content.split('.') if s.strip()]
        if len(sentences) <= 2:
            return content
        
        return f"{sentences[0]}. {sentences[1]}..."
    
    async def process_document(self, file_path):
        """Verwerk een document met AI"""
        print(f"\n📄 Processing document: {file_path}")
        print("=" * 50)
        
        # Stap 1: Lees document met MCP filesystem server
        print("1️⃣ Reading document...")
        result = await self.call_server("filesystem", "read_file", {"path": file_path})
        
        if result and result.get("status") == "success":
            content = result["content"]
            print(f"   ✅ Document gelezen ({len(content)} karakters)")
            
            # Stap 2: Analyseer met LWM
            print("2️⃣ Analyzing with LWM...")
            analysis = self.simulate_lwm_analysis(content)
            
            print(f"   📊 Analysis results:")
            print(f"      - Words: {analysis['word_count']}")
            print(f"      - Sentences: {analysis['sentence_count']}")
            print(f"      - Language: {analysis['language']}")
            print(f"      - Sentiment: {analysis['sentiment']}")
            print(f"      - Topics: {', '.join(analysis['topics'])}")
            print(f"      - Summary: {analysis['summary']}")
            
            # Stap 3: Sla analyse op met MCP memory server
            print("3️⃣ Storing analysis...")
            await self.call_server("memory", "write", {
                "key": f"analysis_{Path(file_path).stem}",
                "value": {
                    "timestamp": datetime.now().isoformat(),
                    "file_path": file_path,
                    "analysis": analysis
                }
            })
            
            # Stap 4: Genereer rapport
            print("4️⃣ Generating report...")
            report = self.generate_report(file_path, analysis)
            
            # Stap 5: Sla rapport op
            report_path = f"/workspace/output/analysis_{Path(file_path).stem}.txt"
            await self.call_server("filesystem", "write_file", {
                "path": report_path,
                "content": report
            })
            
            print(f"   ✅ Report saved to: {report_path}")
            
            return analysis
        else:
            error_msg = result.get('message', 'Unknown error') if result else 'No result returned'
            print(f"   ❌ Error reading document: {error_msg}")
            return None
    
    def generate_report(self, file_path, analysis):
        """Genereer een rapport van de analyse"""
        report = f"""
AI Document Analysis Report
==========================

File: {file_path}
Analyzed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 Analysis Results:
- Word Count: {analysis['word_count']}
- Sentence Count: {analysis['sentence_count']}
- Language: {analysis['language']}
- Sentiment: {analysis['sentiment']}
- Topics: {', '.join(analysis['topics'])}

📝 Summary:
{analysis['summary']}

🔍 AI Insights:
- This document appears to be about {', '.join(analysis['topics'])}
- The content has a {analysis['sentiment']} tone
- Written in {analysis['language']}
- Contains {analysis['word_count']} words across {analysis['sentence_count']} sentences

Generated by AI Document Processor
"""
        return report
    
    async def process_multiple_documents(self, directory_path):
        """Verwerk meerdere documenten"""
        print(f"\n📁 Processing all documents in: {directory_path}")
        print("=" * 60)
        
        try:
            doc_dir = Path(directory_path)
            if not doc_dir.exists():
                print(f"❌ Directory not found: {directory_path}")
                return
            
            # Vind alle tekst bestanden
            text_files = list(doc_dir.glob("*.txt")) + list(doc_dir.glob("*.md"))
            
            if not text_files:
                print(f"❌ No text files found in {directory_path}")
                return
            
            print(f"📄 Found {len(text_files)} documents to process")
            
            # Verwerk elk document
            results = []
            for i, file_path in enumerate(text_files, 1):
                print(f"\n[{i}/{len(text_files)}] Processing: {file_path.name}")
                result = await self.process_document(str(file_path))
                if result:
                    results.append(result)
            
            # Genereer overzicht rapport
            if results:
                await self.generate_summary_report(results)
            
            print(f"\n✅ Processing complete! {len(results)} documents analyzed.")
            
        except Exception as e:
            print(f"❌ Error processing documents: {e}")
    
    async def generate_summary_report(self, results):
        """Genereer een overzicht rapport van alle analyses"""
        print("\n📋 Generating summary report...")
        
        summary = f"""
AI Document Processing Summary Report
====================================

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Documents Processed: {len(results)}

📊 Overall Statistics:
- Total Words: {sum(r['word_count'] for r in results)}
- Total Sentences: {sum(r['sentence_count'] for r in results)}
- Average Words per Document: {sum(r['word_count'] for r in results) / len(results):.1f}

🌍 Language Distribution:
- Dutch: {len([r for r in results if r['language'] == 'Nederlands'])}
- English: {len([r for r in results if r['language'] == 'English'])}

😊 Sentiment Analysis:
- Positive: {len([r for r in results if r['sentiment'] == 'positief'])}
- Neutral: {len([r for r in results if r['sentiment'] == 'neutraal'])}

📚 Topic Distribution:
"""
        
        # Tel topics
        all_topics = []
        for result in results:
            all_topics.extend(result['topics'])
        
        topic_counts = {}
        for topic in all_topics:
            topic_counts[topic] = topic_counts.get(topic, 0) + 1
        
        for topic, count in sorted(topic_counts.items(), key=lambda x: x[1], reverse=True):
            summary += f"- {topic}: {count} documents\n"
        
        summary += f"""
🎯 AI Processing Summary:
This batch of documents was successfully processed using:
- MCP Filesystem Server: For document I/O operations
- MCP Memory Server: For storing analysis results
- LWM AI Model: For content analysis and insights

All individual reports have been saved to /workspace/output/
"""
        
        # Sla overzicht rapport op
        summary_path = "/workspace/output/summary_report.txt"
        await self.call_server("filesystem", "write_file", {
            "path": summary_path,
            "content": summary
        })
        
        print(f"   ✅ Summary report saved to: {summary_path}")
    
    async def run_demo(self):
        """Voer een complete demo uit"""
        print("🚀 AI Document Processor Demo")
        print("=" * 60)
        
        # Setup workspace
        Path("/workspace/documents").mkdir(exist_ok=True)
        Path("/workspace/output").mkdir(exist_ok=True)
        
        # Maak voorbeeld documenten
        sample_docs = [
            ("/workspace/documents/ai_intro.txt", 
             "Dit is een document over artificial intelligence en machine learning. "
             "AI is een fascinerend onderwerp dat veel mogelijkheden biedt voor de toekomst."),
            
            ("/workspace/documents/data_analysis.txt",
             "Data analyse is een belangrijk onderdeel van moderne business. "
             "Met de juiste tools kunnen we waardevolle inzichten verkrijgen uit grote datasets."),
            
            ("/workspace/documents/video_processing.txt",
             "Video processing with AI models like LWM can analyze visual content. "
             "This technology enables automatic video description and analysis.")
        ]
        
        for path, content in sample_docs:
            with open(path, 'w') as f:
                f.write(content)
            print(f"📝 Created: {path}")
        
        # Verwerk alle documenten
        await self.process_multiple_documents("/workspace/documents")
        
        print("\n🎯 Demo Complete!")
        print("Check /workspace/output/ for generated reports")

async def main():
    """Main functie"""
    processor = AIDocumentProcessor()
    await processor.run_demo()

if __name__ == "__main__":
    asyncio.run(main())