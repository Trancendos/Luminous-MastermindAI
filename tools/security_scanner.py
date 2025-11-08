#!/usr/bin/env python3
"""
Security Scanner for AI-Generated Code

This script scans AI-generated code for common security vulnerabilities
based on OWASP guidelines and best practices.
"""

import re
import sys
import json
from pathlib import Path
from typing import List, Dict, Any


class SecurityScanner:
    """A simple security scanner for AI-generated code."""
    
    def __init__(self):
        self.vulnerabilities = []
        
    def scan_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Scan a file for security vulnerabilities.
        
        Args:
            file_path: Path to the file to scan
            
        Returns:
            List of vulnerabilities found
        """
        self.vulnerabilities = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                
            # Run all security checks
            self._check_hardcoded_credentials(lines)
            self._check_sql_injection(lines)
            self._check_command_injection(lines)
            self._check_xss_vulnerabilities(lines)
            self._check_insecure_crypto(lines)
            self._check_eval_usage(lines)
            self._check_unsafe_deserialization(lines)
            
        except Exception as e:
            self.vulnerabilities.append({
                'severity': 'ERROR',
                'type': 'File Read Error',
                'line': 0,
                'description': f'Error reading file: {str(e)}'
            })
            
        return self.vulnerabilities
    
    def _check_hardcoded_credentials(self, lines: List[str]):
        """Check for hardcoded credentials."""
        patterns = [
            (r'password\s*=\s*["\'][^"\']+["\']', 'Hardcoded password'),
            (r'api_key\s*=\s*["\'][^"\']+["\']', 'Hardcoded API key'),
            (r'secret\s*=\s*["\'][^"\']+["\']', 'Hardcoded secret'),
            (r'token\s*=\s*["\'][^"\']+["\']', 'Hardcoded token'),
        ]
        
        for line_num, line in enumerate(lines, 1):
            for pattern, description in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    self.vulnerabilities.append({
                        'severity': 'HIGH',
                        'type': 'Hardcoded Credentials',
                        'line': line_num,
                        'description': description,
                        'recommendation': 'Use environment variables or secure credential management systems'
                    })
    
    def _check_sql_injection(self, lines: List[str]):
        """Check for potential SQL injection vulnerabilities."""
        patterns = [
            (r'execute\s*\(\s*["\'].*%s.*["\']', 'String formatting in SQL query'),
            (r'execute\s*\(\s*f["\']', 'F-string in SQL query'),
            (r'execute\s*\(\s*.*\+.*\)', 'String concatenation in SQL query'),
        ]
        
        for line_num, line in enumerate(lines, 1):
            for pattern, description in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    self.vulnerabilities.append({
                        'severity': 'CRITICAL',
                        'type': 'SQL Injection',
                        'line': line_num,
                        'description': description,
                        'recommendation': 'Use parameterized queries or prepared statements'
                    })
    
    def _check_command_injection(self, lines: List[str]):
        """Check for potential command injection vulnerabilities."""
        patterns = [
            (r'os\.system\s*\(', 'Use of os.system'),
            (r'subprocess\.call\s*\(.*shell\s*=\s*True', 'Use of subprocess with shell=True'),
            (r'eval\s*\(', 'Use of eval function'),
            (r'exec\s*\(', 'Use of exec function'),
        ]
        
        for line_num, line in enumerate(lines, 1):
            for pattern, description in patterns:
                if re.search(pattern, line):
                    self.vulnerabilities.append({
                        'severity': 'CRITICAL',
                        'type': 'Command Injection',
                        'line': line_num,
                        'description': description,
                        'recommendation': 'Avoid dynamic command execution; use safe alternatives'
                    })
    
    def _check_xss_vulnerabilities(self, lines: List[str]):
        """Check for potential XSS vulnerabilities."""
        patterns = [
            (r'innerHTML\s*=', 'Use of innerHTML'),
            (r'document\.write\s*\(', 'Use of document.write'),
            (r'dangerouslySetInnerHTML', 'Use of dangerouslySetInnerHTML'),
        ]
        
        for line_num, line in enumerate(lines, 1):
            for pattern, description in patterns:
                if re.search(pattern, line):
                    self.vulnerabilities.append({
                        'severity': 'HIGH',
                        'type': 'Cross-Site Scripting (XSS)',
                        'line': line_num,
                        'description': description,
                        'recommendation': 'Sanitize and escape user input; use safe DOM manipulation methods'
                    })
    
    def _check_insecure_crypto(self, lines: List[str]):
        """Check for use of insecure cryptographic algorithms."""
        patterns = [
            (r'MD5', 'Use of MD5 hash'),
            (r'SHA1', 'Use of SHA1 hash'),
            (r'DES', 'Use of DES encryption'),
        ]
        
        for line_num, line in enumerate(lines, 1):
            for pattern, description in patterns:
                if re.search(pattern, line):
                    self.vulnerabilities.append({
                        'severity': 'MEDIUM',
                        'type': 'Weak Cryptography',
                        'line': line_num,
                        'description': description,
                        'recommendation': 'Use modern cryptographic algorithms (e.g., SHA-256, AES)'
                    })
    
    def _check_eval_usage(self, lines: List[str]):
        """Check for dangerous eval usage."""
        patterns = [
            (r'\beval\s*\(', 'Use of eval'),
            (r'Function\s*\(', 'Use of Function constructor'),
        ]
        
        for line_num, line in enumerate(lines, 1):
            for pattern, description in patterns:
                if re.search(pattern, line):
                    self.vulnerabilities.append({
                        'severity': 'CRITICAL',
                        'type': 'Code Injection',
                        'line': line_num,
                        'description': description,
                        'recommendation': 'Avoid eval and dynamic code execution'
                    })
    
    def _check_unsafe_deserialization(self, lines: List[str]):
        """Check for unsafe deserialization."""
        patterns = [
            (r'pickle\.loads\s*\(', 'Use of pickle.loads'),
            (r'yaml\.load\s*\(', 'Use of yaml.load without safe loader'),
        ]
        
        for line_num, line in enumerate(lines, 1):
            for pattern, description in patterns:
                if re.search(pattern, line):
                    self.vulnerabilities.append({
                        'severity': 'HIGH',
                        'type': 'Insecure Deserialization',
                        'line': line_num,
                        'description': description,
                        'recommendation': 'Use safe deserialization methods; validate input'
                    })
    
    def generate_report(self, output_format: str = 'json') -> str:
        """
        Generate a security report.
        
        Args:
            output_format: Format of the report ('json' or 'text')
            
        Returns:
            Formatted report
        """
        if output_format == 'json':
            return json.dumps(self.vulnerabilities, indent=2)
        else:
            report = "Security Scan Report\n"
            report += "=" * 50 + "\n\n"
            
            if not self.vulnerabilities:
                report += "No vulnerabilities found.\n"
            else:
                report += f"Found {len(self.vulnerabilities)} potential issues:\n\n"
                
                for vuln in self.vulnerabilities:
                    report += f"[{vuln['severity']}] {vuln['type']}\n"
                    report += f"  Line: {vuln['line']}\n"
                    report += f"  Description: {vuln['description']}\n"
                    if 'recommendation' in vuln:
                        report += f"  Recommendation: {vuln['recommendation']}\n"
                    report += "\n"
            
            return report


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python security_scanner.py <file_path> [output_format]")
        print("Output formats: json, text (default: text)")
        sys.exit(1)
    
    file_path = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else 'text'
    
    if not Path(file_path).exists():
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    
    scanner = SecurityScanner()
    scanner.scan_file(file_path)
    
    report = scanner.generate_report(output_format)
    print(report)


if __name__ == '__main__':
    main()
