class MediaType:
    jpeg = {'extension': '.jpeg', 'document_type': 'JPEG images', 'mime': 'image/jpeg'}
    gif = "image/gif"
    csv = "text/csv"
    avi = "video/x-msvideo"
    doc = "application/msword"
    png = "image/png"
    pdf = "application/pdf"
    all_medias = [jpeg, gif, csv, avi, doc, png, pdf]

    def get_type(self, file_name):
        for media in self.all_medias:
            if media['extension'] in file_name:
                return media
            else:
                return "No identified"


if __name__ == '__main__':
    media = MediaType()

    test = media.get_type("test.jpeg")
    print(test)