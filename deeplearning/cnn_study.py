import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super(SimpleCNN, self).__init__()
        
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
        
        self.fc1 = nn.Linear(in_features=32 * 8 * 8, out_features=128)
        self.fc2 = nn.Linear(in_features=128, out_features=num_classes)
    
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 32 * 8 * 8)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)

        return x
    
if __name__ == "__main__":
    cnnmodel = SimpleCNN(num_classes=10)
    
    criterion = nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(cnnmodel.parameters(), lr=0.001)

    images = torch.randn(4, 3, 32, 32)
    labels = torch.tensor([0, 1, 2, 3])

    outputs = cnnmodel(images)
    loss = criterion(outputs, labels)

    optimizer.zero_grad()
    loss.backward()

    optimizer.step()

    print("Loss:", loss.item())
    print("Outputs:", outputs)
    print("Model architecture:\n", cnnmodel)
    print("Number of parameters:", sum(p.numel() for p in cnnmodel.parameters() if p.requires_grad))
    total_params = sum(p.numel() for p in cnnmodel.parameters())
    print("Total number of parameters (including non-trainable):", total_params)
 

