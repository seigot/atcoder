# h: y index
# w: x index
# W: width
def conv2dto1d(h,w):
    return h * W + w
def conv1dto2d(idx):
    h = idx // W
    w = idx % W
    return h, w
