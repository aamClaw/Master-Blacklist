# Bypass Category

This category blocks domains related to tools used to bypass filtering (VPN, DNS proxy, Tor, etc.).

## Sources
The blocklist is compiled from multiple reputable sources including:
- StevenBlack hosts
- Energized Protection blocklist
- PolishFiltersTeam/KADhosts
- FadeMind/hosts.extras Risk list

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
- Approximately 88,704 unique domains
- Format: 0.0.0.0 domain.com (one per line)
- Ready for immediate use in blocking bypass services