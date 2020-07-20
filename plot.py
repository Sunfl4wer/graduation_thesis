import matplotlib.pyplot as plt 
import numpy as np 
import math 

plt.style.use('seaborn-whitegrid')
font = {'size'   : 17}

plt.rc('font', **font)


x = np.linspace(-10, 10, 100) 
# Sigmoid function
sigmoid = 1/(1 + np.exp(-x))
# Divergence of Sigmoid function
div_sigmoid = np.exp(-x)/np.power(1 + np.exp(-x),2)
  
# Tanh function
tanh = 2/(1+np.exp(-2*x)) - 1
# Divergence of tanh function
div_tanh = 4*np.exp(-2*x)/np.power(1 + np.exp(-2*x),2)

# RelU function
relu = np.maximum(0,x)
# Divergence of ReLU function
div_relu = np.sign(x)/2+0.5

x_point = np.linspace(-10,10,5)
# y expected
y = np.array((1,2,3,4,5))
# y predicted
y_predicted = np.array((3,7,4,1,5))
# loss values
j = 0.5*np.power(y-y_predicted,2)

labels = ["Wearing a hardhat", "Not wearing a hardhat", "Wearing a safety vest", "Not wearing a safety vest", "Wearing a mask", "Not wearing a mask"]
m_3_precision = [0.7297297297297297, 0.8783783783783784, 0.9324324324324325, 0.7432432432432432, 0.8175675675675675, 0.3716216216216216]
m_3_recall = [0.8558558558558558, 0.6621621621621622, 0.8513513513513513, 0.7162162162162162, 0.47747747747747743, 0.6486486486486487]
x_pos = np.arange(len(labels))
# plt.plot(x, sigmoid, 'r', label = "Sigmoid(x)")
# plt.plot(x, div_sigmoid, 'b', label = "Đạo hàm của Sigmoid(x)")
# plt.title('Đồ thị hàm Sigmoid và đạo hàm của hàm Sigmoid')
# plt.plot(x, tanh, 'r', label = "Tanh(x)")
# plt.plot(x, div_tanh, 'b', label = "Đạo hàm của Tanh(x)")
# plt.title('Đồ thị hàm Tanh và đạo hàm của hàm Tanh')
# plt.plot(x, relu, 'r', label = "ReLU(x)")
# plt.plot(x, div_relu, 'b', label = "Đạo hàm của ReLU(x)")
# plt.title('Đồ thị hàm ReLU và đạo hàm của hàm ReLU')
plt.plot(x_pos, m_3_precision, '-or', label = "Expected")
plt.xlabel("x")
plt.legend()
plt.show() 