# Ads and Tracking Category

This category blocks domains related to advertising, tracking, malware, phishing, ransomware, and spam.

## Sources
The blocklist is compiled from multiple reputable sources including:
- EasyList (general ad-blocking filters)
- EasyPrivacy (privacy-tracking filters)
- uBlock Origin filters
- StevenBlack hosts (merged adware/malware hosts)
- adaway (mobile ad providers)
- hagezi DNS blocklists
- pgl.yoyo.org adservers list
- BlockList Project ads list

## Usage
The final blocklist is located at `hosts` and contains domains in the format:
```
0.0.0.0 example.com
```

This file can be used directly with DNS-based blockers like:
- Pi-hole
- AdGuard Home
- NextDNS
- unbound
- BIND

## Maintenance
To update this blocklist:
1. Add/update source URLs in `sorce.txt` (one per line)
2. Run the Python scripts in `scripts/` to:
   - Download sources to `scripts/raw/`
   - Process domains to `0.0.0.0` format
   - Remove duplicates and sort
   - Generate final list in `scripts/result/`
3. Copy the result to `hosts` file
4. Commit and push changes

## Statistics
- Approximately 277,874 unique domains
- Format: 0.0.0.0 domain.com (one per line)
- Ready for immediate use in blocking systems