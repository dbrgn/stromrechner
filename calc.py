import sys

HOCHTARIF_H = 13 * 5 + 6
NIEDERTARIF_H = 7 * 24 - HOCHTARIF_H

HOCHTARIF_CHF = 0.2447
NIEDERTARIF_CHF = 0.1432

if len(sys.argv) != 2:
    print('Usage: %s <watt>' % sys.argv[0])
    sys.exit(1)

watt = int(sys.argv[1])
niedertarif = NIEDERTARIF_H * watt / 1000 * NIEDERTARIF_CHF
hochtarif = HOCHTARIF_H * watt / 1000 * HOCHTARIF_CHF

print('Total cost per week: %.02f CHF' % (niedertarif + hochtarif))
print('Total cost per 30 day month: ~%.02f CHF' % ((niedertarif + hochtarif) / 7 * 30))
print('Total cost per year: ~%.02f CHF' % ((niedertarif + hochtarif) * 52))
