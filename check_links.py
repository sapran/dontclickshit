#!/usr/bin/env python3
"""
Script to check all external links in the dontclickshit documentation.
"""

import re
import sys
import urllib.request
import urllib.error
from typing import List, Tuple, Dict
from collections import defaultdict

def extract_urls_from_file(filepath: str) -> List[Tuple[str, int]]:
    """Extract all URLs from a markdown file with line numbers."""
    urls = []
    url_pattern = re.compile(r'https?://[^\s\)\]]+')

    with open(filepath, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            matches = url_pattern.findall(line)
            for url in matches:
                # Clean up trailing punctuation that might be part of markdown
                url = url.rstrip(')')
                url = url.rstrip(']')
                urls.append((url, line_num))

    return urls

def check_url(url: str, timeout: int = 10) -> Tuple[bool, str]:
    """Check if a URL is accessible."""
    try:
        # Handle user agent to avoid 403 errors from some sites
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Link Checker)'}
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            status_code = response.getcode()
            if 200 <= status_code < 400:
                return True, f"OK ({status_code})"
            else:
                return False, f"Status {status_code}"
    except urllib.error.HTTPError as e:
        return False, f"HTTP Error {e.code}"
    except urllib.error.URLError as e:
        return False, f"URL Error: {str(e.reason)}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    files_to_check = [
        'README.md',
        'README_EN.md',
        'guide_clean.md'
    ]

    print("=" * 80)
    print("LINK CHECKER FOR DONTCLICKSHIT DOCUMENTATION")
    print("=" * 80)
    print()

    all_urls = {}

    # Extract URLs from all files
    for filename in files_to_check:
        try:
            urls = extract_urls_from_file(filename)
            all_urls[filename] = urls
            print(f"✓ Found {len(urls)} URLs in {filename}")
        except FileNotFoundError:
            print(f"✗ File not found: {filename}")
        except Exception as e:
            print(f"✗ Error reading {filename}: {e}")

    print()
    print("=" * 80)
    print("CHECKING LINKS...")
    print("=" * 80)
    print()

    # Track unique URLs and their results
    url_results = {}
    broken_links = defaultdict(list)

    # Check each unique URL only once
    for filename, urls in all_urls.items():
        for url, line_num in urls:
            if url not in url_results:
                print(f"Checking: {url[:70]}{'...' if len(url) > 70 else ''}", end=' ')
                sys.stdout.flush()
                is_ok, message = check_url(url)
                url_results[url] = (is_ok, message)

                if is_ok:
                    print("✓")
                else:
                    print(f"✗ {message}")

            # Track where this URL appears
            is_ok, message = url_results[url]
            if not is_ok:
                broken_links[url].append((filename, line_num, message))

    # Print summary
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()

    total_unique_urls = len(url_results)
    working_urls = sum(1 for is_ok, _ in url_results.values() if is_ok)
    broken_urls = total_unique_urls - working_urls

    print(f"Total unique URLs checked: {total_unique_urls}")
    print(f"Working URLs: {working_urls}")
    print(f"Broken URLs: {broken_urls}")
    print()

    if broken_links:
        print("=" * 80)
        print("BROKEN LINKS REPORT")
        print("=" * 80)
        print()

        for url, occurrences in sorted(broken_links.items()):
            print(f"✗ {url}")
            print(f"  Error: {occurrences[0][2]}")
            print(f"  Found in:")
            for filename, line_num, _ in occurrences:
                print(f"    - {filename}:{line_num}")
            print()
    else:
        print("✓ All links are working!")

    return 0 if not broken_links else 1

if __name__ == '__main__':
    sys.exit(main())
