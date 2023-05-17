class MusicNotes:
    def __init__(self):
        self._notes = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self._note_Index = -1
        self._octIndex = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self._octIndex == 4 and self._note_Index == len(self._notes) - 1 :
           raise StopIteration
        self._note_Index += 1
        if self._note_Index == len(self._notes):
            self._note_Index = 0
            self._octIndex += 1

        return self._notes[self._note_Index] * (2 ** self._octIndex)


notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)
