# SKILL NEXIS by NEXIS SOLUTIONS
# A comprehensive educational repository for learning Large Language Models (LLMs) from scratch
# Repository: https://github.com/rakeshsoniiii/LLMs


class KVCache:
    def __init__(self, n_layers, batch_size):
        self.cache = [
            [None for _ in range(batch_size)] for _ in range(n_layers)
        ]

    def get(self, layer_idx, batch_idx):
        return self.cache[layer_idx][batch_idx]

    def update(self, layer_idx, batch_idx, value):
        self.cache[layer_idx][batch_idx] = value

    def get_layer(self, layer_idx):
        return self.cache[layer_idx]

    def reset(self):
        for layer in self.cache:
            for i in range(len(layer)):
                layer[i] = None
