import tkinter
import customtkinter

app = customtkinter.CTk()

if __name__ == "__main__" :

    def vigenere(message, key, direction=1):

        key_index = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        final_message = ''

        for char in message.lower():

            # Append any non-letter character to the message
            if not char.isalpha():
                final_message += char
            else:        
                # Find the right key character to encode/decode
                key_char = key[key_index % len(key)]
                key_index += 1

                # Define the offset and the encrypted/decrypted letter
                offset = alphabet.index(key_char)
                index = alphabet.find(char)
                new_index = (index + offset*direction) % len(alphabet)
                final_message += alphabet[new_index]
        
        return final_message
    
    def encrypt(message, key):
        return vigenere(message, key)

    def decrypt(message, key):
        return vigenere(message, key, -1)

     #fenêtre
    app.geometry("350x500")
    app.resizable(False, False)
    app.title("Vigenere")

    label_message = customtkinter.CTkLabel(app, text="Message :")
    label_message.pack(pady=(10, 0))

    textbox_message = customtkinter.CTkTextbox(app, width=350, height=100)
    textbox_message.pack(pady=5)

    #clé
    label_key = customtkinter.CTkLabel(app, text="Clé :")
    label_key.pack(pady=(10, 0))

    entry_key = customtkinter.CTkEntry(app, width=200)
    entry_key.pack(pady=5)

    #résultat
    label_result = customtkinter.CTkLabel(app, text="Résultat :")
    label_result.pack(pady=(10, 0))

    textbox_result = customtkinter.CTkTextbox(app, width=350, height=100)
    textbox_result.pack(pady=5)

    def handle_encrypt():
        message = textbox_message.get("1.0", "end").strip()
        key = entry_key.get().lower().strip()
        if message and key:
            result = encrypt(message, key)
            textbox_result.delete("1.0", "end")
            textbox_result.insert("1.0", result)


    # Boutons
button_encrypt = customtkinter.CTkButton(app, text="🔒 Chiffrer", command=handle_encrypt)
button_encrypt.pack(pady=10)

app.mainloop()