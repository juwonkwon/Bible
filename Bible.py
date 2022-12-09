import pip._vendor.requests as requests
import json

class Bible:

    def __init__(self):
        self.response = requests.get("https://raw.githubusercontent.com/thiagobodruk/bible/master/json/en_bbe.json")
        self.bible = json.loads(self.response.content)
        self.book_list = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth", 
        "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", 
        "Esther", "Job", "Psalms", "Proverbs", "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah", 
        "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", 
        "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi", "Matthew", "Mark", "Luke", "John", "Acts",
        "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", 
        "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrew", "James", 
        "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"]
        self.lc_book_list = [book.lower() for book in self.book_list]

    def user_input(self):
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
        print(f"{book_info[0]} {book_info[1]}:{book_info[2]}-{book_info[3]}\n")
        if book_info[3] != 0:
            for i in range(book_info[3] - book_info[2] + 1):
                self.final_verse = self.bible[self.book_list.index(book_info[0])]["chapters"][book_info[1]-1][book_info[2]+i-1]
                print(f"{i+1} {self.final_verse}")
        else:
            self.final_verse = self.bible[self.book_list.index(book_info[0])]["chapters"][book_info[1]-1][book_info[2]-1]
            return f"{self.final_verse}"

