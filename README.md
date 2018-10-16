[![Build Status](https://travis-ci.org/Zethson/MHC-1-Binding-Predictor-iGEM2018-Tuebingen.svg?branch=master)](https://travis-ci.org/Zethson/MHC-1-Binding-Predictor-iGEM2018-Tuebingen)
[![codecov](https://codecov.io/gh/Zethson/MHC-1-Binding-Predictor-iGEM2018-Tuebingen/branch/master/graph/badge.svg)](https://codecov.io/gh/Zethson/MHC-1-Binding-Predictor-iGEM2018-Tuebingen)
[![BCH compliance](https://bettercodehub.com/edge/badge/Zethson/MHC-1-Binding-Predictor-iGEM2018-Tuebingen?branch=development)](https://bettercodehub.com/)

# MHCBoost
Gradient boosted trees based predictor for MHC Class I epitope binding prediction.

How to install
=====
1. <code>git clone https://github.com/Zethson/MHC-1-Binding-Predictor-iGEM2018-Tuebingen</code>
2. <code>python setup.py install</code>
3. <code>mhc-1</code>

Usage
=====
## The CLI - Command Line Interface
```bash
> mhc-1
-p, --dataset_to_predict_path             <arg> file to perform prediction on OR peptide sequence
-o, --predicted_dataset_path              <arg> filepath to save the predicted output file to
-a, --allele                              <arg> allele to perform prediction on
-l, --peptide_length                      <arg> epitope peptide length - usually 9
optional -t, --training_dataset_path      <arg> file for classifier training
optional -s, --silent                     suppresses learning output

```

Examples
=====
Simply provide the answers to the questions asked by our tool.
```bash
> mhc-1 
```
Alternatively, provide input parameters when starting the tool.
```bash
> mhc-1 -p/data/example_input.txt -o /home/mypc/Desktop/output.txt -a A*02:01 -l 9
```
Supported Alleles
=====
MHCBoost supports 65 alleles. 

Performance
=====
MHCBoost has an 5-fold crossvalidated average AUC of 0.899 on the IEDB dataset.
The performance on each allele was compared to the state of the art NetMHCPan. Please refer to [].

License
=====
MIT

Authors
=====
Team iGEM 2018 Tübingen    
Lukas Heumos    
Steffen Lemke    
Alexander Röhl

