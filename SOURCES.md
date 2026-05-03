# Sources for Master Blacklist Categories

This document maintains a list of sources (URLs or file paths) for each category's blocklist.
Update the sources here and then run the respective category's scripts to generate the final blocklist.

## How to Use
1. For each category, place the source URLs (one per line) in the corresponding section below.
2. Use the category's scripts to download from these URLs (if they are URLs) or copy local files to the `scripts/raw/` directory.
3. Run the processing scripts to generate the combined blocklist in `scripts/result/` and then copy to the `hosts` file.
4. After updating, you can check the `hosts` file to see if the blocklist has been regenerated.

## Categories

### Ads and Tracking
- Sources for advertising networks, trackers, malware, phishing, ransomware, and spam.
- Example sources (replace with actual URLs or leave empty if using local files):
  ```
### Ads and Tracking
- Sources for advertising networks, trackers, and privacy-invasive services.
- Example sources (replace with actual URLs or leave empty if using local files):
  ```
  https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts.txt
  https://easylist.to/easylist/easylist.txt
  https://easylist.to/easylist/easyprivacy.txt
  https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt
  https://adaway.org/hosts.txt
  https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt
  https://pgl.yoyo.org/adservers/serverlist.php?hostformat=nohtml&mimetype=plaintext
  https://raw.githubusercontent.com/hagezi/dns-blocklists/master/ad-or.txt
  ```
  ```

### Adult
- Sources for adult and pornographic content.
- Example sources:
  ```
  # Example:
  # https://v.firebog.net/hosts/Prigent-Adult.txt
  # https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list
  # https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts
  ```

### Gambling
- Sources for online gambling and betting sites.
- Example sources:
  ```
  # Example:
  # https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling/hosts
  # https://mirror1.malwaredomains.com/files/justdomains
  ```

### Dating
- Sources for dating services and related domains.
- Example sources:
  ```
  # Example:
  # https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
  # https://v.firebog.net/hosts/Prigent-Adult.txt
  ```

### Bypass
- Sources for tools used to bypass filtering (VPN, proxy, Tor, DNS-over-HTTPS, etc.).
- Example sources:
  ```
  # Example:
  # https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
  # https://mirror1.malwaredomains.com/files/justdomains
  # https://sslbl.abuse.ch/blacklist/sslipblacklist.csv
  # https://risk.rudischosting.com/
  ```

## Notes
- Replace the example URLs with the actual sources you wish to use.
- If you have local source files, you can copy them directly to the `scripts/raw/` directory of each category.
- After updating the sources, run the category's Python scripts to process and generate the blocklist.
- The final blocklist will be in the category's `hosts` file.
- You can consider this category's sources "done" when you have updated the SOURCES.md, run the scripts, and verified the `hosts` file is up to date.

## Updating Sources
To update the sources for a category:
1. Edit this SOURCES.md file and update the URLs for the desired category.
2. Use the category's scripts to download from the URLs (if the scripts are set up to read from this file or from a config) OR manually copy the downloaded files to `scripts/raw/`.
3. Run the processing scripts.
4. Copy the final organized blocklist from `scripts/result/` to the category's `hosts` file.

## Notification
Since automated notifications are not set up in this environment, you can manually verify the update by:
- Checking the timestamp of the `hosts` file.
- Reviewing the content of the `hosts` file to ensure it reflects the latest sources.
- Checking the output of your scripts for any errors or completion messages.

## Current Status (as of latest updates)
- ads_and_tracking: ~325,817 domains
- adult: ~4,729,771 domains
- dating: ~581,785 domains
- gambling: ~119 domains
- bypass: ~88,704 domains