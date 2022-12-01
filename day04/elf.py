class Elf:

    def __init__(self, data):
        # print(data)
        self._raw_data = data
        self._range = self._calculate_range(data)
        # print(self.range)

    @property
    def range(self):
        return self._range

    def _calculate_range(self, data):
        lr = int(data.split("-")[0])    #lower range
        ur = int(data.split("-")[1])    # upper range

        # if ur <= lr:
            # print(f"Lower range < ur: lr:{lr} ur:{ur}") 
            # print(set(range(int(lr), int(ur)+1)))  
        return set(range(int(lr), int(ur)+1))

    def is_fully_contained(self, otherElf):
        return 1 if self.range.issubset(otherElf.range) or otherElf.range.issubset(self.range) else 0

    def intersection(self, otherElf):
        # print(self._raw_data)
        # print(f"own range: {self.range}, other range: {otherElf.range}. overlap: {set.intersection(self.range, otherElf.range)}")
        return set.intersection(self.range, otherElf.range)
