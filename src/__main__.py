from config import configs

from src.image_generator import ImageGridCreator


def main() -> None:

    image_grid_creator = ImageGridCreator(
        input_dir=configs.DIR_CONFIG.FILES_DIR,
        output_file=configs.DIR_CONFIG.RESULT_TIF
    )
    image_grid_creator.check_dirs()
    image_grid_creator.create_tiff_grid()


if __name__ == "__main__":
    main()