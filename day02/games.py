score_shape = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

score_round = {
    "lost": 0,
    "draw": 3,
    "win": 6
}

part_two = {
    "X": {
        "A": 0+3, #elf plays rock, you play scissors
        "B": 0+1, #elf plays paper, you play rock
        "C": 0+2, #elf plays scissors, you play paper
    },
    "Y": {
        "A": 3+1, #both play rock
        "B": 3+2, #both play paper
        "C": 3+3, #both play scissors
    },
    "Z":{
        "A": 6+2, #elf plays rock, you play paper
        "B": 6+3, #elf plays paper, you play scissors
        "C": 6+1, #elf plays scissors, you play rock
    }
}

class RockPaperScissors:
    def __init__(self, data):
        self._data = data
        self.elf_plays = self._data[0]
        self.user_plays = self._data[-1]
        self._parse_match()


    def _parse_match(self):
        if self.user_plays == "X":
            match self.elf_plays:
                case "A":
                    self._outcome = "draw"
                case "B": 
                    self._outcome = "lost"
                case "C":
                    self._outcome = "win"
        elif self.user_plays == "Y":
            match self.elf_plays:
                case "A":
                    self._outcome = "win"
                case "B": 
                    self._outcome = "draw"
                case "C":
                    self._outcome = "lost"
        elif self.user_plays == "Z":
            match self.elf_plays:
                case "A":
                    self._outcome = "lost"
                case "B": 
                    self._outcome = "win"
                case "C":
                    self._outcome = "draw"

    @property
    def outcome(self):
        return self._outcome
    
    @property
    def score(self):
        return score_shape[self.user_plays] + score_round[self._outcome]