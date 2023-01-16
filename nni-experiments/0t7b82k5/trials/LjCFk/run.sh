#!/bin/bash
export NNI_PLATFORM='local'
export NNI_EXP_ID='0t7b82k5'
export NNI_SYS_DIR='/home/sgupta45/nni-experiments/0t7b82k5/trials/LjCFk'
export NNI_TRIAL_JOB_ID='LjCFk'
export NNI_OUTPUT_DIR='/home/sgupta45/nni-experiments/0t7b82k5/trials/LjCFk'
export NNI_TRIAL_SEQ_ID='0'
export NNI_CODE_DIR='/home/sgupta45/test2/Hyperparameter-Optimization-NNI'
cd $NNI_CODE_DIR
eval 'python3 model_vae.py' 1>/home/sgupta45/nni-experiments/0t7b82k5/trials/LjCFk/stdout 2>/home/sgupta45/nni-experiments/0t7b82k5/trials/LjCFk/stderr
echo $? `date +%s%3N` >'/home/sgupta45/nni-experiments/0t7b82k5/trials/LjCFk/.nni/state'