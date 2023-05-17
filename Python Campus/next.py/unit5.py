import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }

notes = "250-sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"




notes = notes.split(",")

print(type(notes))

for note in notes:
    notes_obj = iter(notes)
    while True:
        try:
            note = next(notes_obj)
            note = note.split("-")
            winsound.Beep(int(note[0]),int(freqs.get(note[1])))
        except StopIteration:
            break







