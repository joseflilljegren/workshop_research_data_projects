"""
    Image magick is a commandline tool that manipulates images.

    It's CLI and extremely competent.

    In the file below, we envoke a work-flow that processes images using
    image magick.

    Note that ON your system, your commandline tools and python can envoke each
    other. Claude can run python files, and any commandline tools, a commandline
    tool can run a python script, and python can envoke commandline tools (which
    is done here) using the subprocess package.
"""

import subprocess
from pathlib import Path


PTH_INPUT_IMAGES = Path('source_material/gids_directory')
PTH_OUTPUT_IMAGES = Path('source_material/gids_directory_processed')

# File endings that image magick can read and that we want to treat
IMAGE_SUFFIXES = {'.jpg', '.jpeg', '.png', '.tif', '.tiff', '.bmp', '.gif', '.webp'}


def ensure_directory_existance(pth_dir: Path) -> Path:
    """Return input path after having created that path if it did not already exist."""
    pth_dir.mkdir(parents=True, exist_ok=True)
    return pth_dir




def list_images_in_dir(pth_dir) -> list:
    """List convertable images of a directory."""
    out = sorted(
        pth for pth in pth_dir.iterdir()
        if pth.is_file() and pth.suffix.lower() in IMAGE_SUFFIXES
    )
    return out



def preprocess_individual_image(pth_input: Path, pth_output: Path) -> None:
    """Envoke image magick to preprocess an individual image and save it to target."""
    status = 'Failed'
    print(f' Source: {pth_input}')
    print(f' Target: {pth_output}')

    cmd = [
        'magick', str(pth_input),
        '-background', '#ff00ff',
        '-deskew', '75%',
        '-fuzz', '1%',
        '-fill', '#ff00ff',
        '-trim', '+repage',
        '-enhance',
        '-contrast-stretch', '0.5%x0.5%',
        '-colorspace', 'Gray',
        '-sharpen', '0x1',
        '-quality', '93',
        '-verbose',
        str(pth_output)
    ]

    # Run the command. Image magick writes errors to stderr and returns a
    # non-zero exit code when something goes wrong.
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        status = 'OK'
    else:
        print(f' Error: {result.stderr.strip()}')

    print(f' Status: {status}')




def main():
    """Main."""
    # Make sure that directories exist:
    ensure_directory_existance(pth_dir=PTH_INPUT_IMAGES)
    ensure_directory_existance(pth_dir=PTH_OUTPUT_IMAGES)

    # List all images in the source directory
    target_files = list_images_in_dir(pth_dir=PTH_INPUT_IMAGES)

    # Every image in the input directory will be targeted individually
    for pth_img in target_files:
        print(f'Treating: {pth_img.stem}')
        # The file ending of the output decides the format image magick writes
        pth_output = PTH_OUTPUT_IMAGES / f'{pth_img.stem}.jpg'

        # Parse this image
        preprocess_individual_image(pth_input=pth_img, pth_output=pth_output)




if __name__ == "__main__":
    main()