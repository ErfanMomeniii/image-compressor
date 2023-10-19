import cv2
import os
import numpy as np
import argparse


def parse_flags():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--decompress", help="compress input file")
    parser.add_argument("-c", "--compress", help="decompress input file")

    args = parser.parse_args()

    if args.compress:
        compress(path=args.compress)
    if args.decompress:
        decompress(path=args.decompress)
    return


def get_eigen(img=[], num=2):
    m = np.mean(img.T, axis=1)
    C = img - m
    v = np.cov(C)
    values, vectors = np.linalg.eig(v)
    p = np.size(vectors, axis=1)
    idx = np.argsort(values)
    idx = idx[::-1]
    vectors = vectors[:, idx]
    if p > num > 0:
        vectors = vectors[:, range(num)]
    return vectors


def get_score(vect=[], img=[]):
    m = np.mean(img.T, axis=1)
    C = img - m
    score = np.dot(vect.T, C)
    return score


def compress(path=""):
    img = cv2.imread(path)
    img = img.astype(float) / 255.0
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    x, y = b.shape

    nx = int(x / 4)

    eigen_b = get_eigen(b, nx)
    score_b = get_score(eigen_b, b)
    m_b = np.mean(b.T, axis=1)

    eigen_g = get_eigen(g, nx)
    score_g = get_score(eigen_g, g)
    m_g = np.mean(g.T, axis=1)

    eigen_r = get_eigen(r, nx)
    score_r = get_score(eigen_r, r)
    m_r = np.mean(r.T, axis=1)

    eigens = np.zeros((x, nx, 3), "float")
    eigens[..., 0] = eigen_b
    eigens[..., 1] = eigen_g
    eigens[..., 2] = eigen_r

    scores = np.zeros((nx, y, 3), "float")
    scores[..., 0] = score_b
    scores[..., 1] = score_g
    scores[..., 2] = score_r

    m = np.zeros((y, 3), "float")
    m[..., 0] = m_b
    m[..., 1] = m_g
    m[..., 2] = m_r

    dest = os.path.basename(path).split('.')[0]

    np.savez_compressed(dest, e=eigens, s=scores, m=m)

    return


def decompress(path=""):
    load = np.load(path)
    eigens = load['e']
    scores = load['s']
    m = load['m']

    eigen_b = eigens[:, :, 0]
    eigen_g = eigens[:, :, 1]
    eigen_r = eigens[:, :, 2]

    score_b = scores[:, :, 0]
    score_g = scores[:, :, 1]
    score_r = scores[:, :, 2]

    m_b = m[:, 0]
    m_g = m[:, 1]
    m_r = m[:, 2]

    x, _ = eigen_b.shape
    _, y = score_b.shape

    rgb_array = np.zeros((x, y, 3), "float")

    rgb_array[..., 0] = np.absolute(np.dot(eigen_b, score_b) + m_b)
    rgb_array[..., 1] = np.absolute(np.dot(eigen_g, score_g) + m_g)
    rgb_array[..., 2] = np.absolute(np.dot(eigen_r, score_r) + m_r)

    dest = os.path.basename(path).split('.')[0]

    normalized_image = (rgb_array - np.min(rgb_array)) / (np.max(rgb_array) - np.min(rgb_array))
    scaled_image = (normalized_image * 255).astype(np.uint8)

    cv2.imwrite(dest + ".jpg", scaled_image)

    return


if __name__ == '__main__':
    parse_flags()
