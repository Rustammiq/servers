#!/usr/bin/env python3
"""
LWM Demo Script
Toont hoe je LWM kunt gebruiken voor verschillende taken
"""

import sys
import os
import jax
import jax.numpy as jnp
import numpy as np

def demo_lwm_configs():
    """Demo van verschillende LWM configuraties"""
    print("🚀 LWM Configuratie Demo")
    print("=" * 40)
    
    try:
        # Voeg LWM path toe
        lwm_path = "/Users/innovars_lab/servers/LWM"
        if os.path.exists(lwm_path):
            sys.path.append(lwm_path)
            from lwm.llama import LLaMAConfig, LLAMA_STANDARD_CONFIGS
            
            print("✅ LWM modules geladen!")
            
            # Toon alle beschikbare configuraties
            print("\n📋 Beschikbare Model Configuraties:")
            for name, config in LLAMA_STANDARD_CONFIGS.items():
                params = config['hidden_size'] * config['num_hidden_layers'] * 4  # Rough estimate
                print(f"  - {name:>6}: {config['hidden_size']:>4}d, {config['num_hidden_layers']:>2} layers (~{params//1e6}M params)")
            
            # Maak een debug config voor demo
            debug_config = LLaMAConfig(**LLAMA_STANDARD_CONFIGS['debug'])
            print(f"\n🐛 Debug Config: {debug_config.hidden_size}d, {debug_config.num_hidden_layers} layers")
            
            return True
            
        else:
            print(f"❌ LWM directory niet gevonden: {lwm_path}")
            return False
            
    except ImportError as e:
        print(f"❌ Import fout: {e}")
        print("💡 Tip: Activeer het LWM environment: source lwm_env/bin/activate")
        return False

def demo_jax_computation():
    """Demo van JAX berekeningen"""
    print("\n🔧 JAX Computation Demo:")
    
    # Eenvoudige berekeningen
    x = jnp.array([1.0, 2.0, 3.0, 4.0])
    y = jnp.sum(x)
    z = jnp.mean(x)
    
    print(f"  Input: {x}")
    print(f"  Sum: {y}")
    print(f"  Mean: {z}")
    
    # Matrix operaties
    A = jnp.array([[1, 2], [3, 4]])
    B = jnp.array([[5, 6], [7, 8]])
    C = jnp.dot(A, B)
    
    print(f"  Matrix A: {A}")
    print(f"  Matrix B: {B}")
    print(f"  A × B: {C}")

def demo_model_creation():
    """Demo van model creatie"""
    print("\n🏗️  Model Creation Demo:")
    
    try:
        from lwm.llama import LLaMAConfig, FlaxLLaMAForCausalLM, LLAMA_STANDARD_CONFIGS
        
        # Gebruik debug config voor snelle demo
        config = LLaMAConfig(**LLAMA_STANDARD_CONFIGS['debug'])
        
        print(f"  Configuratie: {config.hidden_size}d, {config.num_hidden_layers} layers")
        print(f"  Vocab size: {config.vocab_size}")
        print(f"  Max sequence length: {config.max_sequence_length}")
        
        # Maak model (zonder weights)
        model = FlaxLLaMAForCausalLM(config)
        print("  ✅ Model architecture created successfully!")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Model creatie fout: {e}")
        return False

def demo_training_scenarios():
    """Demo van training scenario's"""
    print("\n🎯 Training Scenario's:")
    
    scenarios = [
        {
            "name": "Text Training",
            "model": "200M",
            "data": "Tekst data (boeken, artikelen)",
            "script": "run_train_text.sh",
            "use_case": "Taal modellen trainen"
        },
        {
            "name": "Vision + Text Training", 
            "model": "1B-7B",
            "data": "Video + tekst data",
            "script": "run_train_vision_text.sh",
            "use_case": "Multimodale modellen"
        },
        {
            "name": "Vision Chat",
            "model": "3B-13B",
            "data": "Video + dialoog data",
            "script": "run_vision_chat.sh",
            "use_case": "Video chat applicaties"
        }
    ]
    
    for scenario in scenarios:
        print(f"  📝 {scenario['name']}")
        print(f"     Model: {scenario['model']}")
        print(f"     Data: {scenario['data']}")
        print(f"     Script: {scenario['script']}")
        print(f"     Use case: {scenario['use_case']}")
        print()

def demo_inference_setup():
    """Demo van inference setup"""
    print("\n🤖 Inference Setup:")
    
    steps = [
        "1. Download pre-trained weights van LWM repository",
        "2. Laad model met weights",
        "3. Voorbereid input (tekst/video)",
        "4. Voer inference uit",
        "5. Verwerk output"
    ]
    
    for step in steps:
        print(f"  {step}")
    
    print("\n💡 Voor inference heb je pre-trained weights nodig!")
    print("   Download van: https://github.com/LargeWorldModel/LWM")

def main():
    """Main demo functie"""
    print("🚀 Large World Model (LWM) Demo")
    print("=" * 50)
    
    # Test configuraties
    if demo_lwm_configs():
        # Demo JAX
        demo_jax_computation()
        
        # Demo model creatie
        if demo_model_creation():
            # Demo training scenario's
            demo_training_scenarios()
            
            # Demo inference setup
            demo_inference_setup()
    
    print("\n🎯 Volgende stappen:")
    print("1. Download pre-trained weights voor inference")
    print("2. Bekijk training scripts in scripts/ directory")
    print("3. Experimenteer met verschillende model sizes")
    print("4. Combineer met MCP servers voor geavanceerde applicaties")

if __name__ == "__main__":
    main()