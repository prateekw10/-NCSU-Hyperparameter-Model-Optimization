#!/bin/bash
export NNI_PLATFORM='local'
export NNI_EXP_ID='4oh7uzy2'
export NNI_SYS_DIR='/home/sgupta45/nni-experiments/4oh7uzy2/trials/GDpD9'
export NNI_TRIAL_JOB_ID='GDpD9'
export NNI_OUTPUT_DIR='/home/sgupta45/nni-experiments/4oh7uzy2/trials/GDpD9'
export NNI_TRIAL_SEQ_ID='4'
export NNI_CODE_DIR='/home/sgupta45/test2/Hyperparameter-Optimization-NNI'
cd $NNI_CODE_DIR
eval 'python3 model_vae.py' 1>/home/sgupta45/nni-experiments/4oh7uzy2/trials/GDpD9/stdout 2>/home/sgupta45/nni-experiments/4oh7uzy2/trials/GDpD9/stderr
echo $? `date +%s%3N` >'/home/sgupta45/nni-experiments/4oh7uzy2/trials/GDpD9/.nni/state'