import re as regex
from collections import defaultdict, Counter

my_regex = regex.compile(f"[0-9]+{regex.I}")

lookup = defaultdict(int)
my_counter = Counter()

