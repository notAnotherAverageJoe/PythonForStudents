
import base64
# to encode
message = "hello all my buddies"
encoded = base64.b64encode(message.encode("utf-8"))
print(encoded.decode("utf-8")) # aGVsbG8gYWxsIG15IGJ1ZGRpZXM=


with open("hello.txt", "r") as file:
    content = file.read()
    encrypted_file = content
    decrypted_file = base64.b64decode(encrypted_file).decode("utf-8")
    print(decrypted_file)
    