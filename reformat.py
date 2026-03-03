import re
import urllib.parse
from collections import defaultdict
import os

with open('/Users/suryaraj/Desktop/git/AwesomeRISC-VResources/README.md', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

# The list must start with a # Awesome RISC-V Resources heading, followed by an awesome badge [![Awesome](https://awesome.re/badge.svg)](https://awesome.re).

output = []
# Ensure header
has_awesome_heading = False
for line in lines:
    if "Awesome RISC-V Resources" in line and not line.startswith("### "):
        has_awesome_heading = True
        break

def format_description(desc):
    desc = desc.strip()
    if not desc:
        return ""
    # Remove leading dashes or weird characters
    desc = re.sub(r'^[\-\s]+', '', desc)
    # Remove starting with uppercase words like 'A', 'An', or 'The'. (case insensitive but we'll focus on word boundaries)
    desc = re.sub(r'^(?i)(A|An|The)\s+', '', desc)
    if desc:
        desc = desc[0].upper() + desc[1:]
    if desc and not desc.endswith('.'):
        desc += '.'
    return " - " + desc if desc else ""

# parse categories and items
# Because there's a table of contents, we should keep the structure.
# But we need to alphabetize categories inside sections.
# Let's write a simple parser.

class ListEntry:
    def __init__(self, name, url, description, original_line):
        self.name = name
        self.url = url
        self.description = description
        self.original_line = original_line
    def __str__(self):
        desc_str = format_description(self.description)
        return f"- [{self.name}]({self.url}){desc_str}"

sections = []
current_section = {"type": "text", "lines": []}
sections.append(current_section)

i = 0
in_list = False
current_list = []
active_category = None

while i < len(lines):
    line = lines[i]
    m_list = re.match(r'^\s*-\s+\[(.*?)\]\((.*?)\)(.*?)$', line)
    if m_list and not line.strip().endswith('](#open-source-implementations)') and '#uncategorized' not in line.lower() and not line.startswith('  - ['):
        if current_section["type"] != "list":
            current_section = {"type": "list", "items": []}
            sections.append(current_section)
        
        name = m_list.group(1).strip()
        url = m_list.group(2).strip()
        desc = m_list.group(3).strip()
        current_section["items"].append(ListEntry(name, url, desc, line))
    else:
        if current_section["type"] != "text":
            current_section = {"type": "text", "lines": []}
            sections.append(current_section)
        current_section["lines"].append(line)
    i += 1

# rebuild with alphabetized lists
new_lines = []
for sec in sections:
    if sec["type"] == "text":
        new_lines.extend(sec["lines"])
    elif sec["type"] == "list":
        # alphabetize list
        # sorting by name (case-insensitive)
        sec["items"].sort(key=lambda x: x.name.lower())
        for item in sec["items"]:
            # special case for table of contents
            if item.url.startswith('#'):
                new_lines.append(item.original_line)
            else:
                new_lines.append(str(item))

# Replace top headers
final_lines = []

badge_added = False
for line in new_lines:
    if "</h1>" in line or "<h1" in line:
        continue # skip old html header
    if line.strip() == '<div align="center">' or line.strip() == '</div>':
        continue
    # remove old badge
    if 'awesome.re/badge.svg' in line:
        continue
    if 'A curated list of awesome RISC-V resources' in line:
        continue
    final_lines.append(line)

header = [
    "# Awesome RISC-V Resources",
    "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
    "\n",
    "A curated list of awesome RISC-V resources."
]

final_text = "\n".join(header) + "\n" + "\n".join(final_lines)

# Strip multiple blank lines
final_text = re.sub(r'\n{3,}', '\n\n', final_text)

# Also alphabetize categories inside main categories
# We can do this by splitting on `## ` and then alphabetizing `### ` sections inside them
# Let's do it with regex and split

blocks = re.split(r'\n(?=## )', final_text)
sorted_blocks = []
for block in blocks:
    if block.startswith('## '):
        # find subcategories
        sub_blocks = re.split(r'\n(?=### )', block)
        if len(sub_blocks) > 1:
            header_part = sub_blocks[0]
            subs = sub_blocks[1:]
            
            # sort subs by their title
            def get_sub_title(text):
                m = re.match(r'###\s+(.*)', text)
                return m.group(1).lower() if m else ""
            
            # extract content and sort
            subs_sorted = sorted(subs, key=get_sub_title)
            sorted_block = header_part + "\n" + "\n".join(subs_sorted)
            sorted_blocks.append(sorted_block)
        else:
            sorted_blocks.append(block)
    else:
        sorted_blocks.append(block)

# write the output
with open('/Users/suryaraj/Desktop/git/AwesomeRISC-VResources/README.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(sorted_blocks))

print("Reformatting complete.")
