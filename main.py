import typer
from random import randint

app = typer.Typer()

def check_symbol(pw: str) -> bool:
    sym = "&#-_@$%!?+="
    return 1 in [c in sym for c in pw]

def gen_pw(length: int, chars: str) -> str:
    pw = ""
    for _ in range(length):
        pw += (chars[randint(0, len(chars)-1)])
    return pw

@app.command()
def pw(length: int = 16, symbols: bool = True):
    """
    Generate a secure password
    """
    pw = ""
    if symbols: 
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&#-_@$%!?+="
        while True:
            pw = gen_pw(length, chars)
            if check_symbol(pw):
                break
    if not symbols:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        pw = gen_pw(length, chars)
    print(pw)




if __name__ == "__main__":
    app()
