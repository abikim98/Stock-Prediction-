#!/usr/bin/env python
# coding: utf-8

# In[7]:


import torch 
import torch.nn as nn


# In[8]:


from dataset import stockDataset
from model import LSTM
from model import RNN
from tqdm import tqdm 
import matplotlib.pyplot as plt


# In[9]:


device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)


# In[ ]:


train_dataloader = torch.utils.data.DataLoader(train_set, batch_size = 20, shuffle = False)
valid_dataloader = torch.utils.data.DataLoader(valid_set, batch_size = len(valid_set), shuffle = False)


# In[ ]:


num_epochs = 100
learning_rate = 0.01

input_dim = 1
hidden_dim = 32
num_layers = 1
output_dim = 1

lstm = LSTM(input_dim, hidden_dim, num_layers, output_dim).to(device)
rnn = RNN(input_dim, hidden_dim, num_layers, output_dim.to(device)
loss_function = torch.nn.MSELoss()
optimizer = torch.optim.Adam(lstm.parameters(), lr = learning_rate)


# In[10]:


def train(model, train_dataloader, optimizer):
    model.train()
    for epoch in train_loader:
        train_loader = tqdm(train_dataloader)
        for data in train_loader:
            x, y = data
            x = x.reshape(x.shape[0], x.shape[1],1).float()
            
            outputs = model(x.to(device))
            optimizer.zero_grad()
            loss = loss_function(outputs, y.float().to(device))
            optimizer.step()
            train_loader.set_description(f"Epoch:{epoch}, loss: {loss.item():.5f}")
        
        losses =[]
        
def valid(model, valid_dataloader, optimizer):
    model.eval()
    for data in valid_dataloader:
        x, y = data
        x = x.reshape(x.shape[0], x.shape[1], -1).float()
        y = y.float()
        with torch.no_grad():
            rnn.eval()
            valid_predict = rnn(x.to(device))
            
            loss = loss_function(valid_predict.cpu(), y)
        print('valid_loss', loss)
        
        data_predict = valid_predict.data.detach().cpu().numpy() 
        plt.plot(data_predict, label="Predicted Data")
        plt.plot(y, label="Actual Data")
        plt.legend()
        plt.show()

