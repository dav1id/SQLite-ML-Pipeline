import tensorflow as tf 
import pandas as pd 
'''
Will test on csv files, then sql
'''
dftrain = pd.read_csv()
dfeval = pd.read_csv()

y_train = dftrain.pop(target)
y_eval = dfeval.pop(target)

categorical_columns = [] 
numeric_columns = []
feature_columns = []

def sortColumns():
   for column in categorical_columns:
    vocabulary = dftrain[column].unique()
    feature_columns.append(tf.feature_column_with_vocabulary_list(column, vocabulary))

for column in numeric_columns:
    feature_columns.append(tf.feature_column.numeric_column(column, dtype=tf.float32))


def make_input_fn(data_df, label_df, num_epochs=10, shuffle = True, batch_size=32):
    def input_function():
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
        if shuffle:
            ds = ds.shuffle(1000)
        ds =  ds.batch(batch_size).repeat(num_epochs)
        return ds
    return input_function

train_input_fn = make_input_fn(dftrain, y_train)
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)

