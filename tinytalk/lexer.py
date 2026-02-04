"""
═══════════════════════════════════════════════════════════════════════════════
TINYTALK LEXER
Tokenizer for the TinyTalk language

Keywords, operators, literals, identifiers
═══════════════════════════════════════════════════════════════════════════════
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Any
import re


class TokenType(Enum):
    """Token types for TinyTalk."""
    
    # Literals
    NUMBER = auto()
    STRING = auto()
    BOOLEAN = auto()
    NULL = auto()
    
    # Identifiers
    IDENTIFIER = auto()
    
    # Keywords
    LET = auto()
    CONST = auto()
    FN = auto()
    RETURN = auto()
    IF = auto()
    ELSE = auto()
    ELIF = auto()
    FOR = auto()
    WHILE = auto()
    IN = auto()
    BREAK = auto()
    CONTINUE = auto()
    MATCH = auto()
    CASE = auto()
    TYPE = auto()
    STRUCT = auto()
    ENUM = auto()
    IMPL = auto()
    TRAIT = auto()
    IMPORT = auto()
    EXPORT = auto()
    FROM = auto()
    AS = auto()
    PUB = auto()
    MUT = auto()
    ASYNC = auto()
    AWAIT = auto()
    TRY = auto()
    CATCH = auto()
    THROW = auto()
    FIN = auto()
    FINFR = auto()
    
    # Type keywords
    INT = auto()
    FLOAT = auto()
    STR = auto()
    BOOL = auto()
    LIST = auto()
    MAP = auto()
    ANY = auto()
    VOID = auto()
    
    # Operators - Arithmetic
    PLUS = auto()           # +
    MINUS = auto()          # -
    STAR = auto()           # *
    SLASH = auto()          # /
    PERCENT = auto()        # %
    POWER = auto()          # **
    FLOOR_DIV = auto()      # //
    
    # Operators - Comparison
    EQ = auto()             # ==
    NE = auto()             # !=
    LT = auto()             # <
    GT = auto()             # >
    LE = auto()             # <=
    GE = auto()             # >=
    
    # Operators - Logical
    AND = auto()            # and, &&
    OR = auto()             # or, ||
    NOT = auto()            # not, !
    
    # Operators - Bitwise
    BIT_AND = auto()        # &
    BIT_OR = auto()         # |
    BIT_XOR = auto()        # ^
    BIT_NOT = auto()        # ~
    SHL = auto()            # <<
    SHR = auto()            # >>
    
    # Operators - Assignment
    ASSIGN = auto()         # =
    PLUS_EQ = auto()        # +=
    MINUS_EQ = auto()       # -=
    STAR_EQ = auto()        # *=
    SLASH_EQ = auto()       # /=
    PERCENT_EQ = auto()     # %=
    
    # Delimiters
    LPAREN = auto()         # (
    RPAREN = auto()         # )
    LBRACKET = auto()       # [
    RBRACKET = auto()       # ]
    LBRACE = auto()         # {
    RBRACE = auto()         # }
    COMMA = auto()          # ,
    DOT = auto()            # .
    COLON = auto()          # :
    SEMICOLON = auto()      # ;
    ARROW = auto()          # ->
    FAT_ARROW = auto()      # =>
    PIPE = auto()           # |>
    DOUBLE_COLON = auto()   # ::
    QUESTION = auto()       # ?
    AT = auto()             # @
    HASH = auto()           # #
    DOLLAR = auto()         # $
    RANGE = auto()          # ..
    RANGE_INCL = auto()     # ..=
    
    # Special
    NEWLINE = auto()
    EOF = auto()
    ERROR = auto()
    COMMENT = auto()


@dataclass
class Token:
    """A token in the source code."""
    type: TokenType
    value: Any
    line: int
    column: int
    
    def __repr__(self) -> str:
        if self.type in (TokenType.NEWLINE, TokenType.EOF):
            return f"Token({self.type.name})"
        return f"Token({self.type.name}, {self.value!r})"


class Lexer:
    """
    TinyTalk Lexer - Tokenizes source code.
    """
    
    # Keywords mapping
    KEYWORDS = {
        'let': TokenType.LET,
        'const': TokenType.CONST,
        'fn': TokenType.FN,
        'return': TokenType.RETURN,
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'elif': TokenType.ELIF,
        'for': TokenType.FOR,
        'while': TokenType.WHILE,
        'in': TokenType.IN,
        'break': TokenType.BREAK,
        'continue': TokenType.CONTINUE,
        'match': TokenType.MATCH,
        'case': TokenType.CASE,
        'type': TokenType.TYPE,
        'struct': TokenType.STRUCT,
        'enum': TokenType.ENUM,
        'impl': TokenType.IMPL,
        'trait': TokenType.TRAIT,
        'import': TokenType.IMPORT,
        'export': TokenType.EXPORT,
        'from': TokenType.FROM,
        'as': TokenType.AS,
        'pub': TokenType.PUB,
        'mut': TokenType.MUT,
        'async': TokenType.ASYNC,
        'await': TokenType.AWAIT,
        'try': TokenType.TRY,
        'catch': TokenType.CATCH,
        'throw': TokenType.THROW,
        'fin': TokenType.FIN,
        'finfr': TokenType.FINFR,
        'true': TokenType.BOOLEAN,
        'false': TokenType.BOOLEAN,
        'null': TokenType.NULL,
        'nil': TokenType.NULL,
        'and': TokenType.AND,
        'or': TokenType.OR,
        'not': TokenType.NOT,
        # Type keywords
        'int': TokenType.INT,
        'float': TokenType.FLOAT,
        'str': TokenType.STR,
        'bool': TokenType.BOOL,
        'list': TokenType.LIST,
        'map': TokenType.MAP,
        'any': TokenType.ANY,
        'void': TokenType.VOID,
    }
    
    # Multi-character operators (order matters - longer first)
    OPERATORS = [
        ('**', TokenType.POWER),
        ('//', TokenType.FLOOR_DIV),
        ('==', TokenType.EQ),
        ('!=', TokenType.NE),
        ('<=', TokenType.LE),
        ('>=', TokenType.GE),
        ('&&', TokenType.AND),
        ('||', TokenType.OR),
        ('<<', TokenType.SHL),
        ('>>', TokenType.SHR),
        ('+=', TokenType.PLUS_EQ),
        ('-=', TokenType.MINUS_EQ),
        ('*=', TokenType.STAR_EQ),
        ('/=', TokenType.SLASH_EQ),
        ('%=', TokenType.PERCENT_EQ),
        ('->', TokenType.ARROW),
        ('=>', TokenType.FAT_ARROW),
        ('|>', TokenType.PIPE),
        ('::', TokenType.DOUBLE_COLON),
        ('..=', TokenType.RANGE_INCL),
        ('..', TokenType.RANGE),
    ]
    
    # Single-character operators
    SINGLE_OPS = {
        '+': TokenType.PLUS,
        '-': TokenType.MINUS,
        '*': TokenType.STAR,
        '/': TokenType.SLASH,
        '%': TokenType.PERCENT,
        '<': TokenType.LT,
        '>': TokenType.GT,
        '=': TokenType.ASSIGN,
        '&': TokenType.BIT_AND,
        '|': TokenType.BIT_OR,
        '^': TokenType.BIT_XOR,
        '~': TokenType.BIT_NOT,
        '!': TokenType.NOT,
        '(': TokenType.LPAREN,
        ')': TokenType.RPAREN,
        '[': TokenType.LBRACKET,
        ']': TokenType.RBRACKET,
        '{': TokenType.LBRACE,
        '}': TokenType.RBRACE,
        ',': TokenType.COMMA,
        '.': TokenType.DOT,
        ':': TokenType.COLON,
        ';': TokenType.SEMICOLON,
        '?': TokenType.QUESTION,
        '@': TokenType.AT,
        '#': TokenType.HASH,
        '$': TokenType.DOLLAR,
    }
    
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
    
    def tokenize(self) -> List[Token]:
        """Tokenize the entire source."""
        while not self._at_end():
            self._skip_whitespace()
            if self._at_end():
                break
            self._scan_token()
        
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens
    
    def _at_end(self) -> bool:
        return self.pos >= len(self.source)
    
    def _peek(self, offset: int = 0) -> str:
        pos = self.pos + offset
        if pos >= len(self.source):
            return '\0'
        return self.source[pos]
    
    def _advance(self) -> str:
        c = self.source[self.pos]
        self.pos += 1
        if c == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        return c
    
    def _match(self, expected: str) -> bool:
        if self._at_end() or self.source[self.pos] != expected:
            return False
        self._advance()
        return True
    
    def _skip_whitespace(self):
        """Skip whitespace and comments."""
        while not self._at_end():
            c = self._peek()
            
            if c in ' \t\r':
                self._advance()
            elif c == '\n':
                # Track newlines for statement separation
                self._advance()
                self.tokens.append(Token(TokenType.NEWLINE, '\n', self.line - 1, self.column))
            elif c == '/' and self._peek(1) == '/':
                # Single-line comment
                while not self._at_end() and self._peek() != '\n':
                    self._advance()
            elif c == '/' and self._peek(1) == '*':
                # Multi-line comment
                self._advance()  # /
                self._advance()  # *
                while not self._at_end():
                    if self._peek() == '*' and self._peek(1) == '/':
                        self._advance()  # *
                        self._advance()  # /
                        break
                    self._advance()
            elif c == '#':
                # Hash comment (Python/Ruby style)
                while not self._at_end() and self._peek() != '\n':
                    self._advance()
            else:
                break
    
    def _scan_token(self):
        """Scan a single token."""
        start_line = self.line
        start_col = self.column
        
        # Check multi-char operators first
        for op, token_type in self.OPERATORS:
            if self.source[self.pos:self.pos + len(op)] == op:
                for _ in range(len(op)):
                    self._advance()
                self.tokens.append(Token(token_type, op, start_line, start_col))
                return
        
        c = self._peek()
        
        # String literals
        if c in '"\'':
            self._scan_string(c)
            return
        
        # Raw strings
        if c == 'r' and self._peek(1) in '"\'':
            self._advance()  # r
            self._scan_string(self._peek(), raw=True)
            return
        
        # Numbers
        if c.isdigit() or (c == '.' and self._peek(1).isdigit()):
            self._scan_number()
            return
        
        # Identifiers and keywords
        if c.isalpha() or c == '_':
            self._scan_identifier()
            return
        
        # Single-char operators
        if c in self.SINGLE_OPS:
            self._advance()
            self.tokens.append(Token(self.SINGLE_OPS[c], c, start_line, start_col))
            return
        
        # Unknown character
        self._advance()
        self.tokens.append(Token(TokenType.ERROR, c, start_line, start_col))
    
    def _scan_string(self, quote: str, raw: bool = False):
        """Scan a string literal."""
        start_line = self.line
        start_col = self.column
        
        self._advance()  # Opening quote
        
        # Check for triple-quoted string
        triple = False
        if self._peek() == quote and self._peek(1) == quote:
            triple = True
            self._advance()
            self._advance()
        
        value = []
        while not self._at_end():
            c = self._peek()
            
            if triple:
                if c == quote and self._peek(1) == quote and self._peek(2) == quote:
                    self._advance()
                    self._advance()
                    self._advance()
                    break
            else:
                if c == quote:
                    self._advance()
                    break
                if c == '\n' and not triple:
                    # Unterminated string
                    self.tokens.append(Token(TokenType.ERROR, "Unterminated string", start_line, start_col))
                    return
            
            if not raw and c == '\\':
                self._advance()
                if self._at_end():
                    break
                escaped = self._advance()
                escapes = {'n': '\n', 't': '\t', 'r': '\r', '\\': '\\', '"': '"', "'": "'"}
                value.append(escapes.get(escaped, escaped))
            else:
                value.append(self._advance())
        
        self.tokens.append(Token(TokenType.STRING, ''.join(value), start_line, start_col))
    
    def _scan_number(self):
        """Scan a number literal."""
        start_line = self.line
        start_col = self.column
        start_pos = self.pos
        
        # Check for hex, octal, binary
        if self._peek() == '0':
            self._advance()
            if self._peek() in 'xX':
                self._advance()
                while self._peek() in '0123456789abcdefABCDEF_':
                    self._advance()
                value = int(self.source[start_pos:self.pos].replace('_', ''), 16)
                self.tokens.append(Token(TokenType.NUMBER, value, start_line, start_col))
                return
            elif self._peek() in 'oO':
                self._advance()
                while self._peek() in '01234567_':
                    self._advance()
                value = int(self.source[start_pos:self.pos].replace('_', ''), 8)
                self.tokens.append(Token(TokenType.NUMBER, value, start_line, start_col))
                return
            elif self._peek() in 'bB':
                self._advance()
                while self._peek() in '01_':
                    self._advance()
                value = int(self.source[start_pos:self.pos].replace('_', ''), 2)
                self.tokens.append(Token(TokenType.NUMBER, value, start_line, start_col))
                return
        
        # Regular decimal number
        while self._peek().isdigit() or self._peek() == '_':
            self._advance()
        
        # Decimal part
        is_float = False
        if self._peek() == '.' and self._peek(1).isdigit():
            is_float = True
            self._advance()  # .
            while self._peek().isdigit() or self._peek() == '_':
                self._advance()
        
        # Exponent
        if self._peek() in 'eE':
            is_float = True
            self._advance()
            if self._peek() in '+-':
                self._advance()
            while self._peek().isdigit():
                self._advance()
        
        num_str = self.source[start_pos:self.pos].replace('_', '')
        value = float(num_str) if is_float else int(num_str)
        
        self.tokens.append(Token(TokenType.NUMBER, value, start_line, start_col))
    
    def _scan_identifier(self):
        """Scan an identifier or keyword."""
        start_line = self.line
        start_col = self.column
        start_pos = self.pos
        
        while self._peek().isalnum() or self._peek() == '_':
            self._advance()
        
        text = self.source[start_pos:self.pos]
        
        # Check if keyword
        if text in self.KEYWORDS:
            token_type = self.KEYWORDS[text]
            if token_type == TokenType.BOOLEAN:
                value = text == 'true'
            elif token_type == TokenType.NULL:
                value = None
            else:
                value = text
            self.tokens.append(Token(token_type, value, start_line, start_col))
        else:
            self.tokens.append(Token(TokenType.IDENTIFIER, text, start_line, start_col))
