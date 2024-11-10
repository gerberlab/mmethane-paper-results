import os

import os
import time
import shutil
case = ''


for log_file in ['/Users/jendawk/github-repos/mmethane-paper-results/SemiSynData/']:
    for root, dirs, files in os.walk(log_file):
        for file in files:
            # if 'seed_0' not in root:
            # if file=='visualization.pdf':
            #     os.remove(os.path.join(root, file))
            if file.startswith("feats_evaluation_over_seeds") or file.endswith(".yaml") or file=="scores_at_eval.csv" or file=="metabs_emb_locs.csv":
                print(os.path.join(root, file))
                os.remove(os.path.join(root, file))
                # time.sleep(0.01)
            #     # print(os.path.isfile(os.path.join(root, file)))
            # if file.endswith(".ckpt"):
            #     print(os.path.join(root, file))
            #     os.remove(os.path.join(root, file))
            #     time.sleep(0.01)

            # if file.endswith(".pdf"):
            #     print(os.path.join(root, file))
            #     os.remove(os.path.join(root, file))
            #     time.sleep(0.01)
            # if 'seed_0' not in root and file.endswith('.pdf'):
            #     print(os.path.join(root, file))
            #     os.remove(os.path.join(root,file))

            # if 'seed_0' not in root and file.endswith('.pkl'):
            #     print(os.path.join(root, file))
            #     os.remove(os.path.join(root,file))

            # if 'combo_modules' in file and file.endswith('.pdf'):
            #     print(os.path.join(root, file))
            #     os.remove(os.path.join(root,file))