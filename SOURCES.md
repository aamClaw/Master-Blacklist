# Sources for Master Blacklist Categories

This document maintains a list of sources (URLs or file paths) for each category's blocklist.
Update the sources here and then run the respective category's scripts to generate the final blocklist.

## How to Use
1. For each category, place the source URLs (one per line) in the corresponding section below.
2. Use the category's scripts to download from these URLs (if they are URLs) or copy local files to the `scripts/raw/` directory.
3. Run the processing scripts to generate the combined blocklist in `scripts/result/` and then copy to the `hosts` file.
4. After updating, you can check the `hosts` file to see if the blocklist has been regenerated.

## Categories

### Ads
- Sources for advertising networks, trackers, and analytics.
- Example sources (replace with actual URLs or leave empty if using local files):
  ```
  https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts.txt
  https://easylist.to/easylist/easylist.txt
  https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt
  https://adaway.org/hosts.txt
  https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt
  https://pgl.yoyo.org/adservers/serverlist.php?hostformat=nohtml&mimetype=plaintext
  https://raw.githubusercontent.com/hagezi/dns-blocklists/master/ad-or.txt
  ```