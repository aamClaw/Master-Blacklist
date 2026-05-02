#!/usr/bin/env python3
import re
import os
import sys

def extract_domains_from_line(line):
    line = line.strip()
    if not line:
        return []
    # Skip security notice lines from web_fetch
    if line.startswith('SECURITY NOTICE') or 'Source: Web Fetch' in line:
        return []
    # Skip comments
    if line.startswith('!') or line.startswith('[') or line.startswith('#'):
        return []
    domains = []
    # Remove everything after '$' (options in filter lists)
    if '$' in line:
        line = line.split('$')[0]
    # For hosts file format: 0.0.0.0 domain or 127.0.0.1 domain
    if line.startswith('0.0.0.0') or line.startswith('127.0.0.1'):
        parts = line.split()
        if len(parts) >= 2:
            domain = parts[1]
            # Sometimes there are more parts like '0.0.0.0 domain.com # comment'
            # Remove any trailing comment
            if '#' in domain:
                domain = domain.split('#')[0]
            domain = domain.strip()
            if domain and domain not in ('0.0.0.0', '127.0.0.1'):
                domains.append(domain)
        return domains
    # For Adblock Plus/uBlock filters: ||domain.com^ or |http://domain.com
    # Handle ||domain.com^
    if line.startswith('||'):
        # Extract between || and ^
        match = re.match(r'^\|\|([^\/^]+)(?:[\/\^]|$)', line)
        if match:
            domain = match.group(1)
            domains.append(domain)
        return domains
    # Handle |http://domain.com or |https://domain.com
    if line.startswith('|http://') or line.startswith('|https://'):
        proto = 'http://' if line.startswith('|http://') else 'https://'
        rest = line[1+len(proto):]  # remove the leading | and protocol
        # Extract domain until first / or ^ or end
        match = re.match(r'^([^\/^\?]+)', rest)
        if match:
            domain = match.group(1)
            domains.append(domain)
        return domains
    # Handle plain domain (e.g., from yoyo list)
    # Remove any trailing comment
    if '#' in line:
        line = line.split('#')[0]
    line = line.strip()
    # Basic domain check: contains a dot, no spaces, doesn't start with digit (to avoid IPs)
    if line and '.' in line and ' ' not in line and not line[0].isdigit():
        # Additional safety: should not contain slashes or other weird chars (already stripped)
        domains.append(line)
        return domains
    # If none of the above, return empty
    return domains

def process_file(filepath):
    domains = set()
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                for domain in extract_domains_from_line(line):
                    if domain:
                        domains.add(domain)
    except Exception as e:
        print(f"Error processing {filepath}: {e}", file=sys.stderr)
    return domains

def main():
    raw_dir = '/home/masud/.openclaw/workspace/ads_and_tracking/scripts/raw'
    output_file = '/home/masud/.openclaw/workspace/ads_and_tracking/hosts'
    all_domains = set()
    for filename in os.listdir(raw_dir):
        if filename.endswith('.txt'):
            filepath = os.path.join(raw_dir, filename)
            print(f"Processing {filename}...")
            domains = process_file(filepath)
            print(f"  Found {len(domains)} domains")
            all_domains.update(domains)
    # Sort domains
    sorted_domains = sorted(all_domains)
    # Write to output file in 0.0.0.0 domain format
    with open(output_file, 'w') as f:
        for domain in sorted_domains:
            f.write(f"0.0.0.0 {domain}\n")
    print(f"Total unique domains: {len(sorted_domains)}")
    print(f"Written to {output_file}")

if __name__ == '__main__':
    main()