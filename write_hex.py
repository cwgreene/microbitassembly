DATA_OPCODE = "00"

with open("test.bin", "rb") as binary:
    bs = binary.read()
    bs += b"\x00"*(len(bs)%16)
    print(":020000040000FA") # Set memory writes to the very beginning
    for i in range(4,len(bs) // 16):
        print(":", end="")
        # Write length of input binary
        print(f"10" + f"{i*0x10:04X}" + DATA_OPCODE , end="")
        checksum = 0x10+i*0x10+i//0x100
        for b in bs[16*i:16*(i+1)]:
            checksum += b
            print(f"{b:02X}", end="")
        checksum = (-checksum)%256
        print(f"{checksum:02X}")
    print(":04080000C100000033") 
    print(":0400000500000000F7")
    print(":00000001FF")
