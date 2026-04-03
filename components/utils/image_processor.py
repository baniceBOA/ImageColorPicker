import os
import shutil
from PIL import Image as PILImage

class ImageProcessor:
    @staticmethod
    def prepare_for_display(input_path, cache_dir):
        """
        Compresses and standardizes an image for mobile GPU rendering.
        Strictly uses Pillow 8.4.0 constants.
        """
        if not input_path or not os.path.exists(input_path):
            return None

        # 1. Ensure cache directory exists
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

        # Generate a unique name based on the original to avoid cache collisions
        output_name = f"display_{os.path.basename(input_path)}"
        output_path = os.path.join(cache_dir, output_name)

        try:
            with PILImage.open(input_path) as img:
                # Fix for 'Black Background': Always convert to RGB
                # This handles PNG transparency and Palette-based images
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                # 2. Resize using Pillow 8.4.0 Legacy Constant
                # 1024px is the 'sweet spot' for mobile texture memory
                img.thumbnail((1024, 1024), resample=PILImage.LANCZOS)
                
                # 3. Save as optimized JPEG
                img.save(output_path, "JPEG", quality=85, optimize=True)
                
            return output_path
        except Exception as e:
            print(f"ImageProcessor Error: {e}")
            return None
    @staticmethod
    def clear_cache(cache_dir):
        """
        Deletes the entire cache directory to free up space on app close.
        """
        try:
            if os.path.exists(cache_dir):
                # Deletes the folder and all processed JPEGs inside
                shutil.rmtree(cache_dir)
                print(f"Cache cleared: {cache_dir}")
        except Exception as e:
            print(f"Failed to clear cache: {e}")
