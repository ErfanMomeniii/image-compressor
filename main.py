import cv2
import numpy as np


def compress(path=""):
    img = cv2.imread('isfahan.jpg')
    img = img.astype(np.float64)
    img /= 255.0

    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    nr = r
    nb = b
    ng = g
    i = 0
    j = 0

    should_clear = []
    while i < len(r):
        while j < len(r[i]):
            print(i, j)
            if (i + 3 > len(r)) or (j + 3) > len(r[i]):
                nr[i][j] = r[i][j]
                j += 1
            else:
                e = r[i:i + 3, j:j + 3]
                m = np.mean(np.array(e).reshape(1, 9), axis=1)
                e = e - m
                cov = np.cov(e.T)
                values, vectors = np.linalg.eig(cov)
                p = np.size(vectors, axis=1)
                idx = np.argsort(values)
                idx = idx[::-1]
                vectors = vectors[:, idx]
                values = values[idx]
                num_PC = 2
                if p > num_PC > 0:
                    vectors = vectors[:, range(num_PC)]
                    vectors = vectors.astype(float)
                score = np.dot(vectors.T, e) + m
                score = np.uint8(np.absolute(score))
                nr[i:i + 2, j:j + 3] = score
                if j == 0:
                    should_clear.append(i + 2)
                nr[i + 2, j] = -1
                nr[i + 2, j + 1] = -1
                nr[i + 2, j + 2] = -1
                j += 2
        i += 2
        j = 0
    i = 0
    j = 0

    while i < len(g):
        while j < len(g[i]):
            if (i + 3 > len(g)) or (j + 3) > len(g[i]):
                ng[i][j] = g[i][j]
                j += 1
            else:
                e = g[i:i + 3, j:j + 3]
                m = np.mean(np.array(e).reshape(1, 9), axis=1)
                e = e - m
                cov = np.cov(e.T)
                values, vectors = np.linalg.eig(cov)
                p = np.size(vectors, axis=1)
                idx = np.argsort(values)
                idx = idx[::-1]
                vectors = vectors[:, idx]
                values = values[idx]
                num_PC = 2
                if p > num_PC > 0:
                    vectors = vectors[:, range(num_PC)]
                    vectors = vectors.astype(float)
                score = np.dot(vectors.T, e) + m
                score = np.uint8(np.absolute(score))
                ng[i:i + 2, j:j + 3] = score
                ng[i + 2, j] = -1
                ng[i + 2, j + 1] = -1
                ng[i + 2, j + 2] = -1
                j += 2
        i += 2
        j = 0
    i = 0
    j = 0
    while i < len(b):
        while j < len(b[i]):
            if (i + 3 > len(b)) or (j + 3) > len(b[i]):
                nb[i][j] = b[i][j]
                j += 1
            else:
                e = r[i:i + 3, j:j + 3]
                m = np.mean(np.array(e).reshape(1, 9), axis=1)
                e = e - m
                cov = np.cov(e.T)
                values, vectors = np.linalg.eig(cov)
                p = np.size(vectors, axis=1)
                idx = np.argsort(values)
                idx = idx[::-1]
                vectors = vectors[:, idx]
                values = values[idx]
                num_PC = 2
                if p > num_PC > 0:
                    vectors = vectors[:, range(num_PC)]
                    vectors = vectors.astype(float)
                score = np.dot(vectors.T, e) + m
                score = np.uint8(np.absolute(score))
                nb[i:i + 2, j:j + 3] = score
                nb[i + 2, j] = -1
                nb[i + 2, j + 1] = -1
                nb[i + 2, j + 2] = -1
                j += 2
        i += 2
        j = 0
    dp = img
    dp[:, :, 0] = nb
    dp[:, :, 1] = ng
    dp[:, :, 2] = nr
    print(should_clear)
    cv2.imshow("compressed", dp)
    cv2.waitKey(0)

compress()
