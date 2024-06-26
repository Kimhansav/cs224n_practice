# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

from tqdm import tqdm

import utils

eval_corpus_path = "birth_dev.tsv"
eval = open(eval_corpus_path, "r")
len_eval = len(eval.readlines())
prediction = ["London"]*len_eval
total, correct = utils.evaluate_places(eval_corpus_path, prediction)
if total > 0 :
    print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
else:
    print('No targets provided!')
