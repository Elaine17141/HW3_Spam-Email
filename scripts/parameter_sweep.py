#!/usr/bin/env python3
"""
�ѼƷj���}���A�Ω�M��̨Ϊ��U���l��������t�m�C
�������j�����u�ƥH�U�ѼơG
- class_weight
- ngram_range
- min_df
- C (SVM regularization)
- eval_threshold

���G�|�O�s�b reports/sweep_results.json�A�̨μҫ��O�s�b models/ �ؿ��C
"""

import joblib
import numpy as np
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import ParameterGrid
import json
from pathlib import Path
import time
from datetime import datetime
import logging
import itertools

# �]�m��x
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('reports/parameter_sweep.log'),
        logging.StreamHandler()
    ]
)

# �T�O�ؿ��s�b
Path("models").mkdir(exist_ok=True)
Path("reports").mkdir(exist_ok=True)
Path("reports/sweeps").mkdir(exist_ok=True)

def create_parameter_grid():
    """�w�q�ѼƷj���Ŷ�"""
    param_grid = {
        'class_weight': ['balanced', None],
        'ngram_range': [(1,1), (1,2), (1,3)],
        'min_df': [1, 2, 3, 5],
        'C': [0.1, 1.0, 10.0],
        'eval_threshold': [0.3, 0.4, 0.5, 0.6, 0.7]
    }
    return param_grid

def train_and_evaluate(X_train, X_test, y_train, y_test, params, vectorizer=None):
    """�ϥε��w�ѼưV�m�M�����ҫ�"""
    try:
        start_time = time.time()
        
        # �S�x����
        if vectorizer is None:
            vectorizer = TfidfVectorizer(
                max_features=5000,
                max_df=0.95,
                ngram_range=params['ngram_range'],
                min_df=params['min_df'],
                sublinear_tf=True
            )
            X_train_features = vectorizer.fit_transform(X_train)
            X_test_features = vectorizer.transform(X_test)
        else:
            X_train_features = X_train
            X_test_features = X_test
        
        # �V�m�ҫ�
        base_svm = LinearSVC(
            C=params['C'],
            class_weight=params['class_weight'],
            random_state=42,
            max_iter=1000
        )
        
        model = CalibratedClassifierCV(base_svm, cv=5)
        model.fit(X_train_features, y_train)
        
        # �w���M����
        y_prob = model.predict_proba(X_test_features)[:, 1]
        y_pred = (y_prob >= params['eval_threshold']).astype(int)
        
        # �p�����
        report = classification_report(y_test, y_pred, output_dict=True)
        conf_matrix = confusion_matrix(y_test, y_pred)
        
        training_time = time.time() - start_time
        
        results = {
            'accuracy': report['accuracy'],
            'precision': report['1']['precision'],
            'recall': report['1']['recall'],
            'f1': report['1']['f1-score'],
            'confusion_matrix': conf_matrix.tolist(),
            'training_time': training_time,
            'success': True,
            'error': None
        }
        
        return results, model, vectorizer
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'training_time': time.time() - start_time
        }, None, None

def run_parameter_sweep():
    """����ѼƷj���ðO�����G"""
    # ���J���
    logging.info("Loading preprocessed data...")
    processed_data = joblib.load('data/processed_data.joblib')
    
    # ����Ѽƺ���
    param_grid = create_parameter_grid()
    all_combinations = list(ParameterGrid(param_grid))
    total_combinations = len(all_combinations)
    
    logging.info(f"Starting parameter sweep with {total_combinations} combinations")
    
    # ��l�Ƶ��G�l?
    all_results = []
    best_score = {
        'f1': -1,
        'precision': -1,
        'recall': -1
    }
    best_models = {
        'f1': None,
        'precision': None,
        'recall': None
    }
    best_params = {
        'f1': None,
        'precision': None,
        'recall': None
    }
    
    # �}�l�j��
    for i, params in enumerate(all_combinations, 1):
        logging.info(f"\nTrying combination {i}/{total_combinations}:")
        logging.info(f"Parameters: {params}")
        
        # �V�m�M����
        results, model, vectorizer = train_and_evaluate(
            processed_data['X_train'],
            processed_data['X_test'],
            processed_data['y_train'],
            processed_data['y_test'],
            params
        )
        
        if not results['success']:
            logging.warning(f"Failed with parameters {params}: {results['error']}")
            continue
        
        # �O�����G
        results['parameters'] = params
        all_results.append(results)
        
        # ��s�̨μҫ��]�ˬd F1�Bprecision �M recall�^
        metrics = ['f1', 'precision', 'recall']
        for metric in metrics:
            if results[metric] > best_score[metric]:
                best_score[metric] = results[metric]
                best_models[metric] = (model, vectorizer)
                best_params[metric] = params
                
                # �O�s�s���̨μҫ�
                if model is not None and vectorizer is not None:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    model_path = f"models/best_{metric}_model_{timestamp}.joblib"
                    vectorizer_path = f"models/best_{metric}_vectorizer_{timestamp}.joblib"
                    
                    joblib.dump(model, model_path)
                    joblib.dump(vectorizer, vectorizer_path)
                    
                    logging.info(f"New best {metric}: {results[metric]:.4f}")
                    logging.info(f"Saved best {metric} model to {model_path}")
    
    # �O�s�Ҧ����G
    sweep_results = {
        'total_combinations': total_combinations,
        'completed_combinations': len(all_results),
        'best_scores': {
            metric: {
                'score': best_score[metric],
                'parameters': best_params[metric]
            }
            for metric in ['f1', 'precision', 'recall']
        },
        'all_results': all_results
    }
    
    # �N���G�O�s�� JSON
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = f"reports/sweeps/sweep_results_{timestamp}.json"
    
    with open(results_file, 'w') as f:
        json.dump(sweep_results, f, indent=2)
    
    # ���͵��G�K�n���i
    generate_sweep_report(sweep_results, timestamp)
    
    return sweep_results

def generate_sweep_report(results, timestamp):
    """�ͦ��ѼƷj�����K�n���i"""
    report_lines = [
        "Parameter Sweep Results Summary",
        "============================\n",
        f"Total configurations tested: {results['total_combinations']}",
        f"Successful runs: {results['completed_combinations']}\n",
        "Best Configurations:",
        "-----------------"
    ]
    
    for metric in ['f1', 'precision', 'recall']:
        best = results['best_scores'][metric]
        report_lines.extend([
            f"\nBest {metric.upper()}:",
            f"Score: {best['score']:.4f}",
            "Parameters:",
            "\n".join(f"- {k}: {v}" for k, v in best['parameters'].items())
        ])
    
    # �K�[�ѼƤ��R
    report_lines.extend([
        "\nParameter Analysis",
        "-----------------"
    ])
    
    # �N���G�ഫ�� DataFrame �i����R
    df = pd.DataFrame(results['all_results'])
    
    for param in results['all_results'][0]['parameters'].keys():
        param_results = df.groupby(df['parameters'].apply(lambda x: x[param])).agg({
            'f1': ['mean', 'std'],
            'precision': ['mean', 'std'],
            'recall': ['mean', 'std']
        }).round(4)
        
        report_lines.extend([
            f"\nImpact of {param}:",
            param_results.to_string()
        ])
    
    # �O�s���i
    report_file = f"reports/sweeps/sweep_report_{timestamp}.txt"
    with open(report_file, 'w') as f:
        f.write('\n'.join(report_lines))
    
    logging.info(f"Generated sweep report: {report_file}")

if __name__ == "__main__":
    logging.info("Starting parameter sweep...")
    sweep_results = run_parameter_sweep()
    logging.info("Parameter sweep completed.")