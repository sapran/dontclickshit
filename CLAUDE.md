# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**"Don't Click Shit"** (Як не стати кібер-жертвою) is a comprehensive cybersecurity awareness guide for personal security, created by cybersecurity professionals. This is a **documentation-only project** with no code to build, test, or run.

## Project Structure

The repository contains three versions of the same guide:
- `README.md` - Primary Ukrainian version (most comprehensive)
- `README_EN.md` - English translation
- `guide_clean.md` - Markdown version without emojis for environments where emoji rendering is problematic

## Content Architecture

The guide covers 10+ major cybersecurity topics organized hierarchically:

1. **Don't Click Shit** - Core principle: avoiding suspicious files, links, pop-ups, and devices
2. **Password Management** - Passphrases, password managers (1Password, KeePass, Bitwarden), password recipes
3. **Multi-Factor Authentication** - Security keys, TOTP apps, backup codes
4. **Secure Messaging** - Signal, Threema, Wire recommendations
5. **VPN** - Algo, Outline, WireGuard, ZeroTier
6. **Encryption** - Full disk (FileVault, BitLocker, LUKS), cloud data (Cryptomator), communications (PGP)
7. **OS & Software Updates** - Platform-specific guidance for Windows/macOS/Linux
8. **Antivirus** - Platform-specific recommendations
9. **Firewall** - Configuration instructions per OS
10. **Data Backup** - Time Machine, Windows Backup, Linux tools
11. **Mobile Security** - iOS vs Android guidance
12. **Physical Security** - Device protection, travel security

## Development Workflow

### Version Control Only
```bash
git status                    # Check current changes
git log --oneline            # View commit history
git remote -v                # Verify remote: git@github.com:sapran/dontclickshit.git
```

### Making Changes
- Edit markdown files directly in `.md` format
- Maintain consistency across all three versions (Ukrainian, English, clean)
- Follow the existing hierarchical structure with table of contents
- Use emojis in README.md and README_EN.md for readability, but not in guide_clean.md

### Documentation Standards
- **Multi-language**: Update both Ukrainian (README.md) and English (README_EN.md) versions
- **Cross-platform**: Include guidance for Windows, macOS, and Linux where applicable
- **Tool links**: Provide direct links to recommended security tools
- **Practical examples**: Include specific commands, file types, configuration steps
- **Risk indicators**: Use :exclamation: for critical warnings

## Obsidian Integration

The project uses Obsidian for documentation management (`.obsidian/` directory contains workspace configuration). The guide is designed to work both as GitHub markdown and within Obsidian.

## XMind Mind Maps

Visual representations exist as companion resources:
- Ukrainian: http://www.xmind.net/m/DNRY
- English: http://www.xmind.net/m/raQ4

These should be updated if major structural changes occur to the guide.

## Contact & Contributions

- **Maintainer**: Vlad Styran (vlad@styran.com, https://blog.styran.com)
- **Organization**: BSG (https://bsg.tech)
- **Issues**: https://github.com/sapran/dontclickshit/issues/new
- **License**: Free to distribute, modify, and use commercially (attribution encouraged but not required)

## Important Notes

- This is purely educational/documentation content - no build system, tests, or executable code
- Changes should maintain the educational tone and practical focus
- All recommendations come from real-world cybersecurity experience
- The "Don't click shit" slogan is credited to Boris Sverdlik
