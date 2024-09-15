import numpy as np
from torch.utils.tensorboard import SummaryWriter
from PIL import Image

writer = SummaryWriter("logs")
img_path = "dataset/val/bees/44105569_16720a960c.jpg"
img_PIL = Image.open(img_path)
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)

writer.add_image("train", img_array, 2, dataformats='HWC')
# y = x
for i in range(100):
    writer.add_scalar('y=2x', 3*i, i)

writer.close()