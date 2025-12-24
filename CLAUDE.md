# CLAUDE.md - AI Assistant Guide for dontclickshit Repository

## Repository Overview

**Repository Name**: dontclickshit
**Primary Language**: Ukrainian (with English translation)
**Type**: Documentation-only cybersecurity guide
**Author**: Vlad Styran (vlad@styran.com)
**Organization**: Berezha Security / BSG
**License**: Free to use, distribute, and modify
**Permanent URL**: https://github.com/sapran/dontclickshit/

### Purpose

This repository contains a comprehensive personal cybersecurity guide aimed at helping regular users protect themselves from cyber threats. The guide's tagline "Don't click shit" (Ukrainian: "Не натискайте каку") emphasizes the fundamental principle of not opening, clicking, or running suspicious files, links, and programs.

The guide is created by cybersecurity professionals with extensive experience in development, analysis, and ethical hacking of computer systems and networks. It provides practical, actionable advice for personal cybersecurity.

## Repository Structure

```
dontclickshit/
├── README.md           # Main Ukrainian version (most comprehensive and up-to-date)
├── README_EN.md        # English translation
├── guide_clean.md      # Clean Ukrainian version (legacy/alternative format)
└── CLAUDE.md           # This file - AI assistant guide
```

### File Descriptions

1. **README.md** (Ukrainian)
   - The primary, authoritative version of the guide
   - Most comprehensive and frequently updated
   - Contains the latest recommendations and tools
   - ~416 lines of content
   - Should be the reference for any updates

2. **README_EN.md** (English)
   - English translation of the guide
   - May lag slightly behind Ukrainian version
   - ~380 lines of content
   - Should be synchronized when Ukrainian version is updated

3. **guide_clean.md** (Ukrainian)
   - Alternative/legacy version in Ukrainian
   - ~337 lines of content
   - Purpose unclear - may be for specific distribution channels
   - Should be kept synchronized with README.md

## Content Structure

The guide is organized into the following main sections:

1. **Don't Click Shit** - Core principle about avoiding suspicious content
   - Suspicious files
   - Suspicious links
   - Pop-up windows
   - Suspicious devices

2. **Password Management** - Use of password managers and passphrases
   - Password managers (Dashlane, 1Password, Bitwarden, NordPass)
   - Creating strong passphrases
   - Password security best practices

3. **Two-Factor Authentication (2FA)** - Multi-factor authentication setup
   - Enable 2FA on all services
   - Hardware keys (YubiKey, Google Titan, etc.)
   - Authenticator apps
   - Avoid SMS-based 2FA

4. **Secure Messengers** - End-to-end encrypted communication
   - Signal, Threema, Wickr Me, Wire
   - Comparison resources

5. **VPN Usage** - Virtual Private Networks for traffic protection
   - Self-hosted VPN (Algo, Outline, WireGuard, ZeroTier)
   - VPN services comparison

6. **Data Encryption** - Protecting sensitive data
   - HTTPS verification
   - Cloud data encryption (Boxcryptor, Cryptomator, VeraCrypt)
   - Full disk encryption (FileVault, LUKS, BitLocker)

7. **Operating System and Software** - Keeping systems updated
   - Windows, macOS, Linux update procedures
   - Avoiding pirated software
   - Running with least privileges

8. **Antivirus** - Platform-specific recommendations
   - macOS/Linux: Optional (Malwarebytes, BitDefender)
   - Windows: Required (Microsoft Defender)

9. **Firewall** - Network protection
   - macOS, Windows, Linux firewall setup
   - Advanced tools (Little Snitch, LuLu)

10. **Backups** - Data backup strategies
    - Time Machine (macOS)
    - Windows Backup
    - Linux tools (tar, rsync)

11. **Mobile Security** - Smartphone protection
    - Prefer iOS over Android
    - If Android, use Google devices
    - Avoid rooting devices

12. **Physical Security** - Device protection
    - Keep devices in sight
    - Separate devices for sensitive operations
    - Border crossing considerations

## Content Conventions

### Language and Tone

- **Primary audience**: Ukrainian-speaking general users
- **Tone**: Professional but accessible, avoiding excessive technical jargon
- **Style**: Direct, practical, actionable advice
- **Emojis**: Used strategically for emphasis:
  - 💡 (bulb) for tips and examples
  - ❗ (exclamation) for warnings and critical information
  - 🔧 (wrench) for tools and resources
  - :email: or ✉️ for email addresses

### Formatting Standards

1. **Headings**: Use proper Markdown hierarchy (##, ###, ####)
2. **Lists**: Use `-` for unordered lists, numbered lists for steps
3. **Code**: Use backticks for:
   - File extensions (e.g., `EXE`, `PDF`, `ZIP`)
   - Technical terms (e.g., `HTTPS`, `LUKS`, `BitLocker`)
   - Application names (e.g., `FileVault`, `Google Authenticator`)
   - Command examples (use fenced code blocks for multi-line)
4. **Links**: Use descriptive text with inline URLs or reference-style links
5. **Bold**: Use for emphasis on critical warnings and key concepts
6. **Table of Contents**: Maintain at the top with anchor links

### Tool and Service References

When referencing tools or services:
- Provide the tool name with link
- Include both free and commercial options where applicable
- Prefer open-source solutions when available
- Keep links up-to-date and verify they work
- Use official URLs, not shortened links

Example format:
```markdown
🔧 Tool Name: https://example.com
```

### Code Examples

For terminal commands:
```markdown
```bash
apt update && apt -y upgrade
```
```

## Development Workflows

### Making Content Updates

1. **Priority**: Always update README.md (Ukrainian) first
2. **Synchronization**: Update corresponding sections in:
   - README_EN.md (English translation)
   - guide_clean.md (if applicable)
3. **Verification**: Check all links still work
4. **Testing**: Verify Markdown rendering (especially anchors in TOC)

### Adding New Tools or Services

When adding new tool recommendations:
1. Verify the tool is reputable and actively maintained
2. Include official website URL
3. Categorize appropriately (free/paid, open-source/commercial)
4. Add to all language versions
5. Update relevant sections in table of contents

### Updating Security Recommendations

Security landscape changes frequently:
1. Review tool recommendations annually
2. Remove deprecated tools/services
3. Add emerging threats and solutions
4. Update version-specific instructions (OS versions, etc.)
5. Verify security best practices are still current

### Link Management

Critical for maintaining guide utility:
1. Verify all external links are functional
2. Update broken links promptly
3. Archive important pages if concerned about link rot
4. Prefer official documentation over third-party guides
5. Check for HTTPS availability

## Git Workflow

### Branch Strategy

- **Main branch**: Contains production-ready documentation
- **Feature branches**: Use format `claude/description-XXXXX` for AI-assisted changes
- **Commit messages**: Clear, descriptive (see existing pattern in history)

### Commit Best Practices

Based on repository history:
- Keep commits focused on specific updates
- Use descriptive commit messages (e.g., "Update README.md")
- For substantial changes, provide details in commit body
- Commit after completing a logical section update

### Creating Pull Requests

When ready to merge changes:
1. Ensure all language versions are synchronized
2. Verify all links work
3. Check Markdown formatting
4. Test table of contents links
5. Review for typos and grammatical errors
6. Create PR with clear description of changes

## Key Conventions for AI Assistants

### When Updating Content

1. **Preserve Structure**: Maintain existing section hierarchy
2. **Maintain Bilingual Parity**: Update both Ukrainian and English versions
3. **Keep Formatting Consistent**: Follow existing emoji and formatting patterns
4. **Verify Technical Accuracy**: Ensure security recommendations are current
5. **Preserve Author Attribution**: Don't modify credits section
6. **Maintain License Terms**: Keep "free to use/distribute" language

### When Adding New Sections

1. Add to table of contents in all versions
2. Use appropriate heading level
3. Follow existing emoji conventions
4. Include practical examples where helpful
5. Provide tool recommendations with links
6. Consider both beginner and advanced users

### When Removing Outdated Content

1. Don't just delete - consider replacing with updated alternative
2. Update table of contents
3. Check for broken internal references
4. Document reason for removal in commit message

### Translation Guidelines

When translating or updating translations:
1. Maintain equivalent meaning, not literal translation
2. Adapt examples to be culturally appropriate
3. Use correct technical terminology for each language
4. Keep URLs and tool names unchanged
5. Preserve emoji usage across versions

## Common Tasks

### Updating a Security Tool Recommendation

```markdown
Old:
🔧 OldTool: https://oldtool.com

New:
🔧 NewTool: https://newtool.com
🔧 BetterTool: https://bettertool.com
```

Update in:
1. README.md (Ukrainian) - find and update
2. README_EN.md (English) - find and update
3. guide_clean.md (Ukrainian) - if present, update

### Adding a New Section

1. Determine appropriate placement in hierarchy
2. Add section heading with proper level
3. Write content following existing patterns
4. Add to table of contents with anchor link
5. Repeat for all language versions
6. Commit with descriptive message

### Fixing Broken Links

1. Identify broken link
2. Search for current/alternative URL
3. Update in all files where link appears
4. Verify new link works
5. Commit with message like "Fix broken link for [Tool Name]"

## Quality Checklist

Before committing changes:

- [ ] All language versions updated consistently
- [ ] Table of contents reflects structure accurately
- [ ] All internal anchor links work
- [ ] All external links verified functional
- [ ] Markdown formatting correct
- [ ] Emoji usage consistent
- [ ] Technical accuracy verified
- [ ] No typos or grammatical errors
- [ ] Author/credits section unchanged
- [ ] Commit message is descriptive

## Important Notes

1. **No Code**: This is a documentation-only repository. Do not add code, scripts, or executables.

2. **Security Focus**: All recommendations should prioritize user security and privacy.

3. **Accessibility**: Keep language accessible to non-technical users while remaining technically accurate.

4. **Neutrality**: Avoid promoting specific commercial products without justification based on security merit.

5. **Currency**: Security recommendations must be current. Flag outdated information for review.

6. **Bilingual Maintenance**: Never update only one language version. Always synchronize.

7. **Attribution**: Respect author's contribution and maintain proper attribution.

8. **Contact Information**: Current contact is vlad@styran.com, with historical contact sapran@protonmail.com mentioned in some versions.

## Reference Information

### External Resources Mentioned

- VirusTotal: https://virustotal.com
- Have I Been Pwned: https://haveibeenpwned.com
- Two Factor Auth Directory: https://twofactorauth.org
- Secure Messaging Apps Comparison: https://www.securemessagingapps.com

### Key Personalities

- **Vlad Styran**: Primary author and compiler (vlad@styran.com)
- **Boris "jadedsecurity" Sverdlik**: Credited for inspiration and coining the "Don't click shit" slogan
- **Contributors**: Multiple security professionals in Ukraine and abroad

### Organizations

- **BSG / Berezha Security**: https://bsg.tech / https://berezhasecurity.com
- **Vlad Styran's Blog**: https://styran.com / https://blog.styran.com

## Maintenance Schedule Recommendations

### Regular Updates (Quarterly)
- Review and update tool recommendations
- Verify all external links
- Check for new security threats to address
- Update OS version-specific instructions

### Annual Updates
- Comprehensive security review
- Major revision of all recommendations
- Review and update statistics/examples
- Refresh deprecated content

### As Needed
- Breaking security news (major vulnerabilities)
- Tool sunset/discontinuation
- Significant methodology changes
- Community feedback incorporation

## Getting Help

If unclear about updates or changes:
1. Review existing issues at: https://github.com/sapran/dontclickshit/issues
2. Contact repository owner: vlad@styran.com
3. Create new issue for discussion
4. Review commit history for precedent

---

**Last Updated**: 2025-12-24
**Document Version**: 1.0
**Maintained by**: AI Assistant following repository conventions
