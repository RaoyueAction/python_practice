import torch
from torch.utils import data
from torch import nn

# --- 1. 准备数据 (依然使用之前的生成函数) ---
def synthetic_data(w, b, num_examples):
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y

true_w = torch.tensor([2, -3.4])
true_b = 4.2
features, labels = synthetic_data(true_w, true_b, 1000)

# --- 2. 使用 API 读取数据 ---
def load_array(data_arrays, batch_size, is_train=True):
    """构造一个 PyTorch 数据迭代器"""
    dataset = data.TensorDataset(*data_arrays) # 把特征和标签打包
    return data.DataLoader(dataset, batch_size, shuffle=is_train) # 自动打乱并分批

batch_size = 10
data_iter = load_array((features, labels), batch_size)

# --- 3. 定义模型、初始化参数 ---
# Sequential 就像一个容器，按顺序把层串起来
net = nn.Sequential(nn.Linear(2, 1)) 

# 初始化参数：net[0] 表示访问第一层（Linear层）
net[0].weight.data.normal_(0, 0.01)
net[0].bias.data.fill_(0)

# --- 4. 定义损失函数和优化器 (API 的精髓) ---
loss = nn.MSELoss() # 均方误差 API
trainer = torch.optim.SGD(net.parameters(), lr=0.03) # 随机梯度下降 API

# --- 5. 训练循环 ---
num_epochs = 3
for epoch in range(num_epochs):
    for X, y in data_iter:
        l = loss(net(X), y)     # 算损失
        trainer.zero_grad()      # 清空之前的梯度（必须做！）
        l.backward()            # 反向传播，算梯度
        trainer.step()          # 更新模型参数（自动根据 lr 更新）
    
    # 打印进度
    l_final = loss(net(features), labels)
    print(f'epoch {epoch + 1}, loss {l_final:f}')