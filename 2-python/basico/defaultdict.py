# coding=utf-8
from collections import Counter
from collections import defaultdict

document = """Most dirty bashful scarce astonishing bent sweet juicy muscular coat. Beefy bent brainy adorable yummy 
twilight. Damaged annoyed brown chubby shallow acrid kind narrow refined wall. Quaint bored important boundless 
rancid grumpy denmark. Yellow damp scarce clean bewildered ugly lion. Rapping quick polite eager many wrong billions 
soccer. Great clumsy orange bright abrasive ashamed animal. Future microscopic alive kind harsh bright mushy crowd. 
Mushy echoing bald harsh flat optician. Lemon freezing few bright itchy modern wide slimy bear. Fierce loose 
shrilling wrong clumsy daybreak. Blue clean mammoth tiny jealous straight easy broad blushing cricket. Hallowed late 
shallow damp vast fierce massive mechanic. Odd quiet slimy easy able unsightly witty scooter. Massive appalling brash 
few shrilling red plumber. Tiny gray elegant green witty moldy camera. Burly ugly muscular limited uptight clumsy 
nail. Apprehensive boring tasty appetizing miniature refined air. Muscular millions loud dead silly morn. Short 
sticky glamorous crooked curved orange london. Better quick limited jealous raspy vr. Proud belligerent grumpy clumsy 
white scientist. Jealous crashing ugly ugly jealous thundering flat petabyte. Adorable screeching red absurd yellow 
melodic oxygen. Bumpy ugly nutritious sweet witty author. Low colossal astonishing strong silly sharp low aggressive 
boots. Famous jealous defeated many embarrassed grumpy full beautiful lion. High acceptable black nice echoing 
arrogant brash leather. Adventurous brown raspy tender noisy crooked prehistoric famous appetizing window. Bald black 
sweet green angry putrid lizard. Scruffy fluffy careful breezy abrasive salty chilly abrasive church. Great rich 
proud wonderful absurd clumsy savory brash enough breakfast. Easy wailing vast nice rapid bashful petite late 
xylophone. Enough handsome substantial immense putrid gray abandoned hospital. Modern incalculable shallow abandoned 
abandoned absurd wailing eager disease. Panicky scrawny howling zealous appalling teeny bright calm deafening 
printer. Prehistoric vast callous flaky howling plain receptionist. High tasty refined beefy rhythmic army. Important 
shy belligerent important pitiful rapping powerful shrilling boy. Stocky blushing kind glamorous alive alligator. 
Belligerent millions large brash best rough happy slimy rotten church. Quaint abiding bright skinny clever aggressive 
byte. Happy itchy sparse alive salmon purring boy. Kind colossal wailing microscopic callous mother. Petite dead 
future early dazzling quaint unimportant mealy vast grass. Flat bland teeny cagey shrilling boring broken howling 
oxygen. Ancient prehistoric repulsive lively witty whining abnormal stale bed. Blushing full boundless round bitter 
puny aloof odd odd elephant. Blushing round juicy gifted substantial unkempt millions salesclerk. Whining sparse 
uninterested blue acrid able muscular tiny loud cat. Fluffy squeaking weak immense muscular gigabyte. Panicky late 
fresh sharp rapid bulky spicy kind fresh argument. Eager putrid limited late wrong plain handsome action. Straight 
mango spicy tender mealy aggressive rancid panicky scooter. Flabby limited shrilling thousands bitter fresh plump 
jewellery. Many flabby mushy faithful victorious thankful millions brief raincoat. Gorgeous savory putrid damp 
delicious famous anxious angry memory. Itchy annoyed adorable tasteless wooden lively aloof tight noon. Silly tangy 
rough squeaking adorable waitress. Creamy obnoxious delightful nutritious whispering prickly disgusting truck. Aloof 
damp straight red damaged incalculable able shampoo. Busy wonderful tiny important plain tent. Little drab antsy 
black broad kind island. Warm polite appetizing abandoned gifted busy baby. Bashful gorgeous substantial salmon odd 
ripe uneven salmon oxygen. Annoyed acidic apprehensive tinkling fat whining agreeable hydrogen. Wrong mammoth 
important kind rough shallow raincoat. Scruffy unkempt wonderful round gorgeous red screeching dirty cagey car. Brown 
screeching careful burly broken quaint salty fast address. Dirty noisy rotten slimy shaggy dirty limited wrong 
pharmacist. Large white refined unkempt mushy sticky weak fancy fast kangaroo. High elegant young microscopic cuddly 
appalling early tight helicopter. Polite annoyed square green ashamed rich busy harsh tender cat. Victorious young 
repulsive faint ripe wire. Average cagey happy unsightly putrid zealous eggplant. Massive inexpensive scarce echoing 
huge clumsy state. Poor shrilling low sweet appetizing agreeable careful appetizing puny spoon. Attractive purple 
faithful quick clever sweden. Full icy uninterested strong worried gas. Bitter clean flat harsh ashamed belgium. Loud 
belligerent black limited bashful russia. Damaged rough rhythmic skinny wet faithful russia. Magnificent creamy beefy 
deep abrasive leather. Better hallowed mysterious breezy bright putrid uneven family. Large acidic tinkling abandoned 
shapely petabyte. Glamorous obedient shy ambitious little sour deep salty jewellery. Tasty absurd annoyed appalling 
important lively quiet warm billowy hydrogen. Adorable clean abiding wonderful plump abundant broken lazy airplane. 
Full wide late sticky yellow modern chubby numerous flabby rain. Acceptable limited billowy grumpy kind purring 
substantial greasy girl. Thankful ripe billowy gorgeous full small ashamed powerful inexpensive nail. Brief uneven 
putrid long nutritious sour dirty whining average bed. Thoughtless belligerent dirty cagey abundant sharp black few 
monitor. Quaint yummy tasty screeching millions some winter. Absurd tasty flaky melodic high orange. Sticky hissing 
hollow large quaint fierce arrogant stale round cpu. Acoustic adorable abrasive old breezy flat thundering thankful 
famous river. Wailing stocky mysterious abrasive nutritious happy skinny market. Best gray glamorous obedient 
faithful abandoned tender australia. Purring deep tiny some cuddly embarrassed tinkling tasteless thundering baby """

word_counts = {}
for word in document.split():
    word = word.lower().strip(".").strip(",")
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

word_counts = {}
for word in document.split():
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 0

word_counts = {}
for word in document.split():
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

word_counts = defaultdict(int)  # int() produz 0
for word in document.split():
    word_counts[word] += 1

dd_list = defaultdict(list)  # list() produz uma lista vazia
dd_list[2].append(1)  # agora 'dd_list' contém {2: [1]}

dd_dict = defaultdict(dict)  # dict() produz um dicionário vazio
dd_dict["Joel"]["City"] = "Seattle"  # {"Joel": {"City": "Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1  # agora 'dd_pair' contém {2: [0, 1]}

# Contador

c = Counter([0, 1, 2, 0])  # 'c' é (basicamente) {0: 2, 1: 1, 2: 1}

word_counts = Counter(word.strip(".").lower() for word in document.split())
letter_counts = Counter(word.strip(".").lower() for word in document)

# imprime às dez palavras mais comuns e suas contas
for word, count in word_counts.most_common(10):
    print(f"'{word}' appeared {count} times.")
print()
# imprime às dez letras mais comuns e suas contas
for letter, count in letter_counts.most_common(10):
    print(f"'{letter}' appeared {count} times.")
