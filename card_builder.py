header = (r"\documentclass[10pt]{report}"
          r"\setlength{\paperwidth}{200pt}"
          r"\usepackage[paperheight=60mm,paperwidth=40mm,margin=0.5mm,heightrounded,showframe]{geometry}"
          r"\usepackage{mathptmx}"
          r"\usepackage{anyfontsize}"
          r"\usepackage{t1enc}"
          r"\begin{document}")

document = (r"\noindent ")

footer = (r"\end{document}")

knacks_on_line = 0
items_on_line = 0

def small_header(header_text):
  return r"{\fontsize{9}{11}\selectfont "+header_text+r"\\}"

def knack(name, level):
  global knacks_on_line
  if knacks_on_line == 0:
    line = ""
  else:
    line = "\t"
  line += name+": "+str(level)
  knacks_on_line += 1
  if knacks_on_line == 2:
    line += r"\\"
    knacks_on_line = 0
    line += "\n"
  return line

def attack_line(name, hit, damage):
  return name+r"\\"+hit+r"\\"+damage

def item_entry(name):
  global items_on_line
  if items_on_line == 0:
    line = ""
  else:
    line = "\t"
  line += name
  items_on_line += 1
  if items_on_line == 2:
    line += r"\\"
    items_on_line = 0
    line += "\n"
  return line

from latex import build_pdf

document += small_header("Knacks")
document += knack("Forestry", 7)
document += knack("Yo Mama", 3)
document += knack("Farting", 8)
document += knack("Puns", 11)
document += knack("Cosplay", 8)
document += r"\\"
document += small_header(r"\\Attacks")
document += attack_line("Punch:", "Agility|Melee vs Agility|Dodge", "Body:Power vs Body|Armor")
document += r"\\"
document += small_header(r"\\Gear")
document += item_entry("Nothing")
document += item_entry("More Nothing")
document += item_entry("No Tea")

doc = header+document+footer
print(doc)
pdf = build_pdf(doc)
pdf.save_to("foo.pdf")