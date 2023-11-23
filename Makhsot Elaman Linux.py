#1
# def rc4(key, plaintext):
#     S = list(range(256))
#     j = 0
#
#     # Инициализация перестановочного массива S
#     for i in range(256):
#         j = (j + S[i] + ord(key[i % len(key)])) % 256
#         S[i], S[j] = S[j], S[i]
#
#     # Инициализация переменных
#     i = j = 0
#     ciphertext = []
#
#     # Генерация поточного ключа и шифрование
#     for char in plaintext:
#         i = (i + 1) % 256
#         j = (j + S[i]) % 256
#         S[i], S[j] = S[j], S[i]
#         k = S[(S[i] + S[j]) % 256]
#         ciphertext.append(chr(ord(char) ^ k))
#
#     return ''.join(ciphertext)
#
# def rc4_decrypt(key, ciphertext):
#     # Дешифрование RC4 аналогично шифрованию
#     return rc4(key, ciphertext)
#
# # Ввод строки для шифрования
# key = input('Введите ключ (любой текст): ')
# plaintext = input('Введите строку для шифрования: ')
#
# # Шифрование
# encrypted_text = rc4(key, plaintext)
# print('Зашифрованный текст:', encrypted_text)
#
# # Дешифрование
# decrypted_text = rc4_decrypt(key, encrypted_text)
# print('Расшифрованный текст:', decrypted_text)



#2
# def rc4(key, plaintext):
#     S = list(range(256))
#     j = 0
#
#     # Инициализация перестановочного массива S
#     for i in range(256):
#         j = (j + S[i] + ord(key[i % len(key)])) % 256
#         S[i], S[j] = S[j], S[i]
#
#     # Инициализация переменных
#     i = j = 0
#     ciphertext = []
#
#     # Генерация поточного ключа и шифрование
#     for char in plaintext:
#         i = (i + 1) % 256
#         j = (j + S[i]) % 256
#         S[i], S[j] = S[j], S[i]
#         k = S[(S[i] + S[j]) % 256]
#         ciphertext.append(chr(ord(char) ^ k))
#
#     return ''.join(ciphertext)
#
# def rc4_decrypt(key, ciphertext):
#     # Дешифрование RC4 аналогично шифрованию
#     return rc4(key, ciphertext)
#
# # Пример использования
# key = 'Key'  # Ключ шифрования (любой текстовый объект)
# plaintext = 'Hello, RC4!'  # Открытый текст для шифрования
#
# # Шифрование
# encrypted_text = rc4(key, plaintext)
# print('Зашифрованный текст:', encrypted_text)
#
# # Дешифрование
# decrypted_text = rc4_decrypt(key, encrypted_text)
# print('Расшифрованный текст:', decrypted_text)
