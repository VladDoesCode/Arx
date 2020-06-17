import ctypes
import enum


class _COORD(ctypes.Structure):
    _fields_ = [('X', ctypes.c_ushort),
                ('Y', ctypes.c_ushort)]

    def __repr__(self):
        return f"win32<{self.X}, {self.Y}>"


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __to_win32_COORD(self):
        return _COORD(self.x, self.y)

    def __repr__(self):
        return f"<{self.x}, {self.y}>"

    @staticmethod
    def __from_win32_COORD(coord):
        return Vector2D(coord.X, coord.Y)


class _SMALL_RECT(ctypes.Structure):
    _fields_ = [('Left', ctypes.c_ushort),
                ('Top', ctypes.c_ushort),
                ('Right', ctypes.c_ushort),
                ('Bottom', ctypes.c_ushort)]


class Rectangle:
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def __to_win32_SMALL_RECT(self):
        return _SMALL_RECT(self.left, self.top, self.right, self.bottom)

    def __repr__(self):
        return f"Rectangle<left:{self.left}, top:{self.top}, right:{self.right}, bottom:{self.bottom}>"

    @staticmethod
    def __from_win32_SMALL_RECT(small_rect):
        return Rectangle(small_rect.Left, small_rect.Top, small_rect.Right, small_rect.Bottom)


class _CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    _fields_ = [('dwSize', _COORD),
                ('dwCursorPosition', _COORD),
                ('wAttributes', ctypes.c_ushort),
                ('srWindow', _SMALL_RECT),
                ('dwMaximumWindowSize', _COORD)]

    def __repr__(self):
        return f"dwCursorPosition: {self.dwCursorPosition}"


class ConsoleScreenInformation:
    def __init__(self, size: Vector2D, cursor_position: Vector2D, window_rectangle: Rectangle, maximum_window_size: Vector2D):
        self.size = size
        self.cursor_position = cursor_position
        self.window_rectangle = window_rectangle
        self.maximum_window_size = maximum_window_size

    def __to_win32_CONSOLE_SCREEN_BUFFER_INFO(self, attributes):
        return _CONSOLE_SCREEN_BUFFER_INFO(self.size, self.cursor_position, attributes, self.window_rectangle, self.maximum_window_size)

    def __repr__(self):
        return f"ConsoleScreenInformation<size:{self.size}, cursor_position:{self.cursor_position}, window_rectangle:{self.window_rectangle}, maximum_window_size:{self.maximum_window_size}>"

    @staticmethod
    def __from_win32_CONSOLE_SCREEN_BUFFER_INFO(info):
        return ConsoleScreenInformation(Vector2D._Vector2D__from_win32_COORD(info.dwSize),
                                        Vector2D._Vector2D__from_win32_COORD(
                                            info.dwCursorPosition),
                                        Rectangle._Rectangle__from_win32_SMALL_RECT(
                                            info.srWindow),
                                        Vector2D._Vector2D__from_win32_COORD(info.dwMaximumWindowSize))


class _CONSOLE_CURSOR_INFO(ctypes.Structure):
    _fields_ = [('dwSize', ctypes.c_ulong),
                ('bVisible', ctypes.c_int)]

    def __repr__(self):
        return f"win32<{self.dwSize}, {self.bVisible}>"


class _Char(ctypes.Union):
    _fields_ = [('UnicodeChar', ctypes.c_wchar),
                ('AsciiChar', ctypes.c_char)]


class _CHAR_INFO(ctypes.Structure):
    _fields_ = [('Char', _Char),
                ('Attributes', ctypes.c_ushort)]


class CursorInformation:
    def __init__(self, size: int, visibility: bool):
        self.size = size
        self.visibility = visibility

    def __to_win32_CONSOLE_CURSOR_INFO(self):
        return _CONSOLE_SCREEN_BUFFER_INFO(self.size, 1 if self.visibility else 0)

    @staticmethod
    def __from_CONSOLE_CURSOR_INFO(info):
        return CursorInformation(info.dwSize, True if info.bVisible else False)

    def __repr__(self):
        return f"<{self.size}, {self.visibility}>"


STD_OUTPUT_HANDLE = -11
INVALID_HANDLE_VALUE = -1


class TextAttribute(enum.IntFlag):
    FOREGROUND_BLUE = 0x0001
    FOREGROUND_GREEN = 0x0002
    FOREGROUND_RED = 0x0004
    FOREGROUND_INTENSITY = 0x0008
    BACKGROUND_BLUE = 0x0010
    BACKGROUND_GREEN = 0x0020
    BACKGROUND_RED = 0x0040
    BACKGROUND_INTENSITY = 0x0080
    COMMON_LVB_LEADING_BYTE = 0x0100
    COMMON_LVB_TRAILING_BYTE = 0x0200
    COMMON_LVB_GRID_HORIZONTAL = 0x0400
    COMMON_LVB_GRID_LVERTICAL = 0x0800
    COMMON_LVB_GRID_RVERTICAL = 0x1000
    COMMON_LVB_REVERSE_VIDEO = 0x4000
    COMMON_LVB_UNDERSCORE = 0x8000


class ConsoleError(Exception):
    pass


def _general_windows_errcheck(result, func, args):
    if not result:
        raise ctypes.WinError(ctypes.get_last_error())


def _get_std_handle_errcheck(result, func, args):
    if result == ctypes.c_void_p(INVALID_HANDLE_VALUE):
        raise ctypes.WinError(ctypes.get_last_error())
    elif result is None:
        raise ConsoleError(
            "The application does not have the associated standard handle provided.")
    return result


_GetStdHandle = ctypes.windll.kernel32.GetStdHandle
_GetStdHandle.argtypes = [ctypes.c_ulong]
_GetStdHandle.restype = ctypes.c_void_p
_GetStdHandle.errcheck = _get_std_handle_errcheck

_SetConsoleCursorPosition = ctypes.windll.kernel32.SetConsoleCursorPosition
_SetConsoleCursorPosition.argtypes = [ctypes.c_void_p, _COORD]
_SetConsoleCursorPosition.restype = ctypes.c_int
_SetConsoleCursorPosition.errcheck = _general_windows_errcheck

_GetConsoleScreenBufferInfo = ctypes.windll.kernel32.GetConsoleScreenBufferInfo
_GetConsoleScreenBufferInfo.argtypes = [
    ctypes.c_void_p, ctypes.POINTER(_CONSOLE_SCREEN_BUFFER_INFO)]
_GetConsoleScreenBufferInfo.restype = ctypes.c_int
_GetConsoleScreenBufferInfo.errcheck = _general_windows_errcheck

_FillConsoleOutputCharacterA = ctypes.windll.kernel32.FillConsoleOutputCharacterA
_FillConsoleOutputCharacterA.argtypes = [
    ctypes.c_void_p, ctypes.c_char, ctypes.c_ulong, _COORD, ctypes.POINTER(ctypes.c_ulong)]
_FillConsoleOutputCharacterA.restype = ctypes.c_int
_FillConsoleOutputCharacterA.errcheck = _general_windows_errcheck

_FillConsoleOutputAttribute = ctypes.windll.kernel32.FillConsoleOutputAttribute
_FillConsoleOutputAttribute.argtypes = [
    ctypes.c_void_p, ctypes.c_ushort, ctypes.c_ulong, _COORD, ctypes.POINTER(ctypes.c_ulong)]
_FillConsoleOutputAttribute.restype = ctypes.c_int
_FillConsoleOutputAttribute.errcheck = _general_windows_errcheck

_SetConsoleCursorInfo = ctypes.windll.kernel32.SetConsoleCursorInfo
_SetConsoleCursorInfo.argtypes = [
    ctypes.c_void_p, ctypes.POINTER(_CONSOLE_CURSOR_INFO)]
_SetConsoleCursorInfo.restype = ctypes.c_int
_SetConsoleCursorInfo.errcheck = _general_windows_errcheck

_GetConsoleCursorInfo = ctypes.windll.kernel32.GetConsoleCursorInfo
_GetConsoleCursorInfo.argtypes = [
    ctypes.c_void_p, ctypes.POINTER(_CONSOLE_CURSOR_INFO)]
_GetConsoleCursorInfo.restype = ctypes.c_int
_GetConsoleCursorInfo.errcheck = _general_windows_errcheck

_SetConsoleTextAttribute = ctypes.windll.kernel32.SetConsoleTextAttribute
_SetConsoleTextAttribute.argtypes = [ctypes.c_void_p, ctypes.c_ushort]
_SetConsoleTextAttribute.restype = ctypes.c_int
_SetConsoleTextAttribute.errcheck = _general_windows_errcheck

_SetConsoleTitleW = ctypes.windll.kernel32.SetConsoleTitleW
_SetConsoleTitleW.argtypes = [ctypes.c_wchar_p]
_SetConsoleTitleW.restype = ctypes.c_int
_SetConsoleTitleW.errcheck = _general_windows_errcheck

_ReadConsoleOutputW = ctypes.windll.kernel32.ReadConsoleOutputW
_ReadConsoleOutputW.argtypes = [ctypes.c_void_p, ctypes.POINTER(
    _CHAR_INFO), _COORD, _COORD, ctypes.POINTER(_SMALL_RECT)]
_ReadConsoleOutputW.restype = ctypes.c_uint
_ReadConsoleOutputW.errcheck = _general_windows_errcheck

_ReadConsoleOutputA = ctypes.windll.kernel32.ReadConsoleOutputA
_ReadConsoleOutputA.argtypes = [ctypes.c_void_p, ctypes.POINTER(
    _CHAR_INFO), _COORD, _COORD, ctypes.POINTER(_SMALL_RECT)]
_ReadConsoleOutputA.restype = ctypes.c_uint
_ReadConsoleOutputA.errcheck = _general_windows_errcheck

_ReadConsoleOutputCharacterA = ctypes.windll.kernel32.ReadConsoleOutputCharacterA
_ReadConsoleOutputCharacterA.argtypes = [
    ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32, _COORD, ctypes.POINTER(ctypes.c_uint32)]
_ReadConsoleOutputCharacterA.restype = ctypes.c_uint
_ReadConsoleOutputCharacterA.errcheck = _general_windows_errcheck


class ConsoleStandardHandle(enum.IntEnum):
    STD_INPUT_HANDLE = -10
    STD_OUTPUT_HANDLE = -11
    STD_ERROR_HANDLE = -12


class Console:
    CONSOLE_COLOR_ATTRIBUTE_MAP = {
        'black': 0x0,
        'blue': 0x1,
        'green': 0x2,
        'aqua': 0x3,
        'red': 0x4,
        'purple': 0x5,
        'yellow': 0x6,
        'white': 0x7,
        'gray': 0x8,
        'light blue': 0x9,
        'light green': 0xA,
        'light aqua': 0xB,
        'light red': 0xC,
        'light purple': 0xD,
        'light yellow': 0xE,
        'bright white': 0xF
    }

    def __init__(self, std_handle=ConsoleStandardHandle.STD_INPUT_HANDLE):
        self.handle = _GetStdHandle(std_handle)
        print(self.handle)
        self.__default_cursor_info = self.__get_win32_cursor_info()
        self.__default_console_info = self.__get_win32_console_screen_buffer_info()

    def clear_screen(self, char=' '):
        coord_screen = _COORD(0, 0)
        chars_written = ctypes.c_ulong(0)
        csbi = _CONSOLE_SCREEN_BUFFER_INFO()
        console_size = ctypes.c_ulong(0)

        _GetConsoleScreenBufferInfo(self.handle, ctypes.byref(csbi))
        console_size = csbi.dwSize.X * csbi.dwSize.Y

        _FillConsoleOutputCharacterA(self.handle, ctypes.c_char(
            ord(char)), console_size, coord_screen, ctypes.byref(chars_written))
        _GetConsoleScreenBufferInfo(self.handle, ctypes.byref(csbi))
        _FillConsoleOutputAttribute(
            self.handle, csbi.wAttributes, console_size, coord_screen, ctypes.byref(chars_written))
        _SetConsoleCursorPosition(self.handle, coord_screen)

    def set_title(self, title):
        unicode_buffer = ctypes.create_unicode_buffer(title)
        _SetConsoleTitleW(unicode_buffer)

    def set_default_cursor_info(self):
        _SetConsoleCursorInfo(
            self.handle, ctypes.byref(self.__default_cursor_info))

    def set_default_text_color(self):
        self.__set_text_attribute(self.__default_console_info.wAttributes)

    def get_cursor_info(self):
        cci = self.__get_win32_cursor_info()
        return CursorInformation._CursorInformation__from_CONSOLE_CURSOR_INFO(cci)

    def __get_win32_cursor_info(self):
        print(self.handle)
        cci_out = _CONSOLE_CURSOR_INFO()
        _GetConsoleCursorInfo(self.handle, ctypes.byref(cci_out))
        return cci_out

    def get_console_info(self):
        csbi = self.__get_win32_console_screen_buffer_info()
        return ConsoleScreenInformation._ConsoleScreenInformation__from_win32_CONSOLE_SCREEN_BUFFER_INFO(csbi)

    def __get_win32_console_screen_buffer_info(self):
        csbi = _CONSOLE_SCREEN_BUFFER_INFO()
        _GetConsoleScreenBufferInfo(self.handle, ctypes.byref(csbi))
        return csbi

    def set_cursor_info(self, size: int, visibility: bool):
        if size < 1 or size > 100:
            raise ConsoleError("Size must be between 1 and 100")

        cci = _CONSOLE_CURSOR_INFO(size, 1 if visibility else 0)
        _SetConsoleCursorInfo(self.handle, ctypes.byref(cci))

    def __set_text_attribute(self, attributes: TextAttribute):
        _SetConsoleTextAttribute(self.handle, attributes)

    def set_cursor_pos(self, x, y):
        coord_screen = _COORD(x, y)
        _SetConsoleCursorPosition(self.handle, coord_screen)

    def set_text_color(self, foreground: str, background: str):
        if foreground not in Console.CONSOLE_COLOR_ATTRIBUTE_MAP:
            raise ConsoleError("Unable to find foreground color.")

        if background not in Console.CONSOLE_COLOR_ATTRIBUTE_MAP:
            raise ConsoleError("Unable to find background color.")
        _SetConsoleTextAttribute(self.handle, Console.CONSOLE_COLOR_ATTRIBUTE_MAP[background.lower()] << 4 |
                                 Console.CONSOLE_COLOR_ATTRIBUTE_MAP[foreground.lower()])

    def read_console(self):
        csbi = self.__get_win32_console_screen_buffer_info()
        buffer_size = _COORD(0, 0)
        buffer_coord = _COORD(0, 0)
        rectangle = _SMALL_RECT()

        rectangle.Left = csbi.srWindow.Left - 1
        rectangle.Right = csbi.srWindow.Right - 1
        rectangle.Top = csbi.srWindow.Top - 1
        rectangle.Bottom = csbi.srWindow.Bottom - 1

        buffer_size.X = rectangle.Right - rectangle.Left + 1
        buffer_size.Y = rectangle.Bottom - rectangle.Top + 1
        char_info_buffer = (_CHAR_INFO * (buffer_size.X * buffer_size.Y))()

        _ReadConsoleOutputW(self.handle, ctypes.cast(char_info_buffer, ctypes.POINTER(
            _CHAR_INFO)), buffer_size, buffer_coord, ctypes.byref(rectangle))
        char_buffer = ctypes.create_string_buffer(
            buffer_size.X * buffer_size.Y + 1)

        for i, char_info in enumerate(char_info_buffer):
            char_buffer[i] = char_info.Char.AsciiChar

        strings = [None] * buffer_size.Y
        for y in range(buffer_size.Y):
            for x in range(buffer_size.X):
                i = x + buffer_size.X * y
                string = ctypes.string_at(ctypes.byref(char_buffer, i + 1), buffer_size.X - x) \
                    .decode('UTF-8') \
                    .replace('\x00', ' ') \

                strings[y] = string
                break
        return strings

    def read_console_line(self, y: int):
        csbi = self.__get_win32_console_screen_buffer_info()
        length = csbi.srWindow.Right - csbi.srWindow.Left - 1
        char_buffer = ctypes.create_string_buffer(length + 1)
        chars_read = ctypes.c_ulong(0)
        _ReadConsoleOutputCharacterA(self.handle, ctypes.cast(ctypes.byref(
            char_buffer), ctypes.c_char_p), length, _COORD(0, y), ctypes.byref(chars_read))
        return ctypes.string_at(char_buffer).decode('UTF-8')

    def clear_line(self, y: int, x: int = 0):
        coord_screen = _COORD(x, y)
        chars_written = ctypes.c_ulong(0)

        console_info = self.__get_win32_console_screen_buffer_info()
        _FillConsoleOutputCharacterA(self.handle, ctypes.c_char(ord(' ')),
                                     console_info.srWindow.Right, coord_screen,
                                     ctypes.byref(chars_written))

    def clear_line_until(self, x_end: int, y: int, x_start: int = 0):
        coord_screen = _COORD(x_start, y)
        chars_written = ctypes.c_ulong(0)

        console_info = self.__get_win32_console_screen_buffer_info()
        max_length = console_info.srWindow.Right - console_info.srWindow.Left
        if x_end >= console_info.srWindow.Right:
            raise ConsoleError("x_end extends past the window size")

        _FillConsoleOutputCharacterA(self.handle, ctypes.c_char(ord(' ')),
                                     x_end, coord_screen,
                                     ctypes.byref(chars_written))


class ConsoleManager:
    def __init__(self, std_handle=ConsoleStandardHandle.STD_OUTPUT_HANDLE):
        self.console = Console(std_handle)

    def __enter__(self):
        return self.console

    def __exit__(self, type_, value, traceback):
        self.console.set_default_cursor_info()
        self.console.set_default_text_color()


# def scroll_text_up(rectangle: Rectangle, clear_rows):
#     ci = console.get_console_info()
#     for row in range(rectangle.top + 1, ci.window_rectangle.bottom + 1 - rectangle.bottom - clear_rows):
#         for clear_row in range(clear_rows):
#             console.clear_line_until(ci.window_rectangle.right - rectangle.right - rectangle.left,
#                                      row - 1 + clear_row, x_start=rectangle.left)
#             line = console.read_console_line(
#                 row + clear_row)[rectangle.left:-rectangle.right]
#             console.set_cursor_pos(rectangle.left, row - 1 + clear_row)
#             print(line, end='', flush=True)


TOP_PADDING = 5
BOTTOM_PADDING = 5
RIGHT_PADDING = 12
LEFT_PADDING = 12

# if __name__ == "__main__":
#     with ConsoleManager() as console:
#         console.clear_screen()
#         ci = console.get_console_info()

#         padding_rectangle = Rectangle(
#             LEFT_PADDING, TOP_PADDING, RIGHT_PADDING, BOTTOM_PADDING)

#         for padding_row in range(padding_rectangle.top):
#             console.set_cursor_pos(padding_rectangle.left, padding_row)
#             copy_str = "01"
#             if padding_row % 2 != 0:
#                 copy_str = "10"
#             write_padding = copy_str * ((ci.window_rectangle.right - 1) // 2)
#             if (ci.window_rectangle.right - 1) % 2 != 0:
#                 write_padding = write_padding[:-1]
#             print(write_padding, end='', flush=True)

#         for padding_row in range(ci.window_rectangle.bottom - padding_rectangle.bottom,
#                                  ci.window_rectangle.bottom + 1):
#             console.set_cursor_pos(padding_rectangle.left, padding_row)
#             copy_str = "01"
#             if padding_row % 2 != 0:
#                 copy_str = "10"
#             write_padding = copy_str * ((ci.window_rectangle.right - 1) // 2)
#             if (ci.window_rectangle.right - 1) % 2 != 0:
#                 write_padding = write_padding[:-1]
#             print(write_padding, end='', flush=True)

#         for row in range(ci.window_rectangle.bottom + 1):
#             console.set_cursor_pos(
#                 ci.window_rectangle.right - RIGHT_PADDING, row)
#             copy_str = "01"
#             if row % 2 != 0:
#                 copy_str = "10"
#             write_padding = copy_str * (padding_rectangle.right + 1 // 2)
#             if ci.window_rectangle.right % 2 != 0:
#                 write_padding = write_padding[:-1]
#             print(write_padding, end='', flush=True)

#         for row in range(ci.window_rectangle.bottom + 1):
#             console.set_cursor_pos(0, row)
#             copy_str = "01"
#             if row % 2 != 0:
#                 copy_str = "10"
#             write_padding = copy_str * (padding_rectangle.left // 2)
#             if padding_rectangle.left % 2 != 0:
#                 write_padding = write_padding[:-1]
#             print(write_padding, end='', flush=True)

#         while True:
#             ci = console.get_console_info()
#             console.set_cursor_pos(
#                 padding_rectangle.left, ci.window_rectangle.bottom - 1 - padding_rectangle.bottom)
#             console.clear_line_until(ci.window_rectangle.right - padding_rectangle.right - padding_rectangle.left,
#                                      ci.window_rectangle.bottom - 1 - padding_rectangle.bottom,
#                                      x_start=padding_rectangle.left)
#             console.set_text_color("bright white", "light red")
#             print('> ', end='', flush=True)
#             console.set_default_text_color()
#             line = input()

#             if line == "quit":
#                 break

#             scroll_text_up(padding_rectangle, 1)
