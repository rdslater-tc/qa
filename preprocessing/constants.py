"""Defines constants used for data preprocessing.
"""

TRAIN_FULL_TEXT_TOKENS_FILE = "train.text_tokens"
DEV_FULL_TEXT_TOKENS_FILE = "dev.text_tokens"
TRAIN_SQUAD_FILE = "train-v1.1.json"
TRAIN_CONTEXT_FILE = "train.context.npy"
TRAIN_QUESTION_FILE = "train.question.npy"
TRAIN_SPAN_FILE = "train.spans.npy"
DEV_SQUAD_FILE = "dev-v1.1.json"
DEV_CONTEXT_FILE = "dev.context.npy"
DEV_QUESTION_FILE = "dev.question.npy"
DEV_SPAN_FILE = "dev.spans.npy"
TRAIN_WORD_IN_QUESTION_FILE = "train.word_in_question.npy"
DEV_WORD_IN_QUESTION_FILE = "dev.word_in_question.npy"
TRAIN_WORD_IN_CONTEXT_FILE = "train.word_in_context.npy"
DEV_WORD_IN_CONTEXT_FILE = "dev.word_in_context.npy"
TRAIN_CONTEXT_CHAR_FILE = "train.context.chars.npy"
TRAIN_QUESTION_CHAR_FILE = "train.question.chars.npy"
DEV_CONTEXT_CHAR_FILE = "dev.context.chars.npy"
DEV_QUESTION_CHAR_FILE = "dev.question.chars.npy"
TRAIN_QUESTION_IDS_FILE = "train.question_ids.npy"
TRAIN_QUESTION_IDS_TO_GND_TRUTHS_FILE = "train.question_ids_to_gnd_truths"
DEV_QUESTION_IDS_FILE = "dev.question_ids.npy"
DEV_QUESTION_IDS_TO_GND_TRUTHS_FILE = "dev.question_ids_to_gnd_truths"

CORENLP_URL = "http://nlp.stanford.edu/software/stanford-corenlp-full-2017-06-09.zip"
CORENLP_ZIP_FILE_NAME = "stanford-corenlp-full-2017-06-09.zip"

VECTORS_URL = "http://nlp.stanford.edu/data/glove.840B.300d.zip"
WORD_VEC_DIM = 300
MAX_WORD_LEN = 25
VECTOR_FILE = "glove.840B.300d.txt"
VECTOR_ZIP_FILE = "glove.840B.300d.zip"
SQUAD_TRAIN_URL = "https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json"
SQUAD_TRAIN_FILE = "train-v1.1.json"
SQUAD_DEV_URL = "https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json"
SQUAD_DEV_FILE = "dev-v1.1.json"

EMBEDDING_FILE = "glove.embedding.npy"
VOCAB_FILE = "vocab.txt"

STANFORD_CORENLP_PORT = "9000"
