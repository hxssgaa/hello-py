import tensorflow as tf
import torch
import numpy as np


def main():
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    x = np.array(list(range(200)))
    x_t = torch.tensor(x, dtype=torch.float32, device=device)
    print(x_t ** 2)


if __name__ == "__main__":
    main()
