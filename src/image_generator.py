import logging
import math
import os

from PIL import Image

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ImageGridCreator:
    def __init__(self, input_dir: str, output_file: str, max_width: int = 2000, max_height: int = 2000,
                 margin: int = 80) -> None:
        self.input_dir: str = input_dir
        self.output_file: str = output_file
        self.max_width: int = max_width
        self.max_height: int = max_height
        self.margin: int = margin
        self.images: list[str] = []

    def is_image_file(self, filename: str) -> bool:
        image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
        return filename.lower().endswith(image_extensions)

    def check_dirs(self) -> list[str]:
        logger.info(f"Scanning directory {self.input_dir} for images.")
        for root, dirs, files in os.walk(self.input_dir):
            for file in files:
                if self.is_image_file(file):
                    image_path = os.path.join(root, file)
                    self.images.append(image_path)
                    logger.info(f"Found image: {image_path}")

        logger.info(f"Total {len(self.images)} images found.")
        return self.images

    def create_tiff_grid(self) -> None:
        if not self.images:
            logger.error("No images to process. Exiting.")
            return

        num_images: int = len(self.images)
        grid_size: int = int(math.ceil(math.sqrt(num_images)))

        max_thumbnail_width: int = (self.max_width - (grid_size + 1) * self.margin) // grid_size
        max_thumbnail_height: int = (self.max_height - (grid_size + 1) * self.margin) // grid_size
        thumbnail_size: tuple[int, int] = (max_thumbnail_width, max_thumbnail_height)

        thumbnails: list[Image.Image] = []
        for img_path in self.images:
            img = Image.open(img_path)
            img.thumbnail(thumbnail_size)
            thumbnails.append(img)
            logger.info(f"Processed thumbnail for: {img_path}")

        grid_width: int = grid_size * (thumbnail_size[0] + self.margin) + self.margin
        grid_height: int = grid_size * (thumbnail_size[1] + self.margin) + self.margin
        grid_image = Image.new('RGB', (grid_width, grid_height), (255, 255, 255))

        for index, img in enumerate(thumbnails):
            row = index // grid_size
            col = index % grid_size
            x = self.margin + col * (thumbnail_size[0] + self.margin)
            y = self.margin + row * (thumbnail_size[1] + self.margin)
            grid_image.paste(img, (x, y))

        grid_image.save(self.output_file, format='TIFF')
        logger.info(f"TIFF file created at: {self.output_file}")
