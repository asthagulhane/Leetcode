class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys =defaultdict(OrderedDict)

    def _update_freq(self, key: int) -> None:
        freq = self.key_to_freq[key]

        del self.freq_to_keys[freq][key]
        
        if freq == self.min_freq and not self.freq_to_keys[freq]:
            self.min_freq += 1

        new_freq = freq + 1
        self.key_to_freq[key] = new_freq
        self.freq_to_keys[new_freq][key] = True   

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self._update_freq(key)  
        return self.key_to_val[key]  

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return

        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._update_freq(key)
            return

        if len(self.key_to_val) >= self.cap:

            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[evict_key] 
            del self.key_to_freq[evict_key] 

        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.min_freq = 1
        self.freq_to_keys[1][key] = True     
        


