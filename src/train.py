import tensorflow as tf 
import pandas as pd 
'''
Will test on csv files, then sql

source venv/bin/activate
python3.11 src/train.py
'''
dftrain = pd.read_csv('/Users/davidola/Desktop/student/student-por.csv', delimiter=';')
dfeval = pd.read_csv('/Users/davidola/Desktop/student/student-mat.csv', delimiter=';')
#print(dftrain.head())
print(dftrain.columns)

target = 'failures'
y_train = dftrain.pop(target)
y_eval = dfeval.pop(target)

categorical_columns = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob', 'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic'] # Columns containing discrete values (Yes, no...)
numeric_columns = ['age', 'traveltime', 'studytime', 'failures', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2', 'G3'] # Columns containing numerical values (1,2,3,4....)
feature_columns = [] # Columns that are harder to encode, since each row has some unique value (name, id, etc)

def sortColumns():
    for column in categorical_columns:
        vocabulary = dftrain[column].unique()
        feature_columns.append(tf.keras.layers.StringLookup(vocabulary=vocabulary, output_mode='int'))

    for column in numeric_columns:
        feature_columns.append(tf.keras.layers.Normalization())

def make_input_fn(data_df, label_df, num_epochs=10, shuffle = True, batch_size=32):
    def input_function():
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
        if shuffle:
            ds = ds.shuffle(1000)
        ds =  ds.batch(batch_size).repeat(num_epochs)
        return ds
    return input_function

sortColumns()
train_input_fn = make_input_fn(dftrain, y_train)
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)

linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)
linear_est.train(train_input_fn)
result = linear_est.evaluate(eval_input_fn)


print(result['accuracy'])

result = list(linear_est.evaluate(eval_input_fn))
print(result[0]['probabilities'][1])
