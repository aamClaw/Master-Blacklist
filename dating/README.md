# Dating Category

This category blocks domains related to dating services and dating websites.

## Sources
The blocklist is compiled from multiple reputable sources including:
- StevenBlack hosts
- Prigent-Adult.txt (adult content domains that often overlap with dating)

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
- Approximately 581,785 unique dating-related domains
- Format: 0.0.0.0 domain.com (one per line)
- Ready for immediate use in dating site blocking systems