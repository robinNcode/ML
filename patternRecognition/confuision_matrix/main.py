import pandas

data = pandas.read_csv('confuision_matrix\data.csv')
print(data)

tp, tn, fp, fn = 0, 0, 0, 0
for datum in range(len(data)):
    if data['actual'][datum] == data['predicted'][datum]:
        if data['actual'][datum] == 'Alive':
            tp += 1
        else:
            tn += 1
    else:
        if data['actual'][datum] == 'Dead':
            fn += 1
        else:
            fp += 1

print('True Positive:', tp)
print('True Negative:', tn)
print('False Positive:', fp)
print('False Negative:', fn)

id = int(input("Enter last 2 digit of your ID: "))

if id % 10 == 1 or id % 10 == 6:
    print('Precision:', tp / (tp + fp))
elif id % 10 == 4 or id % 10 == 7:
    print('Recall:', tp / (tp + fn))
elif id % 10 == 0 or id % 10 == 3 or id % 10 == 8:
    print('Sensitivity:', tp / (tp + fn))
elif id % 10 == 2 or id % 10 == 5 or id % 10 == 9:
    print('Specificity:', tn / (tn + fp))

# print('Accuracy:', (tp + tn) / (tp + tn + fp + fn))
