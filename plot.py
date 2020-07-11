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
  
#plt.plot(x, sigmoid, 'r', label = "Sigmoid(x)")
#plt.plot(x, div_sigmoid, 'b', label = "Đạo hàm của Sigmoid(x)")
# plt.plot(x, tanh, 'r', label = "Tanh(x)")
# plt.plot(x, div_tanh, 'b', label = "Đạo hàm của Tanh(x)")
plt.plot(x, relu, 'r', label = "ReLU(x)")
plt.plot(x, div_relu, 'b', label = "Đạo hàm của ReLU(x)")
plt.xlabel("x")
# plt.title('Đồ thị hàm Sigmoid và đạo hàm của hàm Sigmoid')
# plt.title('Đồ thị hàm Tanh và đạo hàm của hàm Tanh')
plt.title('Đồ thị hàm ReLU và đạo hàm của hàm ReLU')
plt.legend()
plt.show() 