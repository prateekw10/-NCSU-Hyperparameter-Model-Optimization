#!/bin/bash
export NNI_PLATFORM='local'
export NNI_EXP_ID='xosr8gzl'
export NNI_SYS_DIR='/home/sgupta45/nni-experiments/xosr8gzl/trials/rqezd'
export NNI_TRIAL_JOB_ID='rqezd'
export NNI_OUTPUT_DIR='/home/sgupta45/nni-experiments/xosr8gzl/trials/rqezd'
export NNI_TRIAL_SEQ_ID='4'
export NNI_CODE_DIR='/home/sgupta45/test2/Hyperparameter-Optimization-NNI'
cd $NNI_CODE_DIR
eval 'python3 model_vae.py' 1>/home/sgupta45/nni-experiments/xosr8gzl/trials/rqezd/stdout 2>/home/sgupta45/nni-experiments/xosr8gzl/trials/rqezd/stderr
echo $? `date +%s%3N` >'/home/sgupta45/nni-experiments/xosr8gzl/trials/rqezd/.nni/state'