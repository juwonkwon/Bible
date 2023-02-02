import pip._vendor.requests as requests
import json


class DbNode:
    def __init__(self, score, book, chapter, verse):
        self.score = score
        self.next = None
        self.prev = None
        self.book = book
        self.chapter = chapter
        self.verse = verse


class DbLinkedList:
    def __init__(self, emotion):
        self.head = None
        self.tail = None
        self.size = 0
        self.emotion = emotion

    # iterate through list until you find node < tempNode, reassign pointers
    def insert(self, score, book, chapter, verse):
        tempNode = DbNode(score, book, chapter, verse)
        walker = self.head
        if self.size == 0:
            self.head = tempNode
            self.tail = tempNode
            self.size = self.size + 1
        elif self.head.score < tempNode.score:
            tempNode.next = self.head
            tempNode.next.prev = tempNode
            self.head = tempNode
        else:
            walker = self.head

            while ((walker.next is not None) and
                   (walker.next.score < tempNode.score)):
                walker = walker.next

            tempNode.next = walker.next

            if walker.next is not None:
                tempNode.next.prev = tempNode

            walker.next = tempNode
            tempNode.prev = walker

            current = self.head
            while current.next != None:
                current = current.next
            self.tail = current
            self.size = self.size + 1
            if self.size > 5:
                self.tail = self.tail.prev
                self.tail.next = None
                self.size = self.size - 1

    def toPrintReady(self):
        walker = self.head
        array = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        i = 0
        while i < 5:
            array[i] = [walker.book, walker.chapter, walker.verse]
            print(array[i])
            i = i + 1
            walker = walker.next
        return array


class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None
        self.book = 0
        self.chapter = 0

    def setBook(self, book):
        self.book = book

    def setChapter(self, chapter):
        self.chapter = chapter

    def getBook(self):
        return self.book

    def getChapter(self):
        return self.chapter


class RBTree:
    def __init__(self, emotion):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
        self.emotion = emotion

    def insert(self, val):
        # Ordinary Binary Search Insertion
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # new node must be red

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

            # Set the parent and insert the new node
        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

            # Fix the tree
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

        # rotate left at node x

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

        # rotate right at node x

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # CREATE HEIGHT METHOD
    # DEFINE SPECTRUM METHODS USING RANDOM LIBRARY


class Bible:

    def __init__(self):
        # initializes book names, the entirety of the bible
        self.response = requests.get("https://raw.githubusercontent.com/thiagobodruk/bible/master/json/en_bbe.json")
        self.bible = json.loads(self.response.content)
        self.book_list = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth",
                          "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra",
                          "Nehemiah",
                          "Esther", "Job", "Psalms", "Proverbs", "Ecclesiastes", "Song of Solomon", "Isaiah",
                          "Jeremiah",
                          "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah",
                          "Nahum",
                          "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi", "Matthew", "Mark", "Luke", "John",
                          "Acts",
                          "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians",
                          "Colossians",
                          "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrew",
                          "James",
                          "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"]
        self.lc_book_list = [book.lower() for book in self.book_list]
        self.emotion_lst = []
        self.emotion_list = ["Happy", "Hope", "Humility", "Sadness", "Fear", "Disgust", "Anger"]
        self.names_of_God = ['God', 'Jesus', 'Holy Spirit', 'Lord', 'Father', 'Son', 'Savior']
        self.lc_book_list = [book.lower() for book in self.book_list]
        self.names_of_God = ['God', 'Jesus', 'Holy Spirit', 'Lord', 'Father', 'Son', 'Savior']
        self.tree_list = [RBTree('happy'), RBTree('hope'), RBTree('humility'), RBTree('sadness'), RBTree('fear'),
                          RBTree('disgust'), RBTree('anger')]

        self.DbArr = [DbLinkedList("happy"), DbLinkedList("hope"), DbLinkedList("humility"), DbLinkedList("sadness"),
                      DbLinkedList("fear"), DbLinkedList("disgust"), DbLinkedList("anger")]

    def open_file(self, file):
        try:
            file = open(file, mode='r')
            emotions = []
            for r in file:
                x = r.strip().split(',')
                emotion_lst = [i.lower() for i in x if i.strip()]
                emotions.append(emotion_lst)
        except:
            print("Can't find file!")
        self.emotion_lst = emotions
        return emotions

    def hasEmotion(self, chapter):
        # Happiness, Hope, Humility, Sadness, Fear, Disgust, Anger
        counters = [0, 0, 0, 0, 0, 0, 0]
        i = 0
        x = 0
        name = False
        for name in self.names_of_God:
            if name in chapter:
                name = True
        for emotions in self.emotion_lst:
            for emotion in emotions:
                counter = chapter.count(emotion)
                x = x + counter
            if name:
                counters[i] = counters[i] + x * 1.25
            else:
                counters[i] = counters[i] + x
            i += 1
            x = 0
        return counters

    def hasEmotion(self, verses):
        # Happiness, Hope, Humility, Sadness, Fear, Disgust, Anger
        counters = [0, 0, 0, 0, 0, 0, 0]
        i = 0
        x = 0
        name = False
        for name in self.names_of_God:
            if name in verses:
                name = True
        for emotions in self.emotion_lst:
            for emotion in emotions:
                counter = verses.count(emotion)
                x = x + counter
            if name:
                counters[i] = counters[i] + x * 1.25
            else:
                counters[i] = counters[i] + x
            i += 1
            x = 0
        return counters

    def treeCreation(self):
        bookC = 0
        chC = 1
        for books in self.bible:
            bookC = bookC + 1
            chC = 1
            for chapters in books:
                chC = chC + 1
                if self.hasEmotion(chapters)[0] != 0:
                    tempNode = RBNode(self.hasEmotion(chapters)[0])
                    tempNode.setBook(bookC)
                    tempNode.setChapter(chC)
                    self.happy.insert(tempNode)
                if self.hasEmotion(chapters)[1] != 0:
                    tempNode = RBNode(self.hasEmotion(chapters)[1])
                    tempNode.setBook(bookC)
                    tempNode.setChapter(chC)
                    self.hope.insert(tempNode)
                if self.hasEmotion(chapters)[2] != 0:
                    tempNode = RBNode(self.hasEmotion(chapters)[2])
                    tempNode.setBook(bookC)
                    tempNode.setChapter(chC)
                    self.contempt.insert(tempNode)
                if self.hasEmotion(chapters)[3] != 0:
                    tempNode = RBNode(self.hasEmotion(chapters)[3])
                    tempNode.setBook(bookC)
                    tempNode.setChapter(chC)
                    self.sadness.insert(tempNode)
                if self.hasEmotion(chapters)[4] != 0:
                    tempNode = RBNode(self.hasEmotion(chapters)[4])
                    tempNode.setBook(bookC)
                    tempNode.setChapter(chC)
                    self.fear.insert(tempNode)
                if self.hasEmotion(chapters)[5] != 0:
                    tempNode = RBNode(self.hasEmotion(chapters)[5])
                    tempNode.setBook(bookC)
                    tempNode.setChapter(chC)
                    self.digust.insert(tempNode)
                if self.hasEmotion(chapters)[6] != 0:
                    tempNode = RBNode(self.hasEmotion(chapters)[6])
                    tempNode.setBook(bookC)
                    tempNode.setChapter(chC)
                    self.anger.insert(tempNode)

    def scoreBoardCreation(self):
        bookC = 0
        chC = 0
        vC = 0
        for books in self.bible:

            chC = 0
            for one, book in books.items():
                for chapter in book:

                    vC = 0
                    for verse in chapter:
                        for i in range(0, 7):
                            while self.DbArr[i].size < 5:
                                self.DbArr[i].insert(self.hasEmotion(verse)[i], bookC, chC, vC)
                            if self.DbArr[i].tail.score < self.hasEmotion(verse)[i] and self.DbArr[i].size == 5:
                                self.DbArr[i].insert(self.hasEmotion(verse)[i], bookC, chC, vC)
                        vC = vC + 1
                    chC = chC + 1
            bookC = bookC + 1

    # if in top 5 happy, put in the scoreboard (score, bookC, chC, vC)

    # conditional statements to find which is the highest counter,
    # returns the string “emotion(i.e happiness)” for whichever counter wins, and will return string
    # Happiness, Hope, Contempt , Sadness, Fear, Disgust, Anger

    def printScoreBoard(self, emotion):
        for dblist in self.DbArr:
            if dblist.emotion == emotion:
                arr = dblist.toPrintReady()
                for elem in arr:

                    verse = self.bible[elem[0]]["chapters"][elem[1]-2][elem[2]]
                    print(verse + "\n")

    def user_input(self):
        # asks for user input
        self.book = (input("What book of the Bible do you want? Press only enter to exit.") or exit())
        if self.book.lower() not in self.lc_book_list:
            self.book = input("Please input the right book name. Press only enter to exit.") or exit()
        self.chapter_pos = self.lc_book_list.index(self.book)
        self.chapter = int(input("What chapter do you want?"))
        self.verse = int(input("What verse do you want to start?"))
        self.end_verse = int(input("What verse do you want to end on? If nothing, enter zero."))
        while self.end_verse != 0 and self.end_verse <= self.verse:
            self.end_verse = int(input("That is an invalid index, what is the ending verse? If nothing, enter zero."))
        return self.book_list[self.chapter_pos], self.chapter, self.verse, self.end_verse

    def search(self, book_info):
        if book_info[3] != 0:
            for i in range(book_info[3] - book_info[2] + 1):
                self.final_verse = self.bible[self.book_list.index(book_info[0])]["chapters"][book_info[1] - 1][
                    book_info[2] + i - 1]
                print(f"{book_info[0]} {book_info[1]}:{book_info[2]}-{book_info[3]}")
                print(f"{i + 1} {self.final_verse}")
        else:
            self.final_verse = self.bible[self.book_list.index(book_info[0])]["chapters"][book_info[1] - 1][
                book_info[2] - 1]
            print(f"{book_info[0]} {book_info[1]}:{book_info[2]}'")
            print(f"{self.final_verse}")
