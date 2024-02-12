""" 
Evlating Trident Model

To be appended to Trident Model script

"""

import time

df = pd.read_csv('/path/to/binary_model/Test_Dataset.csv')
df = df.sample(frac=1, random_state=25)
y_true = df['GreenV'].to_numpy().flatten()
y_true
df.dtypes

tridentValues = []
times = []
for abstract in df['Abstract'][0:100]:
  start_time = time.time()
  abstract_embedding = sentence_embedder(abstract, Model_Path)
  Number = 10
  broad_scope_predictions = broad_scope_class_predictor(class_embeddings, abstract_embedding, Number, Sensitivity='Medium')
  BinaryScore = predict_green(abstract, Model)

  if broad_scope_predictions[2] == 'True' and BinaryScore > 0.5:
    print('Input Text almost certainly related to a Green Plastic')
    green_scope_class_predictor(green_class_embeddings, abstract_embedding, Number)
    tridentV = 1
  elif broad_scope_predictions[2] == 'True' and BinaryScore == 0.5:
    print('Very Likely to be a Green Plastic')
    tridentV = 1
    green_scope_class_predictor(green_class_embeddings, abstract_embedding, Number)
  elif broad_scope_predictions[2] == 'False' and BinaryScore >=0.5:
    print('Not sure if input text is related to a Green Plastic or Not. Please Review Further')
    green_scope_class_predictor(green_class_embeddings, abstract_embedding, Number)
    tridentV = 1
  elif broad_scope_predictions[2] == 'False' and BinaryScore < 0.5:
    print('Input text  Very Unikely to be related to a Green Plastic')
    tridentV = 0
  else:
    print('Input text  Very Unikely to be related to a Green Plastic')

  tridentValues.append(tridentV)
  print("--- %s seconds ---" % (time.time() - start_time))
  times.append(time.time() - start_time)



from sklearn.metrics import accuracy_score, precision_recall_fscore_support
def cal_accuray(y_test, y_pred):
  acc = accuracy_score(y_test, y_pred) * 100
  pres, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')

  res = {'accuracy':acc,
         'precision': pres,
         'recall': recall,
         'f1': f1}

  return res


cal_accuray(y_true[0:100], tridentValues)

# Evaluate Binary
tridentValues2 = []
times = []

for abstract in df['Abstract'][0:100]:
  start_time = time.time()
  BinaryScore = predict_green(str(abstract), Model)

  if BinaryScore >= 0.5:
    print(BinaryScore)
    tridentV = 1
  elif BinaryScore < 0.5:
    tridentV = 0
  else:
    print('Input text  Very Unikely to be related to a Green Plastic')

  tridentValues2.append(tridentV)
  print("--- %s seconds ---" % (time.time() - start_time))
  times.append(time.time() - start_time)

cal_accuray(y_true[0:100], tridentValues2)






