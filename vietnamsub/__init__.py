class vietnamlanguage():
    def sayhi(self):
        random_list = ["Địt mẹ mày",
                       "Chào em, anh đứng đây từ chiều"]
        return __import__("random").choice(random_list)
    def saybye(self):
        random_list = ["Nhớ mặt tao đấy"]
        return __import__("random").choice(random_list)
