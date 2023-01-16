
import nni
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor


import torch.utils.data
from torch import nn, optim
from torch.nn import functional as F
from torchvision import datasets, transforms
from torchvision.utils import save_image

params = {
    'features1': 500,
    'features2': 10,
    'lr': 0.001,
    'epsilon': 1e-07,
}

optimized_params = nni.get_next_parameter()
params.update(optimized_params)
print(params)

class Config:
    batch_size = 128
    epochs = 10
    no_cuda = False
    seed = 1
    log_interval = 10

args = Config()
args.cuda = not args.no_cuda and torch.cuda.is_available()
torch.manual_seed(args.seed)

kwargs = {'num_workers': 1, 'pin_memory': True} if args.cuda else {}


batch_size = 64

train_loader = torch.utils.data.DataLoader(datasets.MNIST('../data',
                                                          train=True, 
                                                          download=True,
                                                          transform=transforms.ToTensor()),
                                           batch_size=args.batch_size, shuffle=True, **kwargs)
test_loader = torch.utils.data.DataLoader(datasets.MNIST('../data',
                                                         train=False,
                                                         transform=transforms.ToTensor()),
                                          batch_size=args.batch_size, shuffle=True, **kwargs)

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")



class VAE(nn.Module):
    def __init__(self):
        super(VAE, self).__init__()
        self.fc1 = nn.Linear(784, params['features1'])
        self.fc21 = nn.Linear(params['features1'], params['features2'])
        self.fc22 = nn.Linear(params['features1'], params['features2'])
        self.fc3 = nn.Linear(params['features2'], params['features1'])
        self.fc4 = nn.Linear(params['features1'], 784)
        self.relu1 = torch.nn.ReLU6()
        self.relu2 = torch.nn.ReLU6()

    def encode(self, x):
        h1 = self.relu1(self.fc1(x))
        return self.fc21(h1), self.fc22(h1)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5*logvar)
        eps = torch.randn_like(std)
        return mu + eps*std

    def decode(self, z):
        h3 = self.relu2(self.fc3(z))
        return torch.sigmoid(self.fc4(h3))

    def forward(self, x):
        mu, logvar = self.encode(x.view(-1, 784))
        z = self.reparameterize(mu, logvar)
        return self.decode(z), mu, logvar




# Reconstruction + KL divergence losses summed over all elements and batch
def loss_function(recon_x, x, mu, logvar):
    BCE = F.binary_cross_entropy(recon_x, x.view(-1, 784), reduction='sum')
    KLD = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())

    return BCE + KLD


def train(epoch):
    model.train()
    train_loss = 0
    for batch_idx, (data, _) in enumerate(train_loader):
        data = data.to(device)
        optimizer.zero_grad()
        recon_batch, mu, logvar = model(data)
        loss = loss_function(recon_batch, data, mu, logvar)
        loss.backward()
        train_loss += loss.item()
        optimizer.step()
        if batch_idx % args.log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader),
                loss.item() / len(data)))

    print('====> Epoch: {} Average loss: {:.4f}'.format(
          epoch, train_loss / len(train_loader.dataset)))


def test(epoch):
    model.eval()
    test_loss = 0
    with torch.no_grad():
        for i, (data, _) in enumerate(test_loader):
            data = data.to(device)
            recon_batch, mu, logvar = model(data)
            test_loss += loss_function(recon_batch, data, mu, logvar).item()
            if i == 0:
                n = min(data.size(0), 8)
                comparison = torch.cat([data[:n],
                                      recon_batch.view(args.batch_size, 1, 28, 28)[:n]])
                save_image(comparison.cpu(),
                         'reconstruction_' + str(epoch) + '.png', nrow=n)

    test_loss /= len(test_loader.dataset)
    print('====> Test set loss: {:.4f}'.format(test_loss))
    return test_loss
    


model = VAE().to(device)
optimizer = optim.Adam(model.parameters(), lr=params['lr'],eps= params['epsilon'])


for epoch in range(1, args.epochs + 1):
    train(epoch)
    loss = test(epoch)
    nni.report_intermediate_result(loss)
    with torch.no_grad():
        sample = torch.randn(64, params['features2']).to(device)
        sample = model.decode(sample).cpu()
        save_image(sample.view(64, 1, 28, 28),
                    'sample_' + str(epoch) + '.png')
nni.report_final_result(loss)
            




