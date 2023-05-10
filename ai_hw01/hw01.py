import numpy as np
X1=[11,86,90,93.5,93,90.63,90,99,106,98.33]
X2=[11,85.5,70,86.5,88.5,82.63,91,88,90,89.67]
X3=[10,77,63.5,58.5,78,69.25,82,73,65,73.33]
X4=[8,82.5,75.5,87.5,82.5,82,75,99,91,88.33]
X5=[11,91,89,88.5,89.75,89.56,105,97,114,105.33]
X6=[11,94.5,89.5,95.5,90.5,92.5,93,116,112,107]
X7=[6,78.25,63.5,62.5,67.25,67.88,94,66,77,79]
X8=[5,86.5,90.5,82.5,0,64.88,85,94,90,89.67]
X9=[11,85,62,63,84.5,73.63,96,95,74,88.33]
X10=[10,89,77.5,90,90.5,86.75,95,105,97,99]
X11=[8,91.25,90.5,88.5,0,67.56,83,83,60,75.33]
X12=[7,70.5,61.5,59,52,60.75,98,95,38,77]
X13=[7,84,0,0,0,21,65,0,0,21.67]
X14=[11,64,9,0,0,18.25,85,48,71,68]
x1=[94]
x2=[89]
x3=[79]
x4=[85]
x5=[95]
x6=[96]
x7=[75]
x8=[75]
x9=[85]
x10=[91]
x11=[76]
x12=[73]
x13=[44]
x14=[57]

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_dev(x):
    return x*(1-x)

def tanh(x):
    return (np.exp(x)- np.exp(-x)) / (np.exp(x)+ np.exp(-x))
def tanh_dev(x):
    return (1-tanh(x)**2)/200 

def mse_loss(y_pred, y_true):
    return ((y_pred - y_true) ** 2).mean()


X = np.array([X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14])
Y = np.array([x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14])/100
x_new = np.array([X1,X2,X3])
result_true = np.array([x1,x2,x3])/100
for j in range(11):
    X[j][0] = X[j][0]/15
    for i in range(1,6) :
       X[j][i] = X[j][i]/100
    for i in range(6,10) :
        X[j][i] = X[j][i]/120
for j in range(3):
    x_new[j][0] = x_new[j][0]/15
    for i in range(1,6) :
        x_new[j][i] = x_new[j][i]/100
    for i in range(6,10) :
        x_new[j][i] = x_new[j][i]/120

#1個神經元(sigmoid)
        
np.random.seed(1)
W1 = 2 * np.random.random((10,1)) - 1


for j in range(10000):
        
    l1_output = sigmoid(np.dot(X, W1))
    
    d_l1_output =(l1_output - Y) * sigmoid_dev(l1_output)
    
    W1 -= 0.1 * X.T.dot(d_l1_output)
print("\n1個神經元(sigmoid)預測值為:")
for i in range(11):
    print(100*l1_output[i])
loss = mse_loss(l1_output, Y).mean()
print("\nMSE:",loss)

l1_output = sigmoid(np.dot(x_new, W1))

y_new = l1_output
loss = mse_loss(y_new, result_true).mean()
print("\n1個神經元(sigmoid)預測值為:")
for i in range(3):
    print(100*y_new[i])

print("\nMSE:",loss)

#1個神經元(tanh)

np.random.seed(1)
W1 = 2 * np.random.random((10,1)) - 1


for j in range(10000):
        
    l1_output = tanh(np.dot(X, W1))

    d_l1_output =(l1_output - Y) * tanh_dev(l1_output)
    
    W1 -= 0.1 * X.T.dot(d_l1_output)
print("\n1個神經元(tanh)測試值為:")
for i in range(11):
    print(100*l1_output[i])
loss = mse_loss(l1_output, Y).mean()
print("\nMSE:",loss)
l1_output = tanh(np.dot(x_new, W1))

y_new = l1_output
loss = mse_loss(y_new, result_true).mean()
print("\n1個神經元(tanh)預測值為:")
for i in range(3):
    print(100*y_new[i])

print("\nMSE:",loss)
 
#2個神經元(sigmoid)

np.random.seed(1)
W1 = 2 * np.random.random((10,2)) - 1
W2 = 2 * np.random.random((2, 1)) - 1

for j in range(10000):
        
    l1_output = sigmoid(np.dot(X, W1))
    l2_output = sigmoid(np.dot(l1_output, W2))


        
    d_l2_output =  (l2_output - Y) * sigmoid_dev(l2_output)
    d_l1_output = d_l2_output.dot(W2.T) * sigmoid_dev(l1_output)

    
    W2 -= 0.1 * l1_output.T.dot(d_l2_output)
    W1 -= 0.1 * X.T.dot(d_l1_output)

print("\n2個神經元(sigmoid)測試值為:")
for i in range(11):
    print(100*l2_output[i])
loss = mse_loss(l2_output, Y).mean()
print("\nMSE:",loss)
l1_output = sigmoid(np.dot(x_new, W1))
l2_output = sigmoid(np.dot(l1_output, W2))
y_new = l2_output
loss = mse_loss(y_new, result_true).mean()

print("\n2個神經元(sigmoid)預測值為:")
for i in range(3):
    print(100*y_new[i])
print("\nMSE:",loss)

#2個神經元(tanh)
np.random.seed(1)
W1 = 2 * np.random.random((10,10)) - 1
W2 = 2 * np.random.random((10, 1)) - 1

for j in range(10000):
        
    l1_output = tanh(np.dot(X, W1))
    l2_output = tanh(np.dot(l1_output, W2))


        
    d_l2_output =  (l2_output - Y) * tanh_dev(l2_output)
    d_l1_output = d_l2_output.dot(W2.T) * tanh_dev(l1_output)

    
    W2 -= 0.1 * l1_output.T.dot(d_l2_output)
    W1 -= 0.1 * X.T.dot(d_l1_output)
print("\n2個神經元(tanh)測試值為:")
for i in range(11):
    print(100*l2_output[i])
loss = mse_loss(l2_output, Y).mean()
print("\nMSE:",loss)
l1_output = tanh(np.dot(x_new, W1))
l2_output =tanh(np.dot(l1_output, W2))
y_new = l2_output
loss = mse_loss(y_new, result_true).mean()

print("\n2個神經元(tanh)預測值為:")
for i in range(3):
    print(100*y_new[i])
print("\nMSE:",loss)

#3個神經元(sigmoid)
np.random.seed(1)
W1 = 2 * np.random.random((10,5)) - 1
W2 = 2 * np.random.random((5, 2)) - 1
W3 = 2 * np.random.random((2, 1)) - 1

for j in range(10000):
        
    l1_output = sigmoid(np.dot(X, W1))
    l2_output = sigmoid(np.dot(l1_output, W2))
    l3_output = sigmoid(np.dot(l2_output, W3))


    d_l3_output =  (l3_output - Y) * sigmoid_dev(l3_output) 
    d_l2_output = d_l3_output.dot(W3.T) * sigmoid_dev(l2_output)
    d_l1_output = d_l2_output.dot(W2.T) * sigmoid_dev(l1_output)

    W3 -= 0.1 * l2_output.T.dot(d_l3_output)
    W2 -= 0.1 * l1_output.T.dot(d_l2_output)
    W1 -= 0.1 * X.T.dot(d_l1_output)
print("\n3個神經元(sigmoid)測試值為:")
for i in range(11):
    print(100*l3_output[i])
loss = mse_loss(l3_output, Y).mean()
print("\nMSE:",loss)
l1_output = sigmoid(np.dot(x_new, W1))
l2_output = sigmoid(np.dot(l1_output, W2))
l3_output = sigmoid(np.dot(l2_output, W3))
y_new = l3_output
loss = mse_loss(y_new, result_true).mean()

print("\n3個神經元(sigmoid)預測值為:")
for i in range(3):
    print(100*y_new[i])
print("\nMSE:",loss)

