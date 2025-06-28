#!/usr/bin/env python3
"""
English Language Lint Test for CTMCK Repository
Ensures no Portuguese content remains in the repository
"""

import re
import os
from pathlib import Path

def check_english_only():
    """Check that repository contains only English text"""
    
    project_root = Path(__file__).resolve().parents[1]
    
    # Portuguese stop words to detect
    portuguese_patterns = [
        r'\bIniciando\b', r'\bInici\b', r'\bEstrel\b', 
        r'\bTempo_\b', r'\bHabitabilidade\b', r'\bAnálise\b',
        r'\bcorrelação\b', r'\bestelar\b', r'\btemporal\b',
        r'\bGerando\b', r'\bMapa\b', r'\bDados\b',
        r'\bAutor\b', r'\bData\b', r'\bProjeto\b'
    ]
    
    # Files to check
    file_patterns = [
        '**/*.py', '**/*.md', '**/*.tex', '**/*.txt'
    ]
    
    violations = []
    
    for pattern in file_patterns:
        for file_path in project_root.glob(pattern):
            # Skip certain directories
            if any(skip in str(file_path) for skip in ['.git', '__pycache__', 'archive']):
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                for pt_pattern in portuguese_patterns:
                    if re.search(pt_pattern, content, re.IGNORECASE):
                        violations.append((file_path, pt_pattern))
                        
            except (UnicodeDecodeError, PermissionError):
                continue
    
    return violations

def main():
    """Main test function"""
    print("🔍 Checking repository for English-only content...")
    
    violations = check_english_only()
    
    if violations:
        print(f"❌ Found {len(violations)} Portuguese content violations:")
        for file_path, pattern in violations:
            print(f"   {file_path}: {pattern}")
        return False
    else:
        print("✅ Repository is English-only compliant!")
        return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
