import datetime


class Photo:
    def __init__(self, name, created_date):
        self.name = name
        self.created_date = created_date

    def __lt__(self, other):
        if self.name == other.name:
            return self.created_date < other.created_date
        return self.name < other.name

    # to instruct how to compare two objects (==)
    def __eq__(self, other):
        if isinstance(other, Photo):
            return self.name == other.name and self.created_date == other.created_date
        return False

    # for operator !=
    def __ne__(self, other):
        return not self.__eq__(other)


gallery = [Photo('Cat and Me', datetime.datetime(2020, 5, 17)),
           Photo('Yummyyyy!!!', datetime.datetime(2021, 8, 4)),
           Photo('Cooool', datetime.datetime(2013, 6, 25)),
           Photo('Cooool', datetime.datetime(2016, 10, 24)),
           Photo('Cooool', datetime.datetime(2013, 6, 25)),
           Photo('Cat and Me', datetime.datetime(2020, 5, 17))]
sorted_gallery = sorted(gallery)
duplicated_photo_list = []

for index in range(1, len(sorted_gallery)):
    # compare a photo and the previous one of it in the list
    # check, if the founded duplicated photo have been added in the duplicated_photo_list or not
    if(sorted_gallery[index] == sorted_gallery[index-1]
            and (len(duplicated_photo_list) == 0 or sorted_gallery[index] != duplicated_photo_list[-1])):
        duplicated_photo_list.append(sorted_gallery[index])

for photo in duplicated_photo_list:
    print(photo.name, " ", photo.created_date)
