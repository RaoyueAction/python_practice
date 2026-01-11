import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# --- 1. 使用 torchvision 加载数据 ---
# 定义数据转换：先转成 Tensor（张量），再进行归一化
transform = transforms.Compose([transforms.ToTensor()])

# 下载并加载训练集和测试集
train_dataset = datasets.FashionMNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.FashionMNIST(root='./data', train=False, download=True, transform=transform)

batch_size = 256
train_iter = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_iter = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# --- 2. 定义网络结构 ---
# Flatten() 的作用：把 [256, 1, 28, 28] 的图片压扁成 [256, 784]
net = nn.Sequential(nn.Flatten(), nn.Linear(784, 10))

# 初始化权重
def init_weights(m):
    if type(m) == nn.Linear:
        nn.init.normal_(m.weight, std=0.01)

net.apply(init_weights)

# --- 3. 定义损失函数与优化器 ---
loss = nn.CrossEntropyLoss()
trainer = torch.optim.SGD(net.parameters(), lr=0.1)

# --- 4. 训练循环 ---
num_epochs = 5
print("开始训练...")
for epoch in range(num_epochs):
    net.train() # 将模型设为训练模式
    for X, y in train_iter:
        y_hat = net(X)
        l = loss(y_hat, y)
        
        trainer.zero_grad()
        l.backward()
        trainer.step()
    
    print(f'Epoch {epoch + 1}: 训练完成')

print("所有训练任务已结束！")

def evaluate_accuracy(net, data_iter):
    net.eval() # 切换到评估模式（不更新参数）
    correct = 0
    total = 0
    with torch.no_grad():
        for X, y in data_iter:
            outputs = net(X)
            # outputs.argmax(dim=1) 会返回概率最大的那个类别的索引
            correct += (outputs.argmax(dim=1) == y).sum().item()
            total += y.size(0)
    return correct / total

accuracy = evaluate_accuracy(net, test_iter)
print(f'模型在测试集上的准确率: {accuracy * 100:.2f}%')