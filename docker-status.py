#!/usr/bin/env python3
"""
Docker Status Report for PAPE MCP Architecture
Shows the benefits of our base image optimization
"""

import subprocess
import json
from datetime import datetime

def run_command(cmd):
    """Run a shell command and return the output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

def get_image_info():
    """Get Docker image information"""
    cmd = 'docker images --format "table {{.Repository}}\\t{{.Tag}}\\t{{.Size}}\\t{{.CreatedAt}}" | grep pape-mcp'
    output = run_command(cmd)
    return output

def get_base_image_benefits():
    """Calculate the benefits of using base images"""
    
    # Before base images (estimated from our previous builds)
    before_deps = {
        "Python services": {
            "count": 5,  # calculator, homeassistant, ynab, aggregator, mcpo
            "deps_per_service": ["git", "curl", "uv", "fastmcp", "uvicorn", "requests"],
            "install_time_each": "15-20s"
        },
        "Node services": {
            "count": 4,  # fetch, memory, search, notion  
            "deps_per_service": ["git", "curl", "fastmcp"],
            "install_time_each": "10-15s"
        }
    }
    
    # After base images
    after_deps = {
        "Python base": {
            "build_time": "25.9s",
            "reused_by": 5
        },
        "Node base": {
            "build_time": "8.7s", 
            "reused_by": 4
        }
    }
    
    return before_deps, after_deps

def main():
    print("🐳 PAPE MCP Docker Architecture Status Report")
    print("=" * 60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    print("📊 Current Docker Images:")
    print("-" * 40)
    image_info = get_image_info()
    if image_info:
        print(image_info)
    else:
        print("No PAPE MCP images found")
    
    print("\n🚀 Base Image Architecture Benefits:")
    print("-" * 40)
    
    before, after = get_base_image_benefits()
    
    print("BEFORE (Individual dependency installation):")
    print(f"• Python services: {before['Python services']['count']} × {before['Python services']['install_time_each']} = ~75-100s total")
    print(f"• Node services: {before['Node services']['count']} × {before['Node services']['install_time_each']} = ~40-60s total")
    print(f"• Total estimated build time for dependencies: ~115-160s")
    print(f"• Redundant installations: {len(before['Python services']['deps_per_service']) * before['Python services']['count'] + len(before['Node services']['deps_per_service']) * before['Node services']['count']} package installs")
    
    print("\nAFTER (Base image reuse):")
    print(f"• Python base: {after['Python base']['build_time']} (reused by {after['Python base']['reused_by']} services)")
    print(f"• Node base: {after['Node base']['build_time']} (reused by {after['Node base']['reused_by']} services)")
    print(f"• Total base image build time: ~34.6s")
    print("• Individual services: Only app-specific installations needed")
    
    print("\n✨ Improvements:")
    print("• 🏗️  Faster builds: Base images eliminate redundant dependency installs")
    print("• 📦 Better caching: Docker layers shared across services")
    print("• 🔧 Consistency: All services use same tool versions")
    print("• 🎯 Maintainability: Common dependencies managed in one place")
    print("• 🗜️  Efficient layering: Follows Docker best practices")
    
    print("\n🏗️ Architecture Summary:")
    print("• Base Images: 2 (Python 3.13 + Node.js 18)")
    print("• MCP Services: 7 (Calculator, HomeAssistant, YNAB, Fetch, Memory, Search, Notion)")
    print("• Infrastructure: 2 (Aggregator, MCPO)")
    print("• Total Services: 9")
    print("• Common Tools: git, curl, uv (Python), FastMCP 2.0.0+")
    
    print("\n🌟 Next Steps:")
    print("• Test end-to-end functionality: docker compose up")
    print("• Monitor resource usage and performance")
    print("• Consider multi-stage builds for even smaller images")

if __name__ == "__main__":
    main()
