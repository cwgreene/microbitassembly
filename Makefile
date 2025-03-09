all:
	arm-linux-gnueabihf-as  test.asm -o test.o	
	objcopy -O binary test.o test.bin
	python3 write_hex.py > intel.hex
