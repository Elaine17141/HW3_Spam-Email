# �U��²�T�����t��

�o�O�@�Ӱ������ǲߪ��U��²�T�]Spam�^�����t�ΡA�ϥ� TF-IDF �M�޿�j�k�ҫ����ѧO�U��²�T�C�Өt�Υ]�t���㪺�V�m�y�{�B���ʦ�����O�A�H�ΧY�ɹw���\��C

## �\��S�I

- �奻�w�B�z�M�M�z
- �ϥ� TF-IDF �i��奻�S�x����
- �ϥ��޿�j�k�i�����
- ���ʦ� Streamlit ����O�A�]�t�G
  - ��Ƥ�����ı��
  - �ҫ��ʯ����
  - �Y�ɹw������
- �i�վ㪺�����H��
- ���㪺�������С]�ǽT�v�B��T�v�B�l�^�v�BF1���ơ^

## �t�λݨD

- Python 3.6+
- �̮ۨM��C��Ш� `requirements.txt`

## �M�׵��c

```
.
�u�w�w app/                    # Streamlit ���ε{��
�x   �|�w�w streamlit_app.py    # ���ʦ�����O
�u�w�w datasets/              # ��ƶ�
�x   �u�w�w processed/         # �B�z�᪺���
�x   �|�w�w sms_spam_no_header.csv  # ��l���
�u�w�w ml/                   # �����ǲ߬����{���X
�u�w�w models/               # �V�m�n���ҫ�
�u�w�w reports/              # �V�m���i�M��ı��
�x   �|�w�w visualizations/   # ��ı�ƹϪ�
�|�w�w scripts/              # �V�m�M�����}��
```

## �w�˻���

1. �J���M�סG
```bash
git clone [�M�׺��}]
cd [�M�׸�Ƨ�]
```

2. �w�ˬ̮ۨM��G
```bash
pip install -r requirements.txt
```

## �ϥλ���

### �V�m�ҫ�

�B��V�m�}���G
```bash
python scripts/train_spam_classifier.py
```

�i��ѼơG
- `--input`: ��JCSV�ɮ׸��|
- `--test-size`: ���ն���� (�w�]: 0.2)
- `--seed`: �H���ؤl (�w�]: 42)
- `--C`: �޿�j�k���h�ưѼ� (�w�]: 1.0)

### �Ұʻ���O

�B�� Streamlit ���ε{���G
```bash
streamlit run app/streamlit_app.py
```

����O�\��G
- ��Ƥ�����ı��
- �`�����J���R
- �ҫ��ʯ����
- �Y�ɹw������

## �D�n�S��

- �奻�w�B�z�G�۰ʳB�z URL�B�q�l�l��B�q�ܸ��X���S��奻
- �i�վ㪺�����H�ȡG�ھڻݨD���ź�T�v�M�l�^�v
- ��ı�Ƥu��G���ѧ��㪺�ҫ��ʯ��ı��
- �Y�ɹw���G�䴩����T�����Y�ɤ����w��
