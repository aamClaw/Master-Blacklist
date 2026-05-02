# Master Blacklist Project

## Goal and Scope
Create a organized blacklist system with separate categories for different types of threats and unwanted content. Each category maintains its own blocklist file, scripts, and documentation.

## Structure
The project follows this directory structure:

```
My-project/ (this workspace/aamClaw/Master-Blacklist)
├── ads/
│   ├── hosts             # Final blocklist file for ads (single file, not a directory)
│   ├── README.md         # Category-specific information
│   └── scripts/          # Python scripts for processing this category
│       ├── raw/          # Source host files (downloaded from various sources)
│       └── result/       # Combined, organized, and deduplicated host file (before final hosts)
├── tracking/
│   ├── hosts
│   ├── README.md
│   └── scripts/
│       ├── raw/
│       └── result/
├── malware/
│   ├── hosts
│   ├── README.md
│   └── scripts/
│       ├── raw/
│       └── result/
├── phishing/
│   ├── hosts
│   ├── README.md
│   └── scripts/
│       ├── raw/
│       └── result/
├── ransomware/
│   ├── hosts
│   ├── README.md
│   └── scripts/
│       ├── raw/
│       └── result/
├── spam/
│   ├── hosts
│   ├── README.md
│   └── scripts/
│       ├── raw/
│       └── result/
├── adult/
│   ├── hosts
│   ├── README.md
│   └── scripts/
│       ├── raw/
│       └── result/
├── gambling/
│   ├── hosts
│   ├── README.md
│   └── scripts/
│       ├── raw/
│       └── result/
├── dating/
│   ├── hosts
│   ├── README.md
│   └── scripts/
│       ├── raw/
│       └── result/
├── bypass/
│   ├── hosts
│   ├── README.md
│   └── scripts/
│       ├── raw/
│       └── result/
└── README.md             # This file: overall project overview
```

## Key Features
- **Separate Categories**: Each threat/content type is isolated in its own directory.
- **Python Scripts Only**: All processing scripts are Python and reside in each category's `scripts/` folder.
- **Hosts File**: Each category's `hosts` file (not a directory) contains the final blocklist (ready for use in Pi-hole, ad blockers, etc.).
- **Scripts Subdirectories**:
  - `raw/` contains the source host files (as downloaded, one file per source).
  - `result/` contains the combined, organized, and deduplicated host file (before final `hosts` file).
- **README per Category**: Each category has its own README.md detailing sources, usage, and any special notes.
- **Extensible**: New categories can be added by duplicating the directory structure.

## Usage
1. For each category, place raw source blocklists in the `scripts/raw/` directory or fetch them via the category's scripts.
2. Use the Python scripts in `scripts/` to process, deduplicate, and combine the raw files, placing the result in `scripts/result/` (e.g., as a temporary combined file).
3. Then, move or copy the final organized host file from `scripts/result/` to the category's `hosts` file (overwriting the previous version).
4. The resulting `hosts` file can be used directly with DNS-based blockers like Pi-hole.

## Maintenance
- Update sources in `scripts/raw/` as needed and re-run the category's scripts to regenerate the blocklist.
- Each category is independent; updating one does not affect others.

## Notes
- Ensure Python is installed to run the scripts.
- Scripts should be written to output blocklists in standard format (e.g., `0.0.0.0 domain.com` per line) for compatibility.
- The `hosts` file is a plain text file, one domain per line, optionally prefixed with `0.0.0.0` (or `127.0.0.1`) for use in blockers.