# Contribution Guidelines

> **Before opening a pull request**, search the existing list to make sure your suggestion is not already included.
> Pull requests titled `Update README.md` will be closed without review — please use a descriptive title.

Thank you for helping make this the most useful RISC-V resource list on the internet. Every quality addition matters. 🙌

---

## ✅ What Belongs Here

This list targets **engineering students and researchers**. A resource is a good fit if it:

- Is **actively maintained** (significant commit activity in the last 12 months, or a stable release with clear long-term support).
- Is **openly accessible** — free to read, download, or use without a paywall.
- Is **directly relevant** to RISC-V architecture, implementation, tooling, or education.
- **Stands out** in some meaningful way: quality of documentation, community adoption, academic recognition, or unique capability.

---

## ❌ What Does NOT Belong Here

Please do not submit resources that:

- Return a 404 or are otherwise unreachable.
- Use plain `http://` — all links must use `https://`.
- Are personal blogs or unofficial tutorials of low quality.
- Duplicate something already on the list.
- Are paywalled commercial products with no free tier.
- Have been unmaintained for 2+ years with no active fork.

> **Archived resources** (dead links, outdated content) are tracked in
> [`Archived_list.txt`](Archived_list.txt) — do not re-add them to README.

---

## 📋 Pull Request Checklist

Before submitting, confirm **all** of the following:

- [ ] I searched the list and confirmed this is not a duplicate.
- [ ] The link opens correctly in a browser and uses `https://`.
- [ ] The resource has been active/maintained within the last 12 months.
- [ ] I am submitting **one resource per pull request**.
- [ ] My entry follows the format below exactly.
- [ ] I used **Title Case** for the resource name.
- [ ] My PR title is descriptive (e.g. `Add XiangShan to Open Source Cores`).
- [ ] The commit message body includes a link to the resource or repository.

---

## 📝 Entry Format

Follow the [sindresorhus/awesome](https://github.com/sindresorhus/awesome/blob/main/awesome.md) standard exactly:

```markdown
- [Resource Name](https://link-to-resource) - One sentence description starting with a capital letter, ending with a period.
```

**Rules:**
- Description is **mandatory** — entries without a description will be rejected.
- Description must start with a capital letter and end with a period.
- Keep descriptions to a single, informative sentence (aim for under 100 characters).
- Place your addition at the **bottom** of the most relevant section.
- If no existing section fits, propose a new one with a clear heading.

**Example:**
```markdown
- [NEORV32](https://github.com/stnolting/neorv32) - A small, customizable RISC-V soft-core CPU and SoC written in platform-independent VHDL.
```

---

## 🗂️ Sections at a Glance

| Section | What goes here |
|---|---|
| **Cores** | Open-source RISC-V CPU core RTL implementations |
| **SoCs** | Complete system-on-chip designs built around RISC-V cores |
| **Simulators/Emulators** | Tools for running or simulating RISC-V code without hardware |
| **Design Environment** | SoC design, build, and generation frameworks |
| **Verification & Testing** | Formal verification, coverage, and test tools |
| **Educational Boards** | Physical development boards for students |
| **Books** | Open-access textbooks and reference manuals |
| **Courses** | Free university courses or MOOC-style learning |
| **Articles** | Notable blog posts or technical write-ups |
| **Research Papers** | Peer-reviewed or workshop papers |
| **Videos** | Conference talks, tutorial series, lectures |
| **Social Media** | Forums, groups, and community channels |

---

## 💬 Questions?

Open an [issue](https://github.com/suryakantamangaraj/AwesomeRISC-VResources/issues) and tag it `question`. We're happy to help you find the right section for your contribution.
