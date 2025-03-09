# set pins to on
# ldr x0, =0x50000518
# ldr x1, =0x10200000
# str x1, [x0]
ldr r0, =0x50000754
ldr r1, =0xfffffffd
str r1, [r0]
ldr r0, =0x50000770
ldr r1, =0xfffffffd
str r1, [r0]

# turn on row 
ldr r0, =0x50000508
ldr r1, =0x200000
str r1, [r0]
wfe
