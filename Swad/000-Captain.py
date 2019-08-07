"""
000
"""

import glob
files= glob.glob("*.py")
medt= 90
easyt= 50
hardt= 30

ctrm= 0
ctre= 0
ctrh= 0
tot= 0
for f in files:
    parts= f.split("-")
    if len(parts)<4: continue
    lev= parts[3].lower()
    if "med" in lev: ctrm+=1
    elif "eas" in lev: ctre+=1
    if "har" in lev: ctrh+=1
print "Done   : ", ctre, ctrm, ctrh
print "Pending: ", easyt-ctre, medt-ctrm, hardt-ctrh
