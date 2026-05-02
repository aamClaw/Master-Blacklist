# Master Blacklist

This repository contains a unified blocklist combining adult and dating categories for use in DNS-based ad blockers (like Pi-hole) or similar filtering systems.

## Source

The blocklist is derived from the [bon-appetit-44-sources](https://github.com/bon-appetit/porn-domains) project, which aggregates 44 various blocklists related to adult content. This unified list already includes a wide range of adult and dating-related domains.

## Files

- `combined/adult_and_dating_unified.hosts`: The unified blocklist in format suitable for Pi-hole (0.0.0.0 domain.com)
- `project.md`: Detailed project documentation

## Usage

Pi-hole users can add this list as an adlist by pointing to the raw file URL or by downloading and adding locally.

## Notes

- The list is extensive and may contain over 3.5 million domains.
- Consider using a DNSBL that supports large lists efficiently.
- Regular updates are recommended as the source blocklists are frequently updated.

## Credits

Based on the work of the bon-appetit/porn-domains project and its contributors.