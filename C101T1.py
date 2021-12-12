import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    access_token = 'sl.A-AzZSbLmCsMzrqDOELNHl_dI7VCKDP3XHB2iK-0Rici5J-i9DvH3anQlu-subKYezm1egQM3E4jF9_xdgAPtCLlcCz8wegLO2-axnxDTnJDSre7014hnKvSIDERXDcTzGChGInlDyr2'
    transferData = TransferData(access_token)

    file_from = 'E:/python/WHJ/py'
    file_to = '/test_dropbox/py'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)


if __name__ == '__main__':
    main()