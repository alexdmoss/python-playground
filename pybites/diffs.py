import difflib
from logger import log

first_list = [ "A value", "Another value", "The same value"]
second_list = [ "B value", "Some value", "The same value"]

log.info("-> Differ().compare ...")

for line in difflib.Differ().compare(first_list, second_list):
    print(line)

log.info("-> context_diff() (before/after) ...")

for line in difflib.context_diff(first_list, second_list):
    print(line)

log.info("-> unified_diff() (inline) ...")

for line in difflib.unified_diff(first_list, second_list):
    print(line)

log.info("-> ndiff() (every line) ...")

for line in difflib.ndiff(first_list, second_list):
    print(line)

log.info("-> get_close_matches() ...")

for line in difflib.get_close_matches("C value", second_list, cutoff=0.8):
    print(line)

log.info("-> HTML table ...")

print (difflib.HtmlDiff().make_table(first_list, second_list))

