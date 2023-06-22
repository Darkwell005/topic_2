byte_size: int = 1234567890
kilo_size: float = byte_size / 1024
mega_size: float = kilo_size / 1024
giga_size: float = mega_size / 1024
print('Размер в байтах:',byte_size,'\n'
      'Размер в килобайтах:',kilo_size,'\n'
      'Размер в мегабайтах:',mega_size,'\n'
      'Размер в гигабайтах:',giga_size,)

