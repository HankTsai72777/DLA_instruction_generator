# Basic Function
def dec_to_bin_str(dec_num, bits):
    bin_representation = bin(dec_num)[2:]
    bin_num = bin_representation.zfill(bits)
    return bin_num
def hex_to_bin_str(hex_num, bits):
    if isinstance(hex_num, int):
        hex_num = hex(hex_num)[2:]
    dec_num = int(hex_num, 16)
    bin_representation = bin(dec_num)[2:]
    bin_num = bin_representation.zfill(bits)
    return bin_num
def dec_to_hex_str(dec_num, bits):
    hex_representation = hex(dec_num)[2:]
    hex_num = hex_representation.zfill(bits)
    return hex_num
def hex_to_dec_value(hex_num):
    if isinstance(hex_num, int):
        hex_num = hex(hex_num)[2:]
    dec_value = int(hex_num, 16)
    return dec_value
# Compiler
def ASIP_inst_gen_2(opcode, source, target=0, length=0, choose_data_num=0, data_num=0):
    # LOAD & DUMP
    opcode_bin = dec_to_bin_str(opcode, 4)

    if (choose_data_num==1):
        source_plus_data_num = (hex_to_dec_value(source)) \
            + int(data_num-1)
        target_bin = dec_to_bin_str(int(source_plus_data_num), 20)
    else:
        target_bin = hex_to_bin_str(target, 20)
    
    source_bin = hex_to_bin_str(source, 20)

    if(length==0):
        length_num = 0
    else:
        length_num = length -1
    length_bin = hex_to_bin_str(length_num, 20)

    ASIP_inst_bin = opcode_bin + length_bin + target_bin + source_bin

    # change to hex type
    ASIP_inst_dec       = int(ASIP_inst_bin, 2)
    ASIP_inst_hex       = dec_to_hex_str(ASIP_inst_dec, 8)
    return ASIP_inst_hex

# txt generator
def ASIP_txt_gen(ASIP_inst_str, file_name):
    ASIP_inst_32bit = ASIP_inst_str.zfill(4)
    with open(file_name, 'w') as f:
        f.write(ASIP_inst_32bit)
    return ASIP_inst_32bit