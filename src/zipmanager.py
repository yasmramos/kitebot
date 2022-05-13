import pathlib
from zipfile import ZIP_DEFLATED, BadZipFile, ZipFile


class ZipManager(object):

    def __init__(self) -> None:
        self.zip_file = None

    def create_zip(self, zfilename: str, directory: str):
        try:
            dir_name = pathlib.Path(directory)
            with ZipFile(zfilename, "w", ZIP_DEFLATED, compresslevel=9) as archive:
                for file_path in dir_name.rglob("*"):
                    archive.write(
                        file_path, arcname=file_path.relative_to(dir_name))
        except BadZipFile as ex:
            print(ex)
        return archive
