byte_size: int = 1234567890

kilo_size: float = byte_size / 1024
mega_size: float = kilo_size / 1024
giga_size: float = mega_size / 1024

print('Размер в байтах:', byte_size,
      '\nРазмер в килобайтах:', kilo_size,
      '\nРазмер в мегабайтах:', mega_size,
      '\nРазмер в гигабайтах:', giga_size, )
