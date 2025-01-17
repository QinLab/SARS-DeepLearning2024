# Train model

## Steps for training
1. Download `alignment-and-proteins/msa_2022-06-16/2022-06-16_unmasked.fa` for having sequences and `variant_surveillance_tsv_2022_06_16/variant_surveillance.tsv` for having labels of sequences from [GISAID](https://gisaid.org/).
2. Save data in these directories:
    - `<root_repository>/GISAID/alignment-and-proteins/msa_2022-06-16/2022-06-16_unmasked.fa`
    - `<root_repository>/GISAID/variant_surveillance_tsv_2022_06_16/variant_surveillance.tsv`
3. Create these folders:
```
data 
│
├── train
└── test   
```
4. Ensure the root directory is in `PYTHONPATH`
```
export PYTHONPATH="<ROOT_DIRECTORY>:$PYTHONPATH"
```
5. To balance data: Run 
```python3 <root_repository>/training/data_prep.py```
6. To make train and test dataset: Run 
```python3 <root_repository>/training/split_data_train_val_test.py```
7. To train the model: Run 
```python3 <root_repository>/training/main.py 64 15```
-batch_size = 64, epoches=15.
 

## Summary of our model


| Layer (type)                |Output Shape            |Param  |   
| --------------------------- |:----------------------:|:-----:|
|conv1d (Conv1D)              | (None, 9958, 196)      | 26264 |                                                                    
|max_pooling1d (MaxPooling1D) | (None, 1991, 196)      | 0     |                                                
|conv1d_1 (Conv1D)            | (None, 658, 196)       |730100 |                                                                   
|max_pooling1d_1(MaxPooling1D)| (None, 131, 196)       | 0     |                                              
|flatten (Flatten)            | (None, 25676)          | 0     |           
|dense (Dense)                | (None, 164)            |4211028|                                                        
|dense_1 (Dense)              | (None, 42)             | 6930  |                                                               
|dense_2 (Dense)              | (None, 20)             | 860   |                                                                     
|dropout (Dropout)            | (None, 20)             | 0     |                                                                    
|dense_3 (Dense)              | (None, 5)              | 105   |    
 
- Total params: 4,975,287
- Trainable params: 4,975,287
- Non-trainable params: 0

## Results
* Accuracy in training and validation dataset

![Accuracy](/results/Training_validation_accuracy.jpg)

* Loss in training and validation dataset

![Loss](/results/Training_validation_loss.jpg)