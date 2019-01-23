import category as cat


class GameData:

    def __init__(self):
        self.categories = None
        self.difficulties = None
        self._init_categories()
        self._init_difficulties()

    def _init_categories(self):
        self.categories = {}
        self.categories[1] = cat.Category(9, "1. General Knowledge")
        self.categories[2] = cat.Category(10, "2. Entertainment: Books")
        self.categories[3] = cat.Category(11, "3. Entertainment: Film")
        self.categories[4] = cat.Category(12, "4. Entertainment: Music")
        self.categories[5] = cat.Category(13, "5. Entertainment: Musicals & Theatres")
        self.categories[6] = cat.Category(14, "6. Entertainment: Television")
        self.categories[7] = cat.Category(15, "7. Entertainment: Video Games")
        self.categories[8] = cat.Category(16, "8. Entertainment: Board Games")
        self.categories[9] = cat.Category(17, "9. Science & Nature")
        self.categories[10] = cat.Category(18, "10. Science: Computers")
        self.categories[11] = cat.Category(19, "11. Science: Mathematics")
        self.categories[12] = cat.Category(20, "12. Mythology")
        self.categories[13] = cat.Category(21, "13. Sports")
        self.categories[14] = cat.Category(22, "14. Geography")
        self.categories[15] = cat.Category(23, "15. History")
        self.categories[16] = cat.Category(24, "16. Politics")
        self.categories[17] = cat.Category(25, "17. Art")
        self.categories[18] = cat.Category(26, "18. Celebrities")
        self.categories[19] = cat.Category(27, "19. Animals")

    def _init_difficulties(self):
        self.difficulties = {1: "easy", 2: "medium", 3: "hard"}
