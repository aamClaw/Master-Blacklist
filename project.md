# Master Blacklist Project

## Goal and Scope
Create an organized blacklist system with separate categories for different types of threats and unwanted content. Each category maintains its own blocklist file, scripts, and documentation.

## Structure
The project follows this directory structure:

```
My-project/ (this workspace/aamClaw/Master-Blacklist)
├── ads_and_tracking/
│   ├── hosts             # Final blocklist file for ads and tracking (single file, format: 0.0.0.0 domain per line)
│   ├── README.md         # Category-specific information
│   ├── sorce.txt         # List of source URLs (one per line) for quick download
│   └── scripts/          # Python scripts for processing this category
│       ├── raw/          # Source host files (downloaded from various sources)
│       └── result/       # Combined, organized, and deduplicated host file (before final hosts)
├── adult/
│   ├── hosts             # Final blocklist file for adult content (single file, format: 0.0.0.0 domain per line) - Git LFS tracked
│   ├── README.md         # Category-specific information
│   ├── sorce.txt         # List of source URLs (one per line) for quick download
│   └── scripts/          # Python scripts for processing this category
│       ├── raw/          # Source host files (downloaded from various sources)
│       └── result/       # Combined, organized, and deduplicated host file (before final hosts)
├── gambling/
│   ├── hosts             # Final blocklist file for gambling (single file, format: 0.0.0.0 domain per line)
│   ├── README.md         # Category-specific information
│   ├── sorce.txt         # List of source URLs (one per line) for quick download
│   └── scripts/          # Python scripts for processing this category
│       ├── raw/          # Source host files (downloaded from various sources)
│       └── result/       # Combined, organized, and deduplicated host file (before final hosts)
├── dating/
│   ├── hosts             # Final blocklist file for dating (single file, format: 0.0.0.0 domain per line)
│   ├── README.md         # Category-specific information
│   ├── sorce.txt         # List of source URLs (one per line) for quick download
│   └── scripts/          # Python scripts for processing this category
│       ├── raw/          # Source host files (downloaded from various sources)
│       └── result/       # Combined, organized, and deduplicated host file (before final hosts)
├── bypass/
│   ├── hosts             # Final blocklist file for bypass (VPN, proxy, Tor, etc.) (single file, format: 0.0.0.0 domain per line)
│   ├── README.md         # Category-specific information
│   ├── sorce.txt         # List of source URLs (one per line) for quick download
│   └── scripts/          # Python scripts for processing this category
│       ├── raw/          # Source host files (downloaded from various sources)
│       └── result/       # Combined, organized, and deduplicated host file (before final hosts)
└── README.md             # This file: overall project overview
```

## Key Features
- **Separate Categories**: Each threat/content type is isolated in its own directory.
- **Python Scripts Only**: All processing scripts are Python and reside in each category's `scripts/` folder.
- **Hosts File**: Each category's `hosts` file (not a directory) contains the final blocklist in the standard format (e.g., `0.0.0.0 domain.com` per line) for use in DNS-based blockers like Pi-hole.
- **Sorce.txt**: Each category's `sorce.txt` file contains a list of source URLs (one per line) for quick download and reference.
- **Scripts Subdirectories**:
  - `raw/` contains the source host files (as downloaded, one file per source).
  - `result/` contains the combined, organized, and deduplicated host file (before final `hosts` file).
- **README per Category**: Each category has its own README.md detailing sources, usage, and any special notes.
- **Note**: The adult category is very large (~161MB) and is tracked by Git LFS to handle large files efficiently.

## Usage
1. For each category, edit `sorce.txt` to include the URLs of the source blocklists (one URL per line).
2. Use the Python scripts in `scripts/` to download the sources from the URLs in `sorce.txt` (or you can manually place downloaded files in `scripts/raw/`).
3. The scripts should process the raw files (e.g., convert to standard format, remove duplicates, etc.) and place the combined, organized result in `scripts/result/`.
4. Then, copy or move the final organized host file from `scripts/result/` to the category's `hosts` file (overwriting the previous version).
5. The resulting `hosts` file can be used directly with DNS-based blockers like Pi-hole.

## Maintenance
- Update the URLs in `sorce.txt` as needed and re-run the category's scripts to regenerate the blocklist.
- Each category is independent; updating one does not affect others.
- For the adult category, ensure Git LFS is properly configured to handle the large file size.

## Notes
- Ensure Python is installed to run the scripts.
- Scripts should be written to output blocklists in standard format (e.g., `0.0.0.0 domain.com` per line) for compatibility.
- The `hosts` file is a plain text file, one domain per line, optionally prefixed with `0.0.0.0` (or `127.0.0.1`) for use in blockers.
- Current approximate domain counts (as of latest updates):
  - ads_and_tracking: ~325,000 domains
  - adult: ~4,730,000 domains 
  - dating: ~582,000 domains
  - gambling: ~119 domains
  - bypass: ~88,700 domains