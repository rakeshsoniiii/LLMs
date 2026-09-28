# SKILL NEXIS by NEXIS SOLUTIONS
# A comprehensive educational repository for learning Large Language Models (LLMs) from scratch
# Repository: https://github.com/rakeshsoniiii/LLMs


# Additional utility and helper functions for text generation not covered
# in the main chapters

def trim_input_tensor(input_ids_tensor, context_len, max_new_tokens):
    assert max_new_tokens < context_len
    keep_len = max(1, context_len - max_new_tokens)

    # If the prompt is too long, left-truncate to keep_len
    if input_ids_tensor.shape[1] > keep_len:
        input_ids_tensor = input_ids_tensor[:, -keep_len:]

    return input_ids_tensor
