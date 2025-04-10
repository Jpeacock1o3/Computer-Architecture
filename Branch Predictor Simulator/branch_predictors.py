# Branch Predictor Implementations

# Static Predictor
class StaticPredictor:
    def __init__(self, always_taken=True):
        """
        Initialize the Static Predictor.
        :param always_taken: If True, always predict "Taken" (1); otherwise, always predict "Not Taken" (0).
        """
        self.prediction = 1 if always_taken else 0

    def predict(self, address):
        return self.prediction

    def update(self, address, actual_outcome):
        pass


# One-Bit Branch Predictor
class OneBitBranchPredictor:
    def __init__(self):
        # Initialize a Branch History Table (BHT) to store one-bit history for each branch address.
        self.bht = {}

    def predict(self, address):
        return self.bht.get(address, 0)  # Default to "Not Taken" if address is not in BHT.

    def update(self, address, actual_outcome):
        self.bht[address] = actual_outcome  # Update BHT with the actual outcome.




# Two-Bit Branch Predictor
class TwoBitBranchPredictor:
    def __init__(self):
        # Initialize a BHT to store two-bit saturating counters.
        self.bht = {}

    def predict(self, address):
        return 1 if self.bht.get(address, 2) >= 2 else 0  # Default to "Weakly Taken".

    def update(self, address, actual_outcome):
        if address not in self.bht:
            self.bht[address] = 2  # Initialize to "Weakly Taken".
        if actual_outcome == 1:
            self.bht[address] = min(3, self.bht[address] + 1)  # Increment up to "Strongly Taken".
        else:
            self.bht[address] = max(0, self.bht[address] - 1)  # Decrement down to "Strongly Not Taken".



# Bimodal Branch Predictor
class BimodalBranchPredictor:
    def __init__(self, size=1024):
        # Initialize a fixed-size BHT indexed by branch address.
        self.size = size
        self.bht = [2] * size  # Default to "Weakly Taken".

    def predict(self, address):
        index = hash(address) % self.size
        return 1 if self.bht[index] >= 2 else 0

    def update(self, address, actual_outcome):
        index = hash(address) % self.size
        if actual_outcome == 1:
            self.bht[index] = min(3, self.bht[index] + 1)
        else:
            self.bht[index] = max(0, self.bht[index] - 1)




# GShare Branch Predictor
class GShareBranchPredictor:
    def __init__(self, size=1024, history_bits=8):
        # Initialize global history and BHT.
        self.size = size
        self.history = 0
        self.history_bits = history_bits
        self.bht = [2] * size

    def predict(self, address):
        index = (hash(address) ^ self.history) % self.size
        return 1 if self.bht[index] >= 2 else 0

    def update(self, address, actual_outcome):
        index = (hash(address) ^ self.history) % self.size
        if actual_outcome == 1:
            self.bht[index] = min(3, self.bht[index] + 1)
        else:
            self.bht[index] = max(0, self.bht[index] - 1)
        self.history = ((self.history << 1) | actual_outcome) & ((1 << self.history_bits) - 1)



# Hybrid Branch Predictor
class HybridBranchPredictor:
    def __init__(self, size=1024):
        # Initialize choice table, GShare, and Bimodal predictors.
        self.size = size
        self.choice_table = [1] * size
        self.bimodal = BimodalBranchPredictor(size)
        self.gshare = GShareBranchPredictor(size)

    def predict(self, address):
        index = hash(address) % self.size
        if self.choice_table[index] == 1:
            return self.gshare.predict(address)
        else:
            return self.bimodal.predict(address)

    def update(self, address, actual_outcome):
        index = hash(address) % self.size
        gshare_pred = self.gshare.predict(address)
        bimodal_pred = self.bimodal.predict(address)

        # Update both predictors.
        self.gshare.update(address, actual_outcome)
        self.bimodal.update(address, actual_outcome)

        # Update choice table based on which predictor was correct.
        if gshare_pred == actual_outcome and bimodal_pred != actual_outcome:
            self.choice_table[index] = 1
        elif bimodal_pred == actual_outcome and gshare_pred != actual_outcome:
            self.choice_table[index] = 0
