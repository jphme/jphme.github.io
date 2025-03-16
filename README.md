# jphme.github.io
New jph.me website

# Jan Philipp Harries - Personal Website

This repository contains the code for my personal website.

## Image Thumbnail Generator

The website includes a grid of thumbnail images from the `talks` folder. To generate these thumbnails:

### Using Poetry (Recommended)

1. Make sure you have Poetry installed:
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Run the thumbnail generator script:
   ```
   ./generate_thumbnails.sh
   ```
   
   Or manually:
   ```
   poetry install
   poetry run python generate_thumbnails.py
   ```

### Alternative Method (without Poetry)

1. Make sure you have Python 3 installed
2. Install the required Python package:
   ```
   pip install Pillow
   ```
3. Run the thumbnail generator script:
   ```
   python generate_thumbnails.py
   ```

## What the Thumbnail Generator Does

This will:
- Take all images from the `talks` folder
- Create a `thumbnails` folder if it doesn't exist
- Generate optimized thumbnails (300x300px) while maintaining aspect ratio
- Save the thumbnails to the `thumbnails` folder

### Custom Usage

You can also specify custom source and target directories:

```
poetry run python generate_thumbnails.py [source_directory] [target_directory]
```

For example:
```
poetry run python generate_thumbnails.py my_images custom_thumbnails
```

## Website Structure

- `index.html` - Main website file
- `talks/` - Directory containing original images
- `thumbnails/` - Directory containing generated thumbnails
- `generate_thumbnails.py` - Script to generate thumbnails
- `pyproject.toml` - Poetry configuration file
- `generate_thumbnails.sh` - Shell script to run the thumbnail generator with Poetry

## Updating the Image Grid

If you add new images to the `talks` folder:

1. Run the thumbnail generator script again
2. Update the HTML in `index.html` to include the new images in the grid
