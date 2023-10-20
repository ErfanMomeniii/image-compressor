# image-compressor

## Overview
<div align="justify">The image compressor is a lightweight and straightforward tool that is capable of reducing the size of images.It utilizes an algorithm inspired by PCA (Principal Component Analysis) to compress images, resulting in a size reduction of at least 50% compared to the original size.By using this tool, you can effectively save memory and storage space.</div>

## Installation
To use the Image Compressor, follow these steps:
1. clone this repository:
```git
git clone https://github.com/ErfanMomeniii/image-compressor.git
```
2. install the required dependencies:
```pip
pip install -r requirements.txt
```

## Usage
To compress an image, run the following command:
```
python setup.py -c "image.jpg"
```
Replace `image.jpg` with the path of your input image and it will output compressed file like `image.npz`.


To decompress an image from `.npz` file, run the following command:
```
python setup.py -d "image.npz"
```
Like compressing, replace `image.npz` with the path of your compressed file.

## Example

<figure>
    <p align="center" style="text-align: justify; width:50%; height: 50%"><figcaption>Original image</figcaption></p>
    <img src="assets/isfahan-o.jpg" alt="Image Description">
</figure>

<figure>
    <p align="center" style="text-align: justify;width:50%; height: 50%"><figcaption>Decompressed image</figcaption></p>
    <img src="assets/isfahan-d.jpg" alt="Image Description">
</figure>

## Contributing

Contributions are welcome! If you would like to contribute to the Image Compressor project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, feel free to reach out to me at [erfamm5@gmail.com](mailto:erfamm5@gmail.com).
