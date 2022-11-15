import re as regex
from collections import Counter, defaultdict

my_regex = regex.compile(f"[0-9]+{regex.I}")

lookup = defaultdict(int)
my_counter = Counter()
