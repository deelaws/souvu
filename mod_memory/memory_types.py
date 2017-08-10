import enum

class MemoryTypes(enum.Enum):
    VOCABULARY = "vocabulary"
    BOOK_NOTE = "book-note"
    FORMULA   = "formula"
    QUOTE = "quote"
    POEM = "poem"
    BOOK_NAME = "book-name"
    PARAGRAPH = "paragraph"

    @staticmethod
    def get_type_from_string(mtype):
        if "vocabulary" == mtype:
            return MemoryTypes.VOCABULARY
        elif "book-note" == mtype:
            return MemoryTypes.BOOK_NOTE
        elif "formula" == mtype:
            return MemoryTypes.FORMULA
        elif "quote" == mtype:
            return MemoryTypes.QUOTE
        elif "poem" == mtype:
            return MemoryTypes.POEM
        elif "book-name" == mtype:
            return MemoryTypes.BOOK_NAME
        elif "paragraph" == mtype:
            return MemoryTypes.PARAGRAPH
        else:
            return None