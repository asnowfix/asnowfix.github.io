# Maintaining github.asnowfix.fr

Static site (plain HTML, Bootstrap/AOS/Font Awesome from CDNs, no build step), published by GitHub Pages from `main`. `CNAME` = `github.asnowfix.fr`; `asnowfix.github.io` redirects to it. Keep the existing design and add no dependencies. Content changes, not look.

## Source of truth (Google Drive, folder "CV & Resumes", id `1YT6XQrELb_NWLh3OUjQucTXlvTe9G_1m`)

| What | Drive file | ID |
|---|---|---|
| Update spec (positioning strings, confidentiality rules, checklist) | `Website update spec - github.asnowfix.fr.md` | `1lQJkBTci04cHY18KwsYS36yQsacXxpnK` |
| Resume, private master | `Resume - FiX Kowalski - AI & IAM Architect` (Google Doc) | `1jvoGHWYZ34xh8wOBp6XlLk65uDdfy0oUQcW6-Y6Oq4c` |
| Detailed CV, private master | `CV Francois-Xavier Kowalski` (Google Doc) | `1Yx1vJQ6dFPP8rFvq1xNHz3knnfJjXSERJ7UvhNThP3U` |
| Resume, web-safe copy (PDF source) | `Web - Resume - FiX Kowalski - Senior Architect` | `1_0sELi_gMEP4b8MTyH8b00-RJCx3J8FhkVZukgriwS0` |
| Detailed CV, web-safe copy (PDF source) | `Web - Detailed CV - FiX Kowalski` | `1RDlBU0ZIBOA8aYn5KkT4lc1cXwaPt_LpOMZNaEplLmM` |

Read the spec from Drive at the start of every site update (`read_file_content`): it may have changed.

The private masters contain a street address, phone number, birth date, family status, manager names and internal Amadeus details. **Never export a PDF from a private master.** PDFs on the site come only from the `Web - ...` copies.

## Published assets

- `assets/FiX-Kowalski-Resume.pdf` is exported from the web-safe resume copy.
- `assets/FiX-Kowalski-Detailed-CV.pdf` is exported from the web-safe detailed CV copy.
- Both are linked from the Contact section of `index.html`. Keep the file names stable so links and bookmarks do not break.

## Refreshing the PDFs (every time the site is updated)

1. Read the private master and the web-safe copy for both documents (`read_file_content` with `includeComments: true`). Compare modified times with `get_file_metadata`.
2. If a private master changed since the copy was made, re-apply those changes to the web-safe copy, with the redactions below. Edit the copy in place with `update_doc` and `replaceAllText` so its link and Drive ID stay the same. If the copy is badly out of date, make a fresh `copy_file` of the master into the same folder, redact it, then update the IDs in this file.
3. Redactions to apply on every refresh (also required by the spec):
   - Remove the street address, phone number, birth date, marital status and children (the private masters have them). Keep only "French Riviera, France", email, LinkedIn, GitHub and the site URL.
   - Remove manager names (regex `\s?\((?:Mgr|Manager): [^)]*\)`).
   - Do not name the internal agentic framework (the spec gives its name) and do not say it was selected as a company standard. Call it "enterprise agentic AI framework".
   - Do not describe how Amadeus DNS defends against data exfiltration, or any other internal security design. Do not use the internal workstream acronym; say "company-wide architecture workstream on agentic security".
   - Self-Healing Platform: approach only. No internal system names, incident data or customer names.
   - Amadeus start date is **November 2019** everywhere (confirmed by FiX on 2026-11-27). HP Inc. ends October 2019.
   - Titles must match the site positioning: "Senior Architect", never "System Software Architect" or "Device & Cloud".
4. Read both web copies back (`read_file_content`) and check there is no street address, phone number, birth date, internal framework name, "standard" claim, DNS-defence detail, workstream acronym or manager name. The master docs show what to look for. This repo is public: never write those private strings into it, not even in this file or in scripts.
5. Export each copy with `download_file_content` and `exportMimeType: "application/pdf"`. The result is saved to a local file under the session's `tool-results` folder; copy it over the matching file in `assets/`. Use `file` to confirm it is a PDF and check the page count (resume about 2 pages, detailed CV about 6).
6. Tell FiX which source docs changed and that the PDFs were regenerated.

## Updating the site

1. Work on a branch in this repo, never on `main`. Keep the main worktree on `main` (see the user-level worktree rule).
2. Apply the spec's positioning strings verbatim: tagline, `<title>`, meta description and `og:description`. Keep `<link rel="canonical">` and `og:url` pointing at `https://github.asnowfix.fr/`.
3. Keep experience entries short (about three lines on desktop). One Amadeus entry, "Nov 2019 - Present".
4. Patent links: US 9,723,052 -> `https://patents.google.com/patent/US9723052B2/en`, US 8,819,698 -> `https://patents.google.com/patent/US8819698B2/en`. EPO register links return 403 to scripts, so check them by hand.
5. Footer year is set by `script.js`; the HTML fallback must match the current year.
6. Run `python3 -I scripts/check_site.py` before every commit. It fails on forbidden strings and missing assets.
7. Do not add an empty "Writing" or "Blog" section. Add one only with the first article.

## Testing

- Preview in Chrome with the Claude-in-Chrome tools (start Claude Code with `--chrome`). With several browsers connected, ask FiX which one to use and call `select_browser`.
- The browser window cannot be resized below about 500px. To check phone width, load the live page in a 390px-wide `iframe` from `javascript_tool`, then measure `scrollWidth` against `clientWidth` after the AOS animations settle (about 1 second).
- Headless Chrome screenshots miss AOS-hidden sections; do not rely on them.
- After merge, GitHub Pages takes a minute or two; confirm with `curl -s https://github.asnowfix.fr | grep -o '<title>[^<]*</title>'`.

## Git and PRs

- `git push` fails here because the git credential helper points at `/usr/local/bin/gh`, but `gh` is at `/opt/local/bin/gh`. Push with: `git -c 'credential.helper=!/opt/local/bin/gh auth git-credential' push -u origin <branch>`. Do not edit the global git config.
- Open PRs with `gh pr create`. Merge with a merge commit (`gh pr merge <n> --merge`), never squash or rebase. No `Co-Authored-By` trailers and no "Generated with Claude Code" lines.
- After a merge: `git checkout main`, pull with the same credential override, and delete the local branch.
