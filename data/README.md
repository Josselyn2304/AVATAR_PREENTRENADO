# Dataset Directory Structure

The dataset directory should follow a structured format to ensure easy access and usage. The expected structure is as follows:

```
/datasets
    /CelebA-HQ
    /FFHQ
    /...other datasets...
```

## Recommended Datasets

1. **CelebA-HQ**: A high-quality version of the CelebA dataset, which contains celebrity face images.
2. **FFHQ**: The Flickr-Faces-HQ dataset, known for its high-resolution images and diverse subjects.  

## Data Requirements for 512x512 Images

To ensure compatibility with models that expect 512x512 images:
- All images should be resized to 512x512 pixels.
- Maintain the original aspect ratio while cropping if necessary to achieve 512x512 dimension.

## Preprocessing Information

Before using the datasets, ensure you perform the following preprocessing steps:
- **Normalization**: Scale pixel values to be between -1 and 1 or 0 and 1, depending on the model's requirements.
- **Data Augmentation**: Apply techniques such as random cropping, flipping, and rotation to enhance dataset variance.
- **Cleaning**: Remove any corrupted images or anomalies that may hinder model training.