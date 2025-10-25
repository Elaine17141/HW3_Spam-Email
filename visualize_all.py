import os
import subprocess
from datetime import datetime

# �Ыؿ�X��Ƨ�
os.makedirs("reports/visualizations", exist_ok=True)

def run_cmd(cmd):
    print(f"\n[Running] {cmd}")
    subprocess.run(cmd, shell=True, check=False)

print("\n========== Phase 4: Visualization Batch Run ==========")
print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# 1?? ���O������
run_cmd("python scripts/visualize_spam.py --class-dist --input datasets/processed/sms_spam_clean.csv --label-col col_0")

# 2?? Token �W�v��
run_cmd("python scripts/visualize_spam.py --token-freq --input datasets/processed/sms_spam_clean.csv --label-col col_0 --text-col col_1 --topn 20")

# 3?? �V�c�x�}�BROC�BPR ���u
run_cmd("python scripts/visualize_spam.py --confusion-matrix --roc --pr --models-dir models --input datasets/processed/sms_spam_clean.csv --label-col col_0 --text-col col_1")

# 4?? �H�ȱ��y�Ϫ�
run_cmd("python scripts/visualize_spam.py --threshold-sweep --models-dir models --input datasets/processed/sms_spam_clean.csv --label-col col_0 --text-col col_1")

print("\n? All visualizations generated successfully!")
print("?  Check the output folder: reports/visualizations/")
