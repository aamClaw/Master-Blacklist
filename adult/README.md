# Adult Category

This category blocks domains related to adult and pornographic content.

## Sources
The blocklist is compiled from multiple reputable sources including:
- Prigent-Adult.txt (DSIBL via Firebog mirror)
- pi_blocklist_porn_top1m.list
- StevenBlack hosts with porn extension

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
4. Commit and push changes (ensure Git LFS is configured for this large file)

## Statistics
- Approximately 4,729,771 unique adult domains
- Format: 0.0.0.0 domain.com (one per line)
- File size: ~161MB (tracked by Git LFS)
- Ready for immediate use in adult content blocking systems