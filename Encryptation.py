import flet as ft
import pyperclip

morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
         '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
         '0': '-----', ' ': '/'}
morse_inv = {a: b for a, b in morse.items()} #https://www.youtube.com/watch?v=F19tasIOYoE&t=663s

polar = {'P': 'C', 'C': 'P', 'O': 'E', 'E': 'O', 'L': 'N', 'N': 'L', 'A': 'I', 'I': 'A', 'R': 'T', 'T': 'R', 'H': 'W',
         'W': 'H', 'D': 'U', 'U': 'D', 'G': 'Y', 'Y': 'G', 'B': 'V', 'V': 'B', 'F': 'J', 'J': 'F', 'K': 'Q', 'Q': 'K',
         'M': 'Z', 'Z': 'M', 'S': 'X', 'X': 'S'}
polar_inv = {a: b for b, a in polar.items()}


def translate(text, dictionary):
    return ''.join(dictionary.get(c.upper(), c) for c in text) #video de como aprender a programar pero no lo encuentro cuando lo encuentre se lo envio


def translate_morse(text, dictionary):
    return ' '.join(dictionary.get(c, c) for c in text.split())


def main(page: ft.Page):
    page.title = "Encryption Machine"

    input_text = ft.TextField(label="Escribe aqui")
    output_text = ft.TextField(label="Resultado", read_only=True)


    def encrypt(e):
        output_text.value = translate(input_text.value, morse) if method.value == "Morse" else translate(
            input_text.value, polar)
        page.update()

    def decrypt(e):
        decoded = translate_morse(input_text.value, morse_inv) if method.value == "Morse" else translate(
            input_text.value, polar_inv)
        input_text.value, output_text.value = decoded, decoded
        page.update()



    def copy_to_clipboard(e):
        pyperclip.copy(output_text.value)
        page.snack_bar = ft.SnackBar(ft.Text("Texto copiado")) #todo esto fue revisando los comandos de pyperclip
        page.snack_bar.open = True
        page.update()

    method = ft.Dropdown(label="Metodo", options=[ft.dropdown.Option("Morse"), ft.dropdown.Option("Polar")])

    page.add(input_text, method, ft.ElevatedButton("Encriptar", on_click=encrypt),
             ft.ElevatedButton("Desencriptar", on_click=decrypt), output_text,
             ft.ElevatedButton("Copiar", on_click=copy_to_clipboard))


ft.app(target=main)