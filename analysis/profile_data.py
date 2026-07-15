import csv
from pathlib import Path
from collections import Counter
from statistics import median

p = Path('data/PS_20174392719_1491204439457_log.csv')
cols = [
    'step', 'type', 'amount', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig',
    'nameDest', 'oldbalanceDest', 'newbalanceDest', 'isFraud', 'isFlaggedFraud'
]
missing = Counter()
unique = {c: set() for c in cols}
cat_counts = {c: Counter() for c in ['type', 'isFraud', 'isFlaggedFraud']}
num_stats = {c: [] for c in ['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']}
rows = 0

with open(p, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows += 1
        for c in cols:
            v = row.get(c, '')
            if v == '' or v.lower() == 'nan':
                missing[c] += 1
            else:
                unique[c].add(v)
            if c in cat_counts:
                cat_counts[c][v] += 1
            if c in num_stats:
                try:
                    num_stats[c].append(float(v))
                except ValueError:
                    pass

print('rows', rows)
print('\nmissing values:')
for c in cols:
    print(f'  {c}: {missing[c]}')

print('\nunique counts:')
for c in cols:
    print(f'  {c}: {len(unique[c])}')

print('\ncategory counts:')
for c in ['type', 'isFraud', 'isFlaggedFraud']:
    print(f'  {c}: {cat_counts[c].most_common(10)}')

print('\nnumeric summaries:')
for c in ['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']:
    vals = num_stats[c]
    print(f'-- {c} --')
    print('  count', len(vals))
    if vals:
        print('  min', min(vals))
        print('  max', max(vals))
        print('  mean', sum(vals) / len(vals))
        print('  median', median(vals))
