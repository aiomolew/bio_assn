#! /usr/bin/env python3

import re

concert = "Katherine went to the concert to see Catheryn and the Cathryn's. She ran into her friend Kathryn, who introduced Katherine to her friend Catherine. Together they enjoyed the concert while texting inaudible snippets to their mutual friend, Kathrin. Their mercurial friend, katharine felt left out."
regex = re.finditer(r"[KCkc]ath[ae]?r[iy]ne?", concert)
column = ['match','start','end', 'length']
print(*column,sep='\t')
for match in regex:
    output = [match.group(), match.start(), match.end(), len(match.group())]
    print(*output,sep=' \t')
