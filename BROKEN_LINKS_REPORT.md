# Broken Links Report for dontclickshit Documentation
**Generated:** 2025-12-24
**Checked files:** README.md, README_EN.md, guide_clean.md

## Executive Summary

This report identifies broken, discontinued, and problematic external links in the dontclickshit cybersecurity documentation. Out of approximately 120 unique URLs checked, **7 critical issues** were identified that require immediate attention.

## Critical Issues (Action Required)

### 1. VeraCrypt - Broken CodePlex Link ❌

**Current URL:** `https://veracrypt.codeplex.com`
**Status:** BROKEN (404 - CodePlex shut down by Microsoft)
**Found in:**
- README_EN.md:292
- guide_clean.md:259

**Recommendation:** Update to official VeraCrypt URL
- Primary: `https://veracrypt.fr/en/Home.html` (already used in README.md)
- Alternative: `https://veracrypt.io/`
- GitHub: `https://github.com/veracrypt/VeraCrypt`

**Note:** CodePlex was officially shut down by Microsoft. All references should point to the current official sites.

**Sources:**
- [VeraCrypt GitHub Issue #245](https://github.com/veracrypt/VeraCrypt/issues/245)
- [VeraCrypt Official Site](https://veracrypt.io/en/Release%20Notes.html)

---

### 2. Wickr Me - Discontinued Service ❌

**Current URL:** `https://wickr.com/`
**Status:** DISCONTINUED (Shutdown December 31, 2023)
**Found in:**
- README.md:161
- README_EN.md:311

**Recommendation:** REMOVE from secure messenger recommendations
- Service completely shut down for consumers
- Only enterprise version (AWS Wickr) remains, not suitable for personal use
- Consider replacing with alternative secure messengers already listed (Signal, Threema, Wire)

**Timeline:**
- June 2021: Acquired by AWS
- November 2022: Shutdown announced
- December 31, 2022: Stopped accepting new users
- December 31, 2023: Complete shutdown

**Sources:**
- [TechCrunch: Amazon-owned Wickr shutting down](https://techcrunch.com/2022/11/21/amazon-wickr-app-shutting-down/)
- [404 Media: Wickr Is Dead](https://www.404media.co/wickr-closed-down-is-dead/)

---

### 3. Flexera PSI - Discontinued Product ❌

**Current URL:** `http://www.flexerasoftware.com/enterprise/products/software-vulnerability-management/personal-software-inspector/`
**Status:** DISCONTINUED (Product ended April 20, 2018)
**Found in:**
- README_EN.md:174
- guide_clean.md:164

**Recommendation:** REMOVE and replace with modern alternatives
- Product has been discontinued for over 7 years
- Modern Windows has built-in update mechanisms
- Consider alternatives like:
  - Windows Package Manager (`winget upgrade --all`)
  - Chocolatey
  - Patch My PC (free version)

**Sources:**
- [Flexera Official Announcement: It's time to say goodbye to PSI](https://www.flexera.com/blog/security/its-time-to-say-goodbye-to-psi/)
- [BleepingComputer: Secunia PSI Being Discontinued](https://www.bleepingcomputer.com/news/security/secunia-personal-software-inspector-psi-being-discontinued-in-april/)

---

### 4. Ricochet IM - Discontinued Project ❌

**Current URLs:**
- `https://ricochet.im`
- `http://retroshare.net`

**Status:** DISCONTINUED (Original project ended 2016)
**Found in:**
- README_EN.md:315, 316
- guide_clean.md:282, 283

**Recommendation:** Update to successor project
- Original Ricochet ended development in November 2016
- Retired due to reliance on legacy Tor technology
- **Successor:** Ricochet Refresh at `https://www.ricochetrefresh.net/`
- Latest version: 3.0.38 (actively maintained)

**Note:** The original ricochet.im domain may still resolve but the software is outdated and insecure.

**Sources:**
- [Wikipedia: Ricochet software](https://en.wikipedia.org/wiki/Ricochet_(software))
- [GitHub Issue #579: Tor Project lists as discontinued](https://github.com/ricochet-im/ricochet/issues/579)
- [Ricochet Refresh Official Site](https://www.ricochetrefresh.net/)

---

### 5. That One Privacy Site - Changed Ownership ⚠️

**Current URL:** `https://thatoneprivacysite.net/#simple-vpn-comparison`
**Status:** COMPROMISED/REDIRECTED
**Found in:**
- README.md:181

**Issues:**
- SSL certificate expired (October 25, 2024)
- Site sold and now redirects to commercial affiliate content (Safetydetectives.com)
- No longer independent VPN comparison resource
- Comparison tables not updated since July 20, 2019

**Recommendation:** UPDATE or REMOVE
- Original creator's work may have moved to `thatoneprivacysite.xyz`
- Consider removing if independent VPN comparison is no longer available
- Alternative: Use more current VPN comparison resources

**Sources:**
- [GitHub OSINT-Framework Issue #21](https://github.com/lockfale/OSINT-Framework/issues/21)
- [MalwareTips Forum Discussion](https://malwaretips.com/threads/that-one-privacy-guy-is-a-sell-out.104990/)

---

## Medium Priority Issues

### 6. HTTP Links That Should Be HTTPS

The following links use HTTP but should be updated to HTTPS for security:

**README_EN.md & guide_clean.md:**
- `http://brew.sh` → `https://brew.sh`
  - Lines: README_EN.md:191, guide_clean.md:180

**README.md:**
- `http://getlinkinfo.com/` → Check if `https://getlinkinfo.com/` works
  - Lines: README.md:58
- `http://revealurl.com/` → Check if `https://revealurl.com/` works
  - Lines: README.md:61
- `http://checkshorturl.com/` → Appears in README_EN.md:60 as HTTP

**README_EN.md:**
- `http://www.expandurl.net/` → `https://www.expandurl.net/`
  - Lines: README_EN.md:61

### 7. Changed Domain - Objective-See

**Current URL:** `https://objective-see.com/products/lulu.html`
**Correct URL:** `https://objective-see.org/products/lulu.html`
**Found in:**
- README_EN.md:234

**Status:** The `.com` domain redirects to `.org`, but documentation should use the canonical domain.

**Recommendation:** Update to `.org` domain

**Sources:**
- [Objective-See Official LuLu Page](https://objective-see.org/products/lulu.html)
- [LuLu GitHub Repository](https://github.com/objective-see/LuLu)

---

### 8. WhisperSystems.org - Legacy Domain

**Current URL:** `https://whispersystems.org`
**Status:** LEGACY (Still works, redirects to Signal)
**Found in:**
- README_EN.md:308
- guide_clean.md:275

**Recommendation:** Consider updating to official Signal URL
- Current: `https://whispersystems.org`
- Updated: `https://signal.org/`
- The whispersystems.org domain still works and shows Signal content, but signal.org is the official current domain

**Note:** Low priority - domain is still functional and maintained

---

## Minor Issues & Notes

### Sites Blocking Automated Checkers (Not Actually Broken)

Many sites returned 403 Forbidden errors during automated checking but are actually accessible via web browsers:

- VirusTotal, Google services, Facebook, Twitter, Instagram, Apple, Microsoft
- Password managers (Dashlane, 1Password, Bitwarden, NordPass)
- 2FA hardware keys (YubiKey, Google Titan, etc.)
- VPN services and secure messengers

These sites implement bot protection and are **NOT** actually broken. Users can access them normally through web browsers.

### Inconsistent Link Formats

Some URLs appear with and without trailing slashes. While not broken, consistency would improve documentation quality:
- `https://twofactorauth.org` vs `https://twofactorauth.org/` (both used)

---

## Recommendations Summary

### Immediate Actions Required:

1. **Remove Wickr Me** from secure messenger recommendations (service shut down)
2. **Remove Flexera PSI** from Windows update recommendations (discontinued 2018)
3. **Update VeraCrypt link** in README_EN.md and guide_clean.md from codeplex.com to veracrypt.fr or veracrypt.io
4. **Update or remove Ricochet IM** - replace with Ricochet Refresh if still recommending
5. **Review thatoneprivacysite.net link** - update or remove due to changed ownership

### Medium Priority:

6. **Update HTTP to HTTPS** for Homebrew (brew.sh) and other links
7. **Update objective-see.com to objective-see.org** for LuLu firewall
8. **Consider updating whispersystems.org to signal.org** for consistency

---

## Testing Methodology

Links were checked using:
1. Automated Python script with urllib
2. Manual verification via WebFetch tool
3. Web searches for discontinued services and URL changes
4. Cross-referencing with official documentation and community sources

**Note:** Many 403 Forbidden errors during automated checking were false positives from bot protection. Critical findings were verified through web research and official sources.

---

## Files Requiring Updates

### README.md (Ukrainian - Primary)
- Line 161: Remove Wickr Me
- Line 164: Review thatoneprivacysite.net
- Lines 58, 61: Consider HTTPS updates for URL shortener checkers

### README_EN.md (English)
- Line 174: Remove Flexera PSI reference
- Line 191: Update http://brew.sh to https://brew.sh
- Line 234: Update objective-see.com to objective-see.org
- Line 292: Update veracrypt.codeplex.com to veracrypt.fr
- Lines 308, 315, 316: Review WhisperSystems.org and Ricochet IM
- Line 311: Remove Wickr Me reference

### guide_clean.md (Ukrainian - Legacy)
- Line 164: Remove Flexera PSI reference
- Line 180: Update http://brew.sh to https://brew.sh
- Line 259: Update veracrypt.codeplex.com to veracrypt.fr
- Lines 275, 282, 283: Review WhisperSystems.org and Ricochet IM

---

## Conclusion

While most links in the documentation are still valid, several critical services have been discontinued or moved since the documentation was last comprehensively updated. The 7 issues identified above should be addressed to maintain the accuracy and trustworthiness of this important cybersecurity guide.

**Priority:** HIGH - Broken links to discontinued services can confuse users and undermine trust in the documentation.

---

**Report generated by:** Claude Code Link Checker
**Date:** 2025-12-24
**Total URLs checked:** ~120 unique URLs
**Critical issues found:** 7
**Estimated fix time:** 30-45 minutes
