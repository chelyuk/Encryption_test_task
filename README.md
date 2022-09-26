# Encryption_test_task
TASK

A XOR cipher is an encryption method on which we take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

A common way to use a XOR cipher is with relatively long text and a relatively short key, on which case the key is repeated cyclically throughout the message:
	‘apoquahgbabfp’ XOR ‘xyz’ =
	‘a’ XOR ‘x’
‘p’ XOR ‘y’
‘o’ XOR ‘z’
‘q’ XOR ‘x’
‘u’ XOR ‘y’, ...
		
In this project, you are required to build a simple brute force encryption-breaking logic in Python that gets an encrypted text and a key size without the key itself - and works to find the encryption key using a brute-force lookup.

1.	Write a function xor_decrypt(encrypted_text, key) that gets a list of numbers and a key (as string) and decrypts this list into a text (as string again). Make sure that xor_decrypt(xor_encrypt(text, key), key) == text.
Example:
	xor_decrypt([24, 24, 26, 30, 28], "yz") -> “abcde”
Explanation:
	‘y’ = 121 -> 24 XOR 121 = 97 -> 97 = ‘a’ (or in short: 24 XOR ‘y’ = ‘a’)
	24 XOR ‘z’ = ‘b’
	26 XOR ‘y’ = ‘c’
	30 XOR ‘z’ = ‘d’
	28 XOR ‘y’ = ‘e’
2.	Write a function guess_key(encrypted_text, key_size) that tries to break a XOR encryption by a brute-force attack under the following assumptions:
a.	The decrypted text contains a standard English text containing only letters, numbers, punctuation marks, etc.
b.	The encryption key consists of key_size lower-case English characters.
	The function will return a list of possible matches as pairs of keys and
	possibly-decrypted text.
3.	Run your result on the “cipher.txt” file provided with key size of 3 - the result (after filtering) should be a readable English text
4.	Using any Python test framework of your choice, write basic tests to ensure guess_key is working as expected (including testing of your filtering mechanism or error handling if such exists).
