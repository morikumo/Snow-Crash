def decode_transformed_output(transformed_output):
    decoded = ""
    local_120 = 0
    
    for char in transformed_output:
        decoded_char = chr(ord(char) - local_120)
        decoded += decoded_char
        local_120 += 1
    
    return decoded

file_path = "/home/user/level09/token"

with open(file_path, "r") as file:
    transformed_output = file.read().strip()

decoded_output = decode_transformed_output(transformed_output)
print("Decoded output:", decoded_output)
