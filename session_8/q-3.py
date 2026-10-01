#3.Build a function reverse_message(message) that reverses any string passed to it, similar to how WhatsApp displays reversed text stickers.<br><br><em><strong>Constraint:</strong> Do not use Python's built-in reversed() or [::-1] slicing shortcut.</em>

def reverse_message(message):
    reversed_text = ""
    for char in message:
        reversed_text = char + reversed_text   
    return reversed_text


print(reverse_message("Hello"))        
print(reverse_message("WhatsApp"))     