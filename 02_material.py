"""
    The directories `data` and `source_material` do not contain anything when
    you pull this repo. They are included in the .gitignore so that their content
    is not handeled via git.

    It is not good practice to push images or large datasets to git which is build
    for version tracking text-files on a per-line basis. Binary files (like many
    image formats) are ill suited for this as smaller or partial changes will cause
    git to update and track the entire image as is.

    This workshop does use some data and source material as examples. The code in 
    this file downloads and positions this data on your machine.

    Read the code and see how well you understand it.
"""

# All of these are part of the "standar python library" - They come with every python distribution
import subprocess
import zipfile
from pathlib import Path



# These are the files we'd like to download and place
DATA_DOWNLOADS = [
    {
        'name': 'data/',
        'url': 'ulown.lilljegren.com/fls/issuers.zip',
    },
    {
        'name': 'source_material/',
        'url': 'ulown.lilljegren.com/fls/gids_directory.zip',
    }
]





def download_remote_data(url, target_directory: Path):
    """Fetch a zipped data and install content into specific directory."""

    # Make sure the target directory exists (it is gitignored, so it may not)
    target_directory.mkdir(parents=True, exist_ok=True)

    # Use the target directory as a temporary cache for the zip-file
    pth_zip = target_directory / Path(url).name

    # Download with curl:
    #   -L  follow redirects
    #   -f  fail on HTTP errors (e.g. 404) instead of saving the error page
    #   -sS silent, but still show errors
    #   -o  write output to this file
    subprocess.run(
        ['curl', '-L', '-f', '-sS', '-o', str(pth_zip), url],
        check=True,
    )

    # Expand the content of the zip-file into the target directory,
    # skipping the `__MACOSX/` metadata that zip-files made on a Mac often contain
    with zipfile.ZipFile(pth_zip) as zf:
        members = [m for m in zf.namelist() if not m.startswith('__MACOSX/')]
        zf.extractall(target_directory, members=members)

    # Clean up: remove the downloaded zip-file
    pth_zip.unlink()





def main():
    """Main."""
    for data_download in DATA_DOWNLOADS:
        pth_dir = Path(data_download['name'])
        url_remote = data_download['url']

        # Verbose
        print(f'Downloading and placing `{pth_dir.stem}`')

        # Fetch data
        download_remote_data(url=url_remote, target_directory=pth_dir)




if __name__ == "__main__":
    main()