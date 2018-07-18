# ex24.py : More Practice

print "Ayo berlatih lagi."
print 'Yang ini tidak di terjemahkan; You\'d need to know \'bout escape with \\that do \n newlines and \t tabs.'

poem = """
\tDunia tercinta
dengan logika yang tertaman kokoh
tidak bisa melihat \n kebutuhan cinta
tidak juga memahami hasrat intuisi
dan membutuhkan penjelasan
\n\tdimana itu tidak ada.
"""

print "--------------"
print poem
print "--------------"

lima = 10 - 2 + 3 - 6
print "Ini seharusnya lima: %s <-- benarkah?" % lima 

def rumus_rahasia(started):       #fungsi
    jelly_beans=started*500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates 

titik_mulai = 10000
beans, jars, crates = rumus_rahasia(titik_mulai)

print "Dengan titik awal: %d" % titik_mulai
print "Kita memiliki %d beans, %d jars, dan %d crates." % (beans,jars,crates)

titik_mulai = titik_mulai / 10

print "Kita bisa melakukannya dengan cara ini."
print "Kita memiliki %d beans, %d jars, dan %d crates." % rumus_rahasia(titik_mulai)

