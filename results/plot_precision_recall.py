import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

plt.rcParams.update({'font.size': 17})

iteration = [0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000]

precision = [0.0,0.81,0.89,0.89,0.88,0.87,0.87,0.86,0.88,0.8,0.86,0.86,0.85]

recall = [0.0,0.55,0.59,0.66,0.67,0.68,0.68,0.70,0.71,0.71,0.74,0.72,0.72]

mAP = [0.0, 0.680156, 0.776576, 0.794934, 0.816612, 0.809256, 0.814943, 0.811121, 0.824844, 0.788236, 0.832291, 0.825616, 0.811770]

plt.plot(iteration, precision,'-or', label = "precision")
plt.plot(iteration, recall,'-ob', label = "recall")
plt.plot(iteration, mAP,'--og', label = "mean average precision")
plt.xlabel('iterations')
plt.title('Precision, Recall and Mean Average Precision of validation dataset during training')
plt.legend()
plt.show()