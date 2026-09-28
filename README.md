# SKILL NEXIS by NEXIS SOLUTIONS

A comprehensive educational repository for learning Large Language Models (LLMs) from scratch. This collection contains code, tutorials, and learning materials for developing, pretraining, and finetuning GPT-like LLMs.

# Table of Contents

- [Troubleshooting Guide](./troubleshooting.md)
- **Setup Guide**: See [setup/README.md](setup/README.md) for Python installation and environment setup.


| Chapter Title                                              | Main Code (for Quick Access)                                                                                                    | All Code + Supplementary      |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| [Setup recommendations](setup)                            | -                                                                                                                               | -                             |
| Ch 1: Understanding Large Language Models                  | No code                                                                                                                         | -                             |
| Ch 2: Working with Text Data                               | - [ch02.ipynb](ch02/01_main-chapter-code/ch02.ipynb)<br/>- [dataloader.ipynb](ch02/01_main-chapter-code/dataloader.ipynb) (summary)<br/>- [exercise-solutions.ipynb](ch02/01_main-chapter-code/exercise-solutions.ipynb)               | [./ch02](./ch02)            |
| Ch 3: Coding Attention Mechanisms                          | - [ch03.ipynb](ch03/01_main-chapter-code/ch03.ipynb)<br/>- [multihead-attention.ipynb](ch03/01_main-chapter-code/multihead-attention.ipynb) (summary) <br/>- [exercise-solutions.ipynb](ch03/01_main-chapter-code/exercise-solutions.ipynb)| [./ch03](./ch03)             |
| Ch 4: Implementing a GPT Model from Scratch                | - [ch04.ipynb](ch04/01_main-chapter-code/ch04.ipynb)<br/>- [gpt.py](ch04/01_main-chapter-code/gpt.py) (summary)<br/>- [exercise-solutions.ipynb](ch04/01_main-chapter-code/exercise-solutions.ipynb) | [./ch04](./ch04)           |
| Ch 5: Pretraining on Unlabeled Data                        | - [ch05.ipynb](ch05/01_main-chapter-code/ch05.ipynb)<br/>- [gpt_train.py](ch05/01_main-chapter-code/gpt_train.py) (summary) <br/>- [gpt_generate.py](ch05/01_main-chapter-code/gpt_generate.py) (summary) <br/>- [exercise-solutions.ipynb](ch05/01_main-chapter-code/exercise-solutions.ipynb) | [./ch05](./ch05)              |
| Ch 6: Finetuning for Text Classification                   | - [ch06.ipynb](ch06/01_main-chapter-code/ch06.ipynb)  <br/>- [gpt_class_finetune.py](ch06/01_main-chapter-code/gpt_class_finetune.py)  <br/>- [exercise-solutions.ipynb](ch06/01_main-chapter-code/exercise-solutions.ipynb) | [./ch06](./ch06)              |
| Ch 7: Finetuning to Follow Instructions                    | - [ch07.ipynb](ch07/01_main-chapter-code/ch07.ipynb)<br/>- [gpt_instruction_finetuning.py](ch07/01_main-chapter-code/gpt_instruction_finetuning.py) (summary)<br/>- [ollama_evaluate.py](ch07/01_main-chapter-code/ollama_evaluate.py) (summary)<br/>- [exercise-solutions.ipynb](ch07/01_main-chapter-code/exercise-solutions.ipynb) | [./ch07](./ch07)  |
| Appendix A: Introduction to PyTorch                        | - [code-part1.ipynb](appendix-A/01_main-chapter-code/code-part1.ipynb)<br/>- [code-part2.ipynb](appendix-A/01_main-chapter-code/code-part2.ipynb)<br/>- [DDP-script.py](appendix-A/01_main-chapter-code/DDP-script.py)<br/>- [exercise-solutions.ipynb](appendix-A/01_main-chapter-code/exercise-solutions.ipynb) | [./appendix-A](./appendix-A) |
| Appendix B: References and Further Reading                 | No code                                                                                                                         | [./appendix-B](./appendix-B) |
| Appendix C: Exercise Solutions                             | - [list of exercise solutions](appendix-C)                                                                 | [./appendix-C](./appendix-C) |
| Appendix D: Adding Bells and Whistles to the Training Loop | - [appendix-D.ipynb](appendix-D/01_main-chapter-code/appendix-D.ipynb)                                                          | [./appendix-D](./appendix-D)  |
| Appendix E: Parameter-efficient Finetuning with LoRA       | - [appendix-E.ipynb](appendix-E/01_main-chapter-code/appendix-E.ipynb)                                                          | [./appendix-E](./appendix-E) |

## Prerequisites

The most important prerequisite is a strong foundation in Python programming.
With this knowledge, you will be well prepared to explore the fascinating world of LLMs
and understand the concepts and code examples presented in this repository.

If you have some experience with deep neural networks, you may find certain concepts more familiar, as LLMs are built upon these architectures.

This repository uses PyTorch to implement the code from scratch without using any external LLM libraries. While proficiency in PyTorch is not a prerequisite, familiarity with PyTorch basics is certainly useful. If you are new to PyTorch, Appendix A provides a concise introduction to PyTorch.



&nbsp;

## Hardware Requirements

The code in the main chapters is designed to run on conventional laptops within a reasonable timeframe and does not require specialized hardware. This approach ensures that a wide audience can engage with the material. Additionally, the code automatically utilizes GPUs if they are available. (Please see the [setup](setup/README.md) doc for additional recommendations.)

## Exercises

Each chapter includes several exercises. The solutions are summarized in Appendix C, and the corresponding code notebooks are available in the main chapter folders of this repository (for example,  [./ch02/01_main-chapter-code/exercise-solutions.ipynb](./ch02/01_main-chapter-code/exercise-solutions.ipynb)).

## Bonus Material

Several folders contain optional materials as a bonus for interested readers:
- **Setup**
  - [Python Setup Tips](setup/01_optional-python-setup-preferences)
  - [Installing Python Packages and Libraries Used in This Repository](setup/02_installing-python-libraries)
  - [Docker Environment Setup Guide](setup/03_optional-docker-environment)

- **Chapter 2: Working With Text Data**
  - [Byte Pair Encoding (BPE) Tokenizer From Scratch](ch02/05_bpe-from-scratch/bpe-from-scratch-simple.ipynb)
  - [Comparing Various Byte Pair Encoding (BPE) Implementations](ch02/02_bonus_bytepair-encoder)
  - [Understanding the Difference Between Embedding Layers and Linear Layers](ch02/03_bonus_embedding-vs-matmul)
  - [Dataloader Intuition With Simple Numbers](ch02/04_bonus_dataloader-intuition)
  - [BPE From Scratch](ch02/05_bpe-from-scratch)
  - [SimpleTokenizerV3 variant](ch02/06_bonus_simple-tokenizer-v3)

- **Chapter 3: Coding Attention Mechanisms**
  - [Comparing Efficient Multi-Head Attention Implementations](ch03/02_bonus_efficient-multihead-attention/mha-implementations.ipynb)
  - [Understanding PyTorch Buffers](ch03/03_understanding-buffers/understanding-buffers.ipynb)

- **Chapter 4: Implementing a GPT Model From Scratch**
  - [FLOPs Analysis](ch04/02_performance-analysis/flops-analysis.ipynb)
  - [KV Cache](ch04/03_kv-cache)
  - [Attention Alternatives](ch04/#attention-alternatives)
    - [Grouped-Query Attention](ch04/04_gqa)
    - [Multi-Head Latent Attention](ch04/05_mla)
    - [Sliding Window Attention](ch04/06_swa)
    - [Gated DeltaNet](ch04/08_deltanet)
    - [DeepSeek Sparse Attention (DSA)](ch04/09_dsa)
    - [Cross-Layer KV Sharing](ch04/10_kv-sharing)
  - [Mixture-of-Experts (MoE)](ch04/07_moe)

- **Chapter 5: Pretraining on Unlabeled Data**
  - [Alternative Weight Loading Methods](ch05/02_alternative_weight_loading/)
  - [Pretraining GPT on the Project Gutenberg Dataset](ch05/03_bonus_pretraining_on_gutenberg)
  - [Adding Bells and Whistles to the Training Loop](ch05/04_learning_rate_schedulers)
  - [Discrepancies between CPU and MPS Devices](ch05/19_cpu_mps_differences)
  - [Optimizing Hyperparameters for Pretraining](ch05/05_bonus_hparam_tuning)
  - [Building a User Interface to Interact With the Pretrained LLM](ch05/06_user_interface)
  - [Converting GPT to Llama](ch05/07_gpt_to_llama)
  - [Memory-efficient Model Weight Loading](ch05/08_memory_efficient_weight_loading/memory-efficient-state-dict.ipynb)
  - [Extending the Tiktoken BPE Tokenizer with New Tokens](ch05/09_extending-tokenizers/extend-tiktoken.ipynb)
  - [PyTorch Performance Tips for Faster LLM Training](ch05/10_llm-training-speed)
  - [LLM Architectures](ch05/#llm-architectures-from-scratch)
    - [Llama 3.2 From Scratch](ch05/07_gpt_to_llama/standalone-llama32.ipynb)
    - [Qwen3 Dense and Mixture-of-Experts (MoE) From Scratch](ch05/11_qwen3/)
    - [Gemma 3 From Scratch](ch05/12_gemma3/)
    - [Olmo 3 From Scratch](ch05/13_olmo3/)
    - [Tiny Aya From Scratch](ch05/15_tiny-aya/)
    - [Qwen3.5 From Scratch](ch05/16_qwen3.5/)
    - [Gemma 4 E2B and E4B From Scratch](ch05/17_gemma4/)
  - [Chapter 5 with other LLMs as Drop-In Replacement (e.g., Llama 3, Qwen 3)](ch05/14_ch05_with_other_llms/)
- **Chapter 6: Finetuning for classification**
  - [Additional Experiments Finetuning Different Layers and Using Larger Models](ch06/02_bonus_additional-experiments)
  - [Finetuning Different Models on the 50k IMDb Movie Review Dataset](ch06/03_bonus_imdb-classification)
  - [Building a User Interface to Interact With the GPT-based Spam Classifier](ch06/04_user_interface)
- **Chapter 7: Finetuning to follow instructions**
  - [Dataset Utilities for Finding Near Duplicates and Creating Passive Voice Entries](ch07/02_dataset-utilities)
  - [Evaluating Instruction Responses Using the OpenAI API and Ollama](ch07/03_model-evaluation)
  - [Generating a Dataset for Instruction Finetuning](ch07/05_dataset-generation/llama3-ollama.ipynb)
  - [Improving a Dataset for Instruction Finetuning](ch07/05_dataset-generation/reflection-gpt4.ipynb)
  - [Generating a Preference Dataset With Llama 3.1 70B and Ollama](ch07/04_preference-tuning-with-dpo/create-preference-data-ollama.ipynb)
  - [Direct Preference Optimization (DPO) for LLM Alignment](ch07/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb)
  - [Building a User Interface to Interact With the Instruction-Finetuned GPT Model](ch07/06_user_interface)
