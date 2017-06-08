import enum

class MemoryTypes(enum.Enum):
    VOCABULARY = "vocabulary"
    BOOK_NOTE = "book-note"
    FORMULA   = "formula"
    QUOTE = "quote"
    POEM = "poem"
    BOOK_NAME = "book-name"

    @staticmethod
    def get_type_from_string(mtype):
        if "vocabulary" == mtype:
            return MemoryTypes.VOCABULARY
        elif "book-note" == mtype:
            return MemoryTypes.BOOK_NOTE
        elif "formula" == mtype:
            return MemoryTypes.FORMULA
        else:
            return None