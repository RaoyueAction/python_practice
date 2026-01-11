import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import torch


def synthetic_data(w, b, num_examples):
    """生成 y = Xw + b + 噪声"""
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))


def linreg(X, w, b):
    return torch.matmul(X, w) + b


def squared_loss(y_hat, y):
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2


def sgd(params, lr, batch_size):
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()


def train(features, labels, lr=0.03, num_epochs=3, batch_size=10):
    """训练并返回学到的参数 (w, b)"""
    w = torch.normal(0, 0.01, size=(2, 1), requires_grad=True)
    b = torch.zeros(1, requires_grad=True)

    for epoch in range(num_epochs):
        for X, y in zip(features.split(batch_size), labels.split(batch_size)):
            loss = squared_loss(linreg(X, w, b), y)
            loss.sum().backward()
            sgd([w, b], lr, batch_size)

        with torch.no_grad():
            train_l = squared_loss(linreg(features, w, b), labels)
            print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}', flush=True)

    return w, b


def main():
    torch.manual_seed(0)
    print('脚本开始: 生成数据并训练模型', flush=True)

    true_w = torch.tensor([2.0, -3.4])
    true_b = 4.2
    features, labels = synthetic_data(true_w, true_b, 1000)
    print(f'数据形状: features={features.shape}, labels={labels.shape}', flush=True)

    w, b = train(features, labels, lr=0.03, num_epochs=3, batch_size=10)

    print('\n训练完成', flush=True)
    print(f'真实的权重: {true_w.tolist()}, 真实的偏置: {true_b}', flush=True)
    print(f'估计的权重: {w.reshape(-1).detach().numpy().tolist()}', flush=True)
    print(f'估计的偏置: {b.item()}', flush=True)


if __name__ == '__main__':
    import traceback
    try:
        main()
    except Exception as e:
        print('运行时异常:', e, flush=True)
        traceback.print_exc()