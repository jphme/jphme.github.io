#!/usr/bin/env python3
import os
import sys

from PIL import Image


def create_thumbnails(source_dir, target_dir, thumbnail_size=(300, 300)):
    """
    Create thumbnails for all images in the source directory and save them to the target directory.

    Args:
        source_dir (str): Directory containing the original images
        target_dir (str): Directory where thumbnails will be saved
        thumbnail_size (tuple): Width and height of the thumbnails
    """
    # Create target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created directory: {target_dir}")

    # Get all image files in the source directory
    image_files = [
        f
        for f in os.listdir(source_dir)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))
    ]

    if not image_files:
        print(f"No image files found in {source_dir}")
        return

    print(f"Found {len(image_files)} images to process")

    # Process each image
    for image_file in image_files:
        source_path = os.path.join(source_dir, image_file)
        target_path = os.path.join(target_dir, image_file)

        try:
            # Open the image
            with Image.open(source_path) as img:
                # Convert to RGB if needed (for PNG with transparency)
                if img.mode in ("RGBA", "LA") or (
                    img.mode == "P" and "transparency" in img.info
                ):
                    img = img.convert("RGB")

                # Resize the image while maintaining aspect ratio
                img.thumbnail(thumbnail_size)

                # Save the thumbnail
                img.save(target_path, optimize=True, quality=85)
                print(f"Created thumbnail: {target_path}")

        except Exception as e:
            print(f"Error processing {image_file}: {e}")


def main():
    # Default directories
    source_dir = "talks"
    target_dir = "thumbnails"

    # Allow command-line arguments to override defaults
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    if len(sys.argv) > 2:
        target_dir = sys.argv[2]

    # Create thumbnails
    create_thumbnails(source_dir, target_dir)
    print("Thumbnail generation complete!")


if __name__ == "__main__":
    main()
