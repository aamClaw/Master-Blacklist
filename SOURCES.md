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
  ```### Tracking
- Sources for tracking domains and privacy-invasive services.
- Example sources:
  ```
  https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts.txt
  https://easylist.to/easylist/easyprivacy.txt
  ```### Malware
- Sources for malware domains, command and control servers, and exploit kits.
- Example sources:
  ```
  # Example:
  # https://malwaredomains.com/files/justdomains
  # https://urlhaus.abuse.ch/downloads/text_online/
  ```

### Phishing
- Sources for phishing and fraudulent websites.
- Example sources:
  ```
  # Example:
  # https://openphish.com/feed.txt
  # https://phishtank.com/phish_online.php
  ```

### Ransomware
- Sources for ransomware distribution sites and related domains.
- Example sources:
  ```
  # Example:
  # https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt
  ```

### Spam
- Sources for spam domains and spam-related services.
- Example sources:
  ```
  # Example:
  # https://spamhaus.org/drop/drop.txt
  ```

### Adult
- Sources for adult and pornographic content.
- Example sources:
  ```
  # Example:
  # https://raw.githubusercontent.com/v2fly/domain-list-community/master/data/category-porn
  # https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-domains.txt
  ```

### Gambling
- Sources for online gambling and betting sites.
- Example sources:
  ```
  # Example:
  # https://www.gamblingblocklist.com/downloads/gambling_domains.txt
  ```

### Dating
- Sources for dating services and related domains.
- Example sources:
  ```
  # Example:
  # https://raw.githubusercontent.com/StephenH518/hosts/master/domains/dating.txt
  ```

### Bypass
- Sources for tools used to bypass filtering (VPN, proxy, Tor, DNS-over-HTTPS, etc.).
- Example sources:
  ```
  # Example:
  # https://www.dnsbl.net.au/contrib/blaze-vpnipspace.txt
  # https://www.cloudflare.com/ips-v4
  # https://www.cloudflare.com/ips-v6
  # https://www.torproject.org/projects/torbot/conf
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
