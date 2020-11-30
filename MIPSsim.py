#On my honor, I have neither given nor received unauthorized aid on this assignment
from sys import argv
import queue
import os
import stat

category1dict = {
"0000":"J","0001":"JR",
"0010":"BEQ","0011":"BLTZ",
"0100":"BGTZ","0101":"BREAK",
"0110":"SW","0111":"LW",
"1000":"SLL","1001":"SRL",
"1010":"SRA","1011":"NOP"
}

category2dict = {
"0000":"ADD","0001":"SUB",
"0010":"MUL","0011":"AND",
"0100":"OR","0101":"XOR",
"0110":"NOR","0111":"SLT",
"1000":"ADDI","1001":"ANDI",
"1010":"ORI","1011":"XORI"
}


def read_file():
	str = ""
	fp = open(argv[1])
	content = fp.readlines()
	return content

def read_file_disassembly():
	str = ""
	fp = open("disassembly.txt")
	content = fp.readlines()
	return content

def write_sample_disassembly(disassembly):
	f = open("disassembly.txt","a")
	f.write(disassembly)
	f.close()

def write_sample_simulation(simulation):
	f = open("simulation.txt","a")
	f.write(simulation)
	f.close()

#------------------------------------------------------------------------------------------------
def bintopositive(content):
	symbol = content[0]
	numstr = content[1:]
	num = int(numstr,2)
	return str(num)

def bintonegative(content):
	newnumlist = []
	symbol = content[0]
	numstr = content[1:]
	numlist = list(numstr)
	for i in range(len(numlist)):
		if numlist[i] == '0':
			newnumlist.append('1')
		else:
			newnumlist.append('0')
	newnumstr = "".join(newnumlist)
	newnum = int(newnumstr,2) + 1
	num = "-" + str(newnum)
	return num

def funneg(content):
	newnumlist = []
	numstr = content
	numlist = list(numstr)
	for i in range(len(numlist)):
		if numlist[i] == '0':
			newnumlist.append('1')
		else:
			newnumlist.append('0')
	newnumstr = "".join(newnumlist)
	newnum = int(newnumstr,2) + 1
	num = str(newnum)
	return num

#------------------------------------------------------------------------------------------------
#disassembly_file
def category1(instruction,content):
	opcode = content[2:6]
	if opcode == "0010":
		instruction3 = category1BEQ(opcode,content)
		disassembly = content + "\t" + str(address) + "\t" + instruction3
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	if opcode == "1000":
		instruction3 = category1SLLSRLSRA(opcode,content)
		disassembly = content + "\t" + str(address) + "\t" + instruction3
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	if opcode == "0111":
		instruction3 = category1W(opcode,content)
		disassembly = content + "\t" + str(address) + "\t" + instruction3
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	if opcode == "0100":
		instruction3 = category1BGTZ(opcode,content)
		disassembly = content + "\t" + str(address) + "\t" + instruction3
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	if opcode == "0000":
		instruction3 = category1J(opcode,content)
		disassembly = content + "\t" + str(address) + "\t" + instruction3
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	if opcode == "0011":
		instruction3 = category1BLTZ(opcode,content)
		disassembly = content + "\t" + str(address) + "\t" + instruction3
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	if opcode == "0110":
		instruction3 = category1W(opcode,content)
		disassembly = content + "\t" + str(address) + "\t" + instruction3
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	if opcode == "0101":
		instruction3 = category1Break(opcode,content)
		disassembly = content + "\t" + str(address) + "\t" + instruction3
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	if opcode == "0001":
		instruction3 = category1JR(opcode,content)
		disassembly = content + "\t" + str(address) + "\t" + instruction3
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	if opcode == "1001":
		instruction3 = category1SLLSRLSRA(opcode,content)
		disassembly = content + "\t" + str(address) + "\t" + instruction3
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	if opcode == "1010":
		instruction3 = category1SLLSRLSRA(opcode,content)
		disassembly = content + "\t" + str(address) + "\t" + instruction3
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	if opcode == "1011":
		disassembly = content + "\t" + str(address) + "\t" + "NOP"
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	#data
	if opcode == "1100" or opcode == "1101" or opcode == "1110" or opcode == "1111":
		num = bintopositive(content)
		data_all.append(int(num))
		disassembly = content + "\t" + str(address) + "\t" + num
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)

def category2(instruction,content):
	idbits = content[2:6]
	if idbits == "0000" or idbits == "0010" or idbits == "0001" or idbits == "0011" or idbits == "0100" or idbits == "0101" or idbits == "0110" or idbits == "0111":
		instruction3 = category2register(idbits,content)
		disassembly = content + "\t" + str(address) + "\t" + instruction3
		#print(disassembly)    #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	if idbits == "1000" or idbits == "1001" or idbits == "1010" or idbits == "1011":
		instruction3 = category2immediate(idbits,content)
		disassembly = content + "\t" + str(address) + "\t" + instruction3
		#print(disassembly)         #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)
	#data
	if idbits == "1100" or idbits == "1101" or idbits == "1110" or idbits == "1111":
		num = bintonegative(content)
		data_all.append(int(num))
		disassembly = content + "\t" + str(address) + "\t" + num
		#print(disassembly)         #tiao shi xin xi
		disassembly  = disassembly + "\n"
		write_sample_disassembly(disassembly)

#------------------------------------------------------------------------------------------------
#BEQ
def category1BEQ(opcode,content):
	rs = content[6:11]
	rt = content[11:16]
	offset = content[16:]

	rs10 = int(rs,2)
	rt10 = int(rt,2)
	instruction1 = "R"+str(rs10)+","
	instruction2 = "R"+str(rt10)+","

	if offset[0] == "1":
		newnum = funneg(offset[1:])
		offsetint = (0 - int(newnum)) << 2
	else:
		offsetint = int(offset,2) << 2

	instruction = category1dict[opcode] + " " + instruction1 + " " + instruction2 + " " + "#" + str(offsetint)
	#print(instruction)
	return instruction

#BGTZ
def category1BGTZ(opcode,content):
	rs = content[6:11]
	offset = content[16:]
	rs10 = int(rs,2)
	instruction1 = "R"+str(rs10)+","

	if offset[0] == "1":
		newnum = funneg(offset[1:])
		offsetint = (0 - int(newnum)) << 2
	else:
		offsetint = int(offset,2) << 2

	instruction = category1dict[opcode] + " " + instruction1 + " " + "#" + str(offsetint)
	#print(instruction)
	return instruction

#BLTZ
def category1BLTZ(opcode,content):
	rs = content[6:11]
	rs10 = int(rs,2)
	offset = content[16:]

	if offset[0] == "1":
		newnum = funneg(offset[1:])
		offsetint = (0 - int(newnum)) << 2
	else:
		offsetint = int(offset,2) << 2

	instruction = category1dict[opcode] + " " + "R" + str(rs10) + ", " + "#" + str(offsetint)
	#print(instruction)
	return instruction

#SLL,SRL,SRA
def category1SLLSRLSRA(opcode,content):
	rt = content[11:16]
	rd = content[16:21]
	sa = content[21:26]
	rt10 = int(rt,2)
	rd10 = int(rd,2)
	sa = int(sa,2)
	instruction1 = "R"+str(rd10)+","
	instruction2 = "R"+str(rt10)+","
	instruction = category1dict[opcode] + " " + instruction1 + " " + instruction2 + " " + "#" + str(sa)
	#print(instruction)
	return instruction

#LW,SW
def category1W(opcode,content):
	base = content[6:11]
	rt = content[11:16]
	offset = content[16:]
	base10 = int(base,2)
	rt10 = int(rt,2)

	if offset[0] == "1":
		newnum = funneg(offset[1:])
		offsetint = (0 - int(newnum))
	else:
		offsetint = int(offset,2)

	instruction1 = "R"+str(rt10)+","
	instruction2 = str(offsetint) + "(R" + str(base10) + ")"
	instruction = category1dict[opcode] + " " + instruction1 + " " + instruction2
	#print(instruction)
	return instruction

#J
def category1J(opcode,content):
	index = content[6:]
	indexint = int(index,2) << 2
	instruction = category1dict[opcode] + " " + "#" + str(indexint)
	#print(instruction)
	return instruction

#JR
def category1JR(opcode,content):
	rs = content[6:11]
	rs10 = int(rs,2)
	instruction = category1dict[opcode] + " " + "R" + str(rs10)
	#print(instruction)
	return instruction

#BREAK
def category1Break(opcode,content):
	instruction = "BREAK"
	return instruction

#NOP

#------------------------------------------------------------------------------------------------
def category2immediate(idbits,content):
	rs = content[6:11]
	rt = content[11:16]
	immediate = content[16:]
	rs10 = int(rs,2)
	rt10 = int(rt,2)
	instruction1 = "R"+str(rt10)+","
	instruction2 = "R"+str(rs10)+","

	if immediate[0] == "1":
		instruction31 = str(int(immediate[1:],2))
		instruction3 = "-" + instruction31
	else:
		instruction3 = str(int(immediate,2))
	instruction = category2dict[idbits] + " " + instruction1 + " " + instruction2 + " " + "#" + instruction3
	#print(instruction)
	return instruction


def category2register(idbits,content):
	rs = content[6:11]
	rt = content[11:16]
	rd = content[16:21]
	rs10 = int(rs,2)
	rt10 = int(rt,2)
	rd10 = int(rd,2)
	instruction1 = "R"+str(rd10)+","
	instruction2 = "R"+str(rs10)+","
	instruction3 = "R"+str(rt10)
	instruction = category2dict[idbits] + " " + instruction1 + " " + instruction2 + " " + instruction3
	#print(instruction)
	return instruction


#new simulation file
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
def handle(instruction,flagn):
	if flagn == 1:
		instruction = instruction.replace(',','')
		list_tmp = instruction.split()
		process = list_tmp[0]

		if process == "ADD":
			process = list_tmp[0]
			rd = list_tmp[1]
			rs1 = list_tmp[2]
			rs2 = list_tmp[3]
			ADD_sim(rd,rs1,rs2)
			return 0
		if process == "ADDI":
			process = list_tmp[0]
			rd = list_tmp[1]
			rs1 = list_tmp[2]
			rs2 = list_tmp[3]
			ADDI_sim(rd,rs1,rs2)
			return 0
		if process == "LW":
			rd = list_tmp[1]
			second_pro = list_tmp[2].split('(')
			imm = second_pro[0]
			rs = second_pro[1][:-1]
			LW_sim(rd,imm,rs)
			return 0
		if process == "SW":
			rd = list_tmp[1]
			second_pro = list_tmp[2].split('(')
			imm = second_pro[0]
			rs = second_pro[1][:-1]
			SW_sim(rd,imm,rs)
			return 0
		if process == "SLL":
			process = list_tmp[0]
			rd = list_tmp[1]
			rt = list_tmp[2]
			sa = list_tmp[3]
			SLL_sim(rd,rt,sa)
			return 0
		if process == "SRL":
			process = list_tmp[0]
			rd = list_tmp[1]
			rt = list_tmp[2]
			sa = list_tmp[3]
			SRL_sim(rd,rt,sa)
			return 0
		if process == "SRA":
			process = list_tmp[0]
			rd = list_tmp[1]
			rt = list_tmp[2]
			sa = list_tmp[3]
			SRA_sim(rd,rt,sa)
			return 0
		if process == "SLT":
			process = list_tmp[0]
			rd = list_tmp[1]
			rs = list_tmp[2]
			rt = list_tmp[3]
			SLT_sim(rd,rs,rt)
			return 0
		if process == "SUB":
			process = list_tmp[0]
			rd = list_tmp[1]
			rs1 = list_tmp[2]
			rs2 = list_tmp[3]
			SUB_sim(rd,rs1,rs2)
			return 0
		if process == "MUL":
			process = list_tmp[0]
			rd = list_tmp[1]
			rs1 = list_tmp[2]
			rs2 = list_tmp[3]
			MUL_sim(rd,rs1,rs2)
			return 0
		if process == "AND":
			process = list_tmp[0]
			rd = list_tmp[1]
			rs1 = list_tmp[2]
			rs2 = list_tmp[3]
			AND_sim(rd,rs1,rs2)
			return 0
		if process == "ANDI":
			process = list_tmp[0]
			rd = list_tmp[1]
			rs1 = list_tmp[2]
			rs2 = list_tmp[3]
			ANDI_sim(rd,rs1,rs2)
			return 0
		if process == "OR":
			process = list_tmp[0]
			rd = list_tmp[1]
			rs1 = list_tmp[2]
			rs2 = list_tmp[3]
			OR_sim(rd,rs1,rs2)
			return 0
		if process == "ORI":
			process = list_tmp[0]
			rd = list_tmp[1]
			rs1 = list_tmp[2]
			rs2 = list_tmp[3]
			ORI_sim(rd,rs1,rs2)
			return 0
		if process == "XOR":
			process = list_tmp[0]
			rd = list_tmp[1]
			rs1 = list_tmp[2]
			rs2 = list_tmp[3]
			XOR_sim(rd,rs1,rs2)
			return 0
		if process == "XORI":
			process = list_tmp[0]
			rd = list_tmp[1]
			rs1 = list_tmp[2]
			rs2 = list_tmp[3]
			XORI_sim(rd,rs1,rs2)
			return 0
		if process == "NOR":
			process = list_tmp[0]
			rd = list_tmp[1]
			rs1 = list_tmp[2]
			rs2 = list_tmp[3]
			NOR_sim(rd,rs1,rs2)
			return 0

	if flagn == 0:
		instruction = instruction.replace(',','')
		list_tmp = instruction.split()
		process = list_tmp[0]

		if process == "BEQ":
			process = list_tmp[0]
			rd = list_tmp[1]
			rs1 = list_tmp[2]
			imm = list_tmp[3]
			new_i = BEQ_sim(rd,rs1,imm)
			return new_i
		if process == "BLTZ" or process == "BGTZ":
			process = list_tmp[0]
			rd = list_tmp[1]
			imm = list_tmp[2]
			new_i = BTZ_sim(process,rd,imm)
			return new_i
		if process == "J":
			process = list_tmp[0]
			imm = list_tmp[1]
			new_i = J(imm)
			return new_i
		if process == "JR":
			process = list_tmp[0]
			rs = int(list_tmp[1][1:])
			imm = str(register_all[rs])
			new_i = JR_sim(imm)
			return new_i

def ADD_sim(rd,rs1,rs2):
	rs110 = int(rs1[1:])
	rs210 = int(rs2[1:])
	rd10 = int(rd[1:])
	register_all[rd10] = register_all[rs110] + register_all[rs210]

def SUB_sim(rd,rs1,rs2):
	rs110 = int(rs1[1:])
	rs210 = int(rs2[1:])
	rd10 = int(rd[1:])
	register_all[rd10] = register_all[rs110] - register_all[rs210]

def MUL_sim(rd,rs1,rs2):
	rs110 = int(rs1[1:])
	rs210 = int(rs2[1:])
	rd10 = int(rd[1:])
	register_all[rd10] = register_all[rs110] * register_all[rs210]

def AND_sim(rd,rs1,rs2):
	rs110 = int(rs1[1:])
	rs210 = int(rs2[1:])
	rd10 = int(rd[1:])
	register_all[rd10] = register_all[rs110] & register_all[rs210]

def ANDI_sim(rd,rs1,rs2):
	rs110 = int(rs1[1:])
	rs210 = int(rs2[1:])
	rd10 = int(rd[1:])
	register_all[rd10] = register_all[rs110] & rs210

def OR_sim(rd,rs1,rs2):
	rs110 = int(rs1[1:])
	rs210 = int(rs2[1:])
	rd10 = int(rd[1:])
	register_all[rd10] = register_all[rs110] | register_all[rs210]

def ORI_sim(rd,rs1,rs2):
	rs110 = int(rs1[1:])
	rs210 = int(rs2[1:])
	rd10 = int(rd[1:])
	register_all[rd10] = register_all[rs110] | rs210

def XOR_sim(rd,rs1,rs2):
	rs110 = int(rs1[1:])
	rs210 = int(rs2[1:])
	rd10 = int(rd[1:])
	register_all[rd10] = register_all[rs110] ^ register_all[rs210]

def XORI_sim(rd,rs1,rs2):
	rs110 = int(rs1[1:])
	rs210 = int(rs2[1:])
	rd10 = int(rd[1:])
	register_all[rd10] = register_all[rs110] ^ rs210

def NOR_sim(rd,rs1,rs2):
	rs110 = int(rs1[1:])
	rs210 = int(rs2[1:])
	rd10 = int(rd[1:])
	register_all[rd10] = ~(register_all[rs110] | register_all[rs210])

def SLT_sim(rd,rs,rt):
	rs10 = int(rs[1:])
	rt10 = int(rt[1:])
	rd10 = int(rd[1:])
	if register_all[rs10] < register_all[rt10]:
		register_all[rd10] = 1
	else:
		register_all[rd10] = 0

def ADDI_sim(rd,rs1,rs2):
	rs110 = int(rs1[1:])
	rs210 = int(rs2[1:])
	rd10 = int(rd[1:])
	register_all[rd10] = register_all[rs110] + rs210

def BEQ_sim(rd,rs1,imm):
	rd10 = int(rd[1:])
	rs10 = int(rs1[1:])
	imm10 = int(imm[1:])
	if register_all[rd10] == register_all[rs10]:
		return int(imm10/4 + 1)
	else:
		return -1

def BTZ_sim(process,rd,imm):
	rd10 = int(rd[1:])
	imm10 = int(imm[1:])
	if process == "BLTZ":
		if register_all[rd10] < 0:
			return int(imm10/4 + 1)
		else:
			return -1
	if process == "BGTZ":
		if register_all[rd10] > 0:
			return int(imm10/4 + 1)
		else:
			return -1

def J(imm):
	imm = imm[1:]
	return dict_sim_aii[imm]

def JR_sim(imm):
	return dict_sim_aii[imm]

def LW_sim(rd,imm,rs):
	rd10 = int(rd[1:])
	rs = int(rs[1:])
	imm = int(imm)
	register_all[rd10] = int(data_memory[str(register_all[rs] + imm)])

def SW_sim(rd,imm,rs):
	rd10 = int(rd[1:])
	rs = int(rs[1:])
	imm = int(imm)
	data_memory[str(register_all[rs] + imm)] = register_all[rd10]

def SLL_sim(rd,rt,sa):
	rd10 = int(rd[1:])
	rt10 = int(rt[1:])
	sa10 = int(sa[1:])
	register_all[rd10] = register_all[rt10] << sa10

def SRL_sim(rd,rt,sa):
	rd10 = int(rd[1:])
	rt10 = int(rt[1:])
	sa10 = int(sa[1:])
	tmp = register_all[rt10]
	tmp = str(tmp)
	if tmp[0] == '-':
		#bin_tmp = bin(tmp)
		#tmp_shu = bin_tmp[3:]
		int1 = int(tmp[1:])
		bin_tmp = '{:031b}'.format(int1)
		bin_tmp = "1" + bin_tmp

		bin_tmp = list(bin_tmp)
		for i in range(len(bin_tmp)):
			if i == 0:
				continue
			else:
				if bin_tmp[i] == '1':
					bin_tmp[i] = '0'
				else:
					bin_tmp[i] = '1'
		bin_tmp = "".join(bin_tmp)
		bin_tmp_int = int(bin_tmp[1:],2) + 1
		a = bin_tmp_int >> sa10
		b = '{:032b}'.format(a)
		b = list(b)

		for i in range(len(b)):
			if i == 0:
				continue
			else:
				if b[i] == '1':
					b[i] = '0'
				else:
					b[i] = '1'
		b = "".join(b)
		b = int(b,2) + 1

		register_all[rd10] = b
	else:
		register_all[rd10] = int(tmp) >> sa10

def SRA_sim(rd,rt,sa):
	rt10 = int(rt[1:])
	rd10 = int(rd[1:])
	sa10 = int(sa[1:])
	register_all[rd10] = int(register_all[rt10]) >> sa10

def sim_print(cycle2):
	write_sample_simulation("--------------------\n")
	str1 = "Cycle " + str(cycle2) + ":\n"
	write_sample_simulation(str1)
	write_sample_simulation("\n")

	str2 = "IF Unit:\n"
	write_sample_simulation(str2)
	if waitIns.qsize() != 0:	
		tmp = waitIns.get()	
		str3 = "\tWaiting Instruction: [" + tmp + "]\n"
		waitIns.put(tmp)
	else:
		str3 = "\tWaiting Instruction:\n"
	if eceIns.qsize() != 0:
		tmp = eceIns.get()
		str4 = "\tExecuted Instruction: [" + tmp + "]\n"
		eceIns.put(tmp)
	else:
		str4 = "\tExecuted Instruction:\n"
	
	write_sample_simulation(str3)
	write_sample_simulation(str4)

	write_sample_simulation("Pre-Issue Queue:\n")


	if preIssue.qsize() != 0:
		for x in range((preIssue.qsize())):
			tmp = preIssue.get()
			strn = "\tEntry "+ str(x) + ": [" + tmp + "]\n"
			preIssue.put(tmp)
			write_sample_simulation(strn)
		if (preIssue.qsize()) != 4:
			for x in range(4 - (preIssue.qsize())):
				strn = "\tEntry "+ str(x+(preIssue.qsize())) + ":\n"
				write_sample_simulation(strn)
	else:
		write_sample_simulation("\tEntry 0:\n")
		write_sample_simulation("\tEntry 1:\n")
		write_sample_simulation("\tEntry 2:\n")
		write_sample_simulation("\tEntry 3:\n")
	

	write_sample_simulation("Pre-ALU1 Queue:\n")
	if preAlu1.qsize() != 0:
		for x in range((preAlu1.qsize())):
			tmp = preAlu1.get()
			strn = "\tEntry "+ str(x) + ": [" + tmp + "]\n"
			preAlu1.put(tmp)
			write_sample_simulation(strn)
		if (preAlu1.qsize()) != 2:
			for x in range(2 - (preAlu1.qsize())):
				strn = "\tEntry "+ str(x+(preAlu1.qsize())) + ":\n"
				write_sample_simulation(strn)
	else:
		write_sample_simulation("\tEntry 0:\n")
		write_sample_simulation("\tEntry 1:\n")
	
	if preMem.empty():
		write_sample_simulation("Pre-MEM Queue:\n")
	else:
		tmp = preMem.get()
		str5 = "Pre-MEM Queue: " + "[" + tmp + "]\n"
		preMem.put(tmp)
		write_sample_simulation(str5)

	if postMem.empty():
		write_sample_simulation("Post-MEM Queue:\n")
	else:
		tmp = postMem.get()
		str6 = "Post-MEM Queue: " + "[" + tmp + "]\n"
		postMem.put(tmp)
		write_sample_simulation(str6)

	write_sample_simulation("Pre-ALU2 Queue:\n")
	for x in range((preAlu2.qsize())):
		tmp = preAlu2.get()
		strn = "\tEntry "+ str(x) + ": [" + tmp + "]\n"
		preAlu2.put(tmp)
		write_sample_simulation(strn)
	if (preAlu2.qsize()) != 2:
		for x in range(2 - (preAlu2.qsize())):
			strn = "\tEntry "+ str(x+(preAlu2.qsize())) + ":\n"
			write_sample_simulation(strn)

	if postAlu2.empty():
		write_sample_simulation("Post-ALU2 Queue:\n")
	else:
		tmp = postAlu2.get()
		str7 = "Post-ALU2 Queue: " + "[" + tmp + "]\n"
		postAlu2.put(tmp)
		write_sample_simulation(str7)
	
	write_sample_simulation("\n")
	write_sample_simulation("Registers\n")
	str8 = "R00:"
	for x in range(8):
		str8 = str8 + "\t" + str(register_all[x])
	str8 = str8 + "\n"
	write_sample_simulation(str8)
	str9 = "R08:"
	for x in range(8):
		str9 = str9 + "\t" + str(register_all[x+8])
	str9 = str9 + "\n"
	write_sample_simulation(str9)
	str10 = "R16:"
	for x in range(8):
		str10 = str10 + "\t" + str(register_all[x+16])
	str10 = str10 + "\n"
	write_sample_simulation(str10)
	str11 = "R24:"
	for x in range(8):
		str11 = str11 + "\t" + str(register_all[x+24])
	str11 = str11 + "\n"
	write_sample_simulation(str11)
	
	write_sample_simulation("\n")
	write_sample_simulation("Data\n")

	j = 0
	str12 = ""

	for key,value in data_memory.items():
		if j % 8 == 0:
			str12 = str12 + key + ":\t" + str(value)
			j = j + 1
			continue
		if j % 8 == 7:
			str12 = str12 + "\t" + str(value) + "\n"
			j = j + 1
			continue
		str12 = str12 + "\t" + str(value)
		j = j + 1
	write_sample_simulation(str12)


def branch_hazardcheck():
	waitIns1 = waitIns.get()
	waitIns.put(waitIns1)
	tmp_str1 = waitIns1.replace(',','')
	tmp_str = tmp_str1.split()
	read = []
	write = []
	return_flag = True
	if tmp_str[0] == "BEQ":
		read.append(tmp_str[1])
		read.append(tmp_str[2])
	if tmp_str[0] == "BGTZ" or tmp_str[0] == "BLTZ":
		read.append(tmp_str[1])
	
	#panduan preIssue
	qqsize = preIssue.qsize()
	for i in range(qqsize):
		tmp_str2 = preIssue.get()
		preIssue.put(tmp_str2)
		tmp_str2 = tmp_str2.replace(',','')
		tmp_str2 = tmp_str2.split()
		if tmp_str2[0] == "LW":
			if (tmp_str2[1] in read):
				return_flag = False
				continue
		elif tmp_str2[0] == "SW":
			continue
		else:
			if tmp_str2[1] in read:
				return_flag = False
				continue

	#panduan preAlu1
	qqsize2 = preAlu1.qsize()
	for i in range(qqsize2):
		tmp_str3 = preAlu1.get()
		preAlu1.put(tmp_str3)
		tmp_str3 = tmp_str3.replace(',','')
		tmp_str3 = tmp_str3.split()
		if tmp_str3[0] == "LW":
			if (tmp_str3[1] in read):
				return_flag = False
				continue
		elif tmp_str3[0] == "SW":
			continue
		else:
			if tmp_str3[1] in read:
				return_flag = False
				continue

	#panduan mem
	qqsize3 = preMem.qsize()
	for i in range(qqsize3):
		tmp_str4 = preMem.get()
		preMem.put(tmp_str4)
		tmp_str4 = tmp_str4.replace(',','')
		tmp_str4 = tmp_str4.split()
		if tmp_str4[0] == "LW":
			if (tmp_str4[1] in read):
				return_flag = False
				continue
		elif tmp_str4[0] == "SW":
			continue
		else:
			if tmp_str4[1] in read:
				return_flag = False
				continue

	#panduan postmem
	qqsize4 = postMem.qsize()
	for i in range(qqsize4):
		tmp_str5 = postMem.get()
		postMem.put(tmp_str5)
		tmp_str5 = tmp_str5.replace(',','')
		tmp_str5 = tmp_str5.split()
		if tmp_str5[0] == "LW":
			if (tmp_str5[1] in read):
				return_flag = False
				continue
		elif tmp_str5[0] == "SW":
			continue
		else:
			if tmp_str5[1] in read:
				return_flag = False
				continue

	#panduan preAlu2
	qqsize5 = preAlu2.qsize()
	for i in range(qqsize5):
		tmp_str6 = preAlu2.get()
		preAlu2.put(tmp_str6)
		tmp_str6 = tmp_str6.replace(',','')
		tmp_str6 = tmp_str6.split()
		if tmp_str6[0] == "LW":
			if (tmp_str6[1] in read):
				return_flag = False
				continue
		elif tmp_str6[0] == "SW":
			continue
		else:
			if tmp_str6[1] in read:
				return_flag = False
				continue

	#panduan postAlu2
	qqsize6 = postAlu2.qsize()
	for i in range(qqsize6):
		tmp_str7 = postAlu2.get()
		postAlu2.put(tmp_str7)
		tmp_str7 = tmp_str7.replace(',','')
		tmp_str7 = tmp_str7.split()
		if tmp_str7[0] == "LW":
			if (tmp_str7[1] in read):
				return_flag = False
				continue
		elif tmp_str7[0] == "SW":
			continue
		else:
			if tmp_str7[1] in read:
				return_flag = False
				continue
	return return_flag

def issue_all_hazardcheck():
	if preIssue.qsize() == 0:
		return -1
	preIssue1 = preIssue.get()
	preIssue.put(preIssue1)
	tmp_str1 = preIssue1.replace(',','')
	tmp_str = tmp_str1.split()
	read_first = []
	write_first = []
	first_process = []
	read_second = []
	write_second = []
	num_of_ins = 0
	num_of_ins_unusual = 0
	process_check = []
	tmp_write = []
	tmp_read = []

	flag1234[0] = 0
	flag1234[1] = 0
	flag1234[2] = 0
	flag1234[3] = 0
	flagSW = 0

	if tmp_str[0] == "LW":
		write_first.append(tmp_str[1])
		tmp2 = tmp_str[2].split('(')
		read_first.append(tmp2[1][:-1])
		if check_lw() and hazard_check_little(read_first,write_first):
			num_of_ins = 1
			flag1234[0] = 1
			process_check.append("lsw")
	elif tmp_str[0] == "SW":
		flagSW = 1
		read_first.append(tmp_str[1])
		tmp2 = tmp_str[2].split('(')
		read_first.append(tmp2[1][:-1])
		if hazard_check_little(read_first,write_first):
			num_of_ins = 1
			flag1234[0] = 1
			process_check.append("lsw")
	elif tmp_str[0] == "SLL" or tmp_str[0] == "SRA" or tmp_str[0] == "SRL" or tmp_str[0] == "ADDI" or tmp_str[0] == "ANDI" or tmp_str[0] == "ORI" or tmp_str[0] == "XORI":
		read_first.append(tmp_str[2])
		write_first.append(tmp_str[1])
		if hazard_check_little(read_first,write_first):
			num_of_ins = 1
			flag1234[0] = 1
			process_check.append("alu")
	else:
		read_first.append(tmp_str[2])
		read_first.append(tmp_str[3])
		write_first.append(tmp_str[1])
		if hazard_check_little(read_first,write_first):
			num_of_ins = 1
			flag1234[0] = 1
			process_check.append("alu")
	first_process.append(tmp_str[0])
	
	#panduan preIssue       #under have 2instr
	qqsize = preIssue.qsize()
	for i in range(qqsize - 1):
		tmp_str2 = preIssue.get()
		preIssue.put(tmp_str2)
		tmp_str2 = tmp_str2.replace(',','')
		tmp_str2 = tmp_str2.split()

		# instr 2
		if i == 0:
			if tmp_str2[0] == "LW":
				if check_lw() and flagSW == 0:
					if (tmp_str2[1] in read_first) or (tmp_str2[1] in write_first) or (tmp_str2[2][4:-1] in write_first):
						flag1234[1] = 0
					else:
						if "lsw" in process_check:
							flag1234[1] = 0
						else:
							tmp_write.append(tmp_str2[1])
							tmp_read.append(tmp_str2[2][4:-1])
							if hazard_check_little(tmp_read,tmp_write):
								flag1234[1] = 1
								num_of_ins = num_of_ins + 1
								write_first.append(tmp_str2[1])
								read_first.append(tmp_str2[2][4:-1])
								process_check.append("lsw")
								tmp_write = []
								tmp_read = []

			elif tmp_str2[0] == "SW":
				flagSW = 1
				if (tmp_str2[1] in write_first) or (tmp_str2[2][4:-1] in write_first):
					flag1234[1] = 0
				else:
					if "lsw" in process_check:
						flag1234[1] = 0
					else:
						tmp_read.append(tmp_str2[1])
						tmp_read.append(tmp_str2[2][4:-1])
						if hazard_check_little(tmp_read,tmp_write):
							flag1234[1] = 1
							num_of_ins = num_of_ins + 1
							read_first.append(tmp_str2[1])
							read_first.append(tmp_str2[2][4:-1])
							process_check.append("lsw")
							tmp_write = []
							tmp_read = []

			else:
				if tmp_str2[0] == "SLL" or tmp_str2[0] == "SRA" or tmp_str2[0] == "SRL" or tmp_str2[0] == "ADDI" or tmp_str2[0] == "ANDI" or tmp_str2[0] == "ORI" or tmp_str2[0] == "XORI":
					if (tmp_str2[1] in read_first) or (tmp_str2[2] in write_first) or (tmp_str2[1] in write_first):
						flag1234[1] = 0
					else:
						if "alu" in process_check:
							flag1234[1] = 0
						else:
							tmp_write.append(tmp_str2[1])
							tmp_read.append(tmp_str2[2])
							if hazard_check_little(tmp_read,tmp_write):
								flag1234[1] = 1
								num_of_ins = num_of_ins + 1
								write_first.append(tmp_str2[1])
								read_first.append(tmp_str2[2])
								process_check.append("alu")
								tmp_write = []
								tmp_read = []
				else:
					if (tmp_str2[1] in read_first) or (tmp_str2[1] in write_first) or (tmp_str2[2] in write_first) or (tmp_str2[3] in write_first):
						flag1234[1] = 0
					else:
						if "alu" in process_check:
							flag1234[1] = 0
						else:
							tmp_write.append(tmp_str2[1])
							tmp_read.append(tmp_str2[2])
							tmp_read.append(tmp_str2[3])
							if hazard_check_little(tmp_read,tmp_write):
								flag1234[1] = 1
								num_of_ins = num_of_ins + 1
								write_first.append(tmp_str2[1])
								read_first.append(tmp_str2[2])
								read_first.append(tmp_str2[3])
								process_check.append("alu")
								tmp_write = []
								tmp_read = []
		# instr 3
		if i == 1:
			if tmp_str2[0] == "LW" :
				if check_lw() and flagSW == 0:
					if (tmp_str2[1] in read_first) or (tmp_str2[1] in write_first) or (tmp_str2[2][4:-1] in write_first):
						flag1234[2] = 0
					else:
						if "lsw" in process_check:
							flag1234[2] = 0
						else:
							tmp_write.append(tmp_str2[1])
							tmp_read.append(tmp_str2[2][4:-1])
							if hazard_check_little(tmp_read,tmp_write):
								flag1234[2] = 1
								num_of_ins = num_of_ins + 1
								write_first.append(tmp_str2[1])
								read_first.append(tmp_str2[2][4:-1])
								process_check.append("lsw")
								tmp_write = []
								tmp_read = []

			elif tmp_str2[0] == "SW":
				flagSW = 1
				if (tmp_str2[1] in write_first) or (tmp_str2[2][4:-1] in write_first):
					flag1234[2] = 0
				else:
					if "lsw" in process_check:
						flag1234[2] = 0
					else:
						tmp_read.append(tmp_str2[1])
						tmp_read.append(tmp_str2[2][4:-1])
						if hazard_check_little(tmp_read,tmp_write):
							flag1234[2] = 1
							num_of_ins = num_of_ins + 1
							read_first.append(tmp_str2[1])
							read_first.append(tmp_str2[2][4:-1])
							process_check.append("lsw")
							tmp_write = []
							tmp_read = []

			else:
				if tmp_str2[0] == "SLL" or tmp_str2[0] == "SRA" or tmp_str2[0] == "SRL" or tmp_str2[0] == "ADDI" or tmp_str2[0] == "ANDI" or tmp_str2[0] == "ORI" or tmp_str2[0] == "XORI":
					if (tmp_str2[1] in read_first) or (tmp_str2[2] in write_first) or (tmp_str2[1] in write_first):
						flag1234[2] = 0
					else:
						if "alu" in process_check:
							flag1234[2] = 0
						else:
							tmp_write.append(tmp_str2[1])
							"""third"""
							tmp_read.append(tmp_str2[2])
							if hazard_check_little(tmp_read,tmp_write):
								flag1234[2] = 1
								num_of_ins = num_of_ins + 1
								write_first.append(tmp_str2[1])
								"""forth"""
								read_first.append(tmp_str2[2])
								process_check.append("alu")
								tmp_write = []
								tmp_read = []
				else:
					if (tmp_str2[1] in read_first) or (tmp_str2[1] in write_first) or (tmp_str2[2] in write_first) or (tmp_str2[3] in write_first):
						flag1234[2] = 0
					else:
						if "alu" in process_check:
							flag1234[2] = 0
						else:
							tmp_write.append(tmp_str2[1])
							tmp_read.append(tmp_str2[2])
							tmp_read.append(tmp_str2[3])
							if hazard_check_little(tmp_read,tmp_write):
								flag1234[2] = 1
								num_of_ins = num_of_ins + 1
								write_first.append(tmp_str2[1])
								read_first.append(tmp_str2[2])
								read_first.append(tmp_str2[3])
								process_check.append("alu")
								tmp_write = []
								tmp_read = []
		# instr 4
		if i == 2:
			if tmp_str2[0] == "LW" :
				if check_lw() and flagSW == 0:
					if (tmp_str2[1] in read_first) or (tmp_str2[1] in write_first) or (tmp_str2[2][4:-1] in write_first):
						flag1234[3] = 0
					else:
						if "lsw" in process_check:
							flag1234[3] = 0
						else:
							tmp_write.append(tmp_str2[1])
							tmp_read.append(tmp_str2[2][4:-1])
							if hazard_check_little(tmp_read,tmp_write):
								flag1234[3] = 1
								num_of_ins = num_of_ins + 1
								write_first.append(tmp_str2[1])
								read_first.append(tmp_str2[2][4:-1])
								process_check.append("lsw")
								tmp_write = []
								tmp_read = []

			elif tmp_str2[0] == "SW":
				flagSW = 1
				if (tmp_str2[1] in write_first) or (tmp_str2[2][4:-1] in write_first):
					flag1234[3] = 0
				else:
					if "lsw" in process_check:
						flag1234[3] = 0
					else:
						tmp_read.append(tmp_str2[1])
						tmp_read.append(tmp_str2[2][4:-1])
						if hazard_check_little(tmp_read,tmp_write):
							flag1234[3] = 1
							num_of_ins = num_of_ins + 1
							read_first.append(tmp_str2[1])
							read_first.append(tmp_str2[2][4:-1])
							process_check.append("lsw")
							tmp_write = []
							tmp_read = []
			else:
				if tmp_str2[0] == "SLL" or tmp_str2[0] == "SRA" or tmp_str2[0] == "SRL" or tmp_str2[0] == "ADDI" or tmp_str2[0] == "ANDI" or tmp_str2[0] == "ORI" or tmp_str2[0] == "XORI":
					if (tmp_str2[1] in read_first) or (tmp_str2[2] in write_first) or (tmp_str2[1] in write_first):
						flag1234[3] = 0
					else:
						if "alu" in process_check:
							flag1234[3] = 0
						else:
							tmp_write.append(tmp_str2[1])
							tmp_read.append(tmp_str2[2])
							""" 
								first
							"""
							if hazard_check_little(tmp_read,tmp_write):
								flag1234[3] = 1
								num_of_ins = num_of_ins + 1
								write_first.append(tmp_str2[1])
								"""
									second
								"""
								read_first.append(tmp_str2[2])
								process_check.append("alu")
								tmp_write = []
								tmp_read = []
				else:
					if (tmp_str2[1] in read_first) or (tmp_str2[1] in write_first) or (tmp_str2[2] in write_first) or (tmp_str2[3] in write_first):
						flag1234[3] = 0
					else:
						if "alu" in process_check:
							flag1234[3] = 0
						else:
							tmp_write.append(tmp_str2[1])
							tmp_read.append(tmp_str2[2])
							tmp_read.append(tmp_str2[3])
							if hazard_check_little(tmp_read,tmp_write):
								flag1234[3] = 1
								num_of_ins = num_of_ins + 1
								write_first.append(tmp_str2[1])
								read_first.append(tmp_str2[2])
								read_first.append(tmp_str2[3])
								process_check.append("alu")
								tmp_write = []
								tmp_read = []
	return num_of_ins



def check_lw():
	return_flag = True
	qqsize2 = preAlu1.qsize()
	for i in range(qqsize2):
		tmp_str3 = preAlu1.get()
		preAlu1.put(tmp_str3)
		tmp_str3 = tmp_str3.replace(',','')
		tmp_str3 = tmp_str3.split()
		if tmp_str3[0] == "SW":
			return_flag =  False
			continue

	#panduan mem
	qqsize3 = preMem.qsize()
	for i in range(qqsize3):
		tmp_str4 = preMem.get()
		preMem.put(tmp_str4)
		tmp_str4 = tmp_str4.replace(',','')
		tmp_str4 = tmp_str4.split()
		if tmp_str4[0] == "SW":
			return_flag =  False
			continue

	#panduan postmem
	qqsize4 = postMem.qsize()
	for i in range(qqsize4):
		tmp_str5 = postMem.get()
		postMem.put(tmp_str5)
		tmp_str5 = tmp_str5.replace(',','')
		tmp_str5 = tmp_str5.split()
		if tmp_str5[0] == "SW":
			return_flag =  False
			continue

	#panduan preAlu2
	qqsize5 = preAlu2.qsize()
	for i in range(qqsize5):
		tmp_str6 = preAlu2.get()
		preAlu2.put(tmp_str6)
		tmp_str6 = tmp_str6.replace(',','')
		tmp_str6 = tmp_str6.split()
		if tmp_str6[0] == "SW":
			return_flag =  False
			continue

	#panduan postAlu2
	qqsize6 = postAlu2.qsize()
	for i in range(qqsize6):
		tmp_str7 = postAlu2.get()
		postAlu2.put(tmp_str7)
		tmp_str7 = tmp_str7.replace(',','')
		tmp_str7 = tmp_str7.split()
		if tmp_str7[0] == "SW":
			return_flag =  False
			continue
	return return_flag
		
def hazard_check_little(read,write):
	#panduan preAlu1
	return_flag = True
	qqsize2 = preAlu1.qsize()
	for i in range(qqsize2):
		tmp_str3 = preAlu1.get()
		preAlu1.put(tmp_str3)
		tmp_str3 = tmp_str3.replace(',','')
		tmp_str3 = tmp_str3.split()
		if tmp_str3[0] == "LW":
			if (tmp_str3[1] in read) or (tmp_str3[1] in write):
			#if (tmp_str3[1] in read) or (tmp_str3[2][4:-1] in write) or (tmp_str3[1] in write):
				return_flag =  False
				continue
		elif tmp_str3[0] == "SW":
			if (tmp_str3[1] in write):
			#if (tmp_str3[1] in write) or (tmp_str3[2][4:-1] in write):
				return_flag =  False
				continue
		else:
			if (tmp_str3[1] in read) or (tmp_str3[1] in write):
			#if (tmp_str3[1] in read) or (tmp_str3[1] in write) or (tmp_str3[2] in write) or (tmp_str3[3] in write):
				return_flag =  False
				continue

	#panduan mem
	qqsize3 = preMem.qsize()
	for i in range(qqsize3):
		tmp_str4 = preMem.get()
		preMem.put(tmp_str4)
		tmp_str4 = tmp_str4.replace(',','')
		tmp_str4 = tmp_str4.split()
		if tmp_str4[0] == "LW":
			if (tmp_str4[1] in read) or (tmp_str4[1] in write):
				return_flag =  False
				continue
		elif tmp_str4[0] == "SW":
			if (tmp_str4[1] in write):
				return_flag =  False
				continue
		else:
			if (tmp_str4[1] in read) or (tmp_str4[1] in write):
				return_flag =  False
				continue

	#panduan postmem
	qqsize4 = postMem.qsize()
	for i in range(qqsize4):
		tmp_str5 = postMem.get()
		postMem.put(tmp_str5)
		tmp_str5 = tmp_str5.replace(',','')
		tmp_str5 = tmp_str5.split()
		if tmp_str5[0] == "LW":
			if (tmp_str5[1] in read) or (tmp_str5[1] in write):
				return_flag =  False
				continue
		elif tmp_str5[0] == "SW":
			if (tmp_str5[1] in write):
				return_flag =  False
				continue
		else:
			if (tmp_str5[1] in read) or (tmp_str5[1] in write):
				return_flag =  False
				continue

	#panduan preAlu2
	qqsize5 = preAlu2.qsize()
	for i in range(qqsize5):
		tmp_str6 = preAlu2.get()
		preAlu2.put(tmp_str6)
		tmp_str6 = tmp_str6.replace(',','')
		tmp_str6 = tmp_str6.split()
		if tmp_str6[0] == "LW":
			if (tmp_str6[1] in read) or (tmp_str6[1] in write):
				return_flag =  False
				continue
		elif tmp_str6[0] == "SW":
			if (tmp_str6[1] in write):
				return_flag =  False
				continue
		else:
			if (tmp_str6[1] in read) or (tmp_str6[1] in write):
				return_flag =  False
				continue

	#panduan postAlu2
	qqsize6 = postAlu2.qsize()
	for i in range(qqsize6):
		tmp_str7 = postAlu2.get()
		postAlu2.put(tmp_str7)
		tmp_str7 = tmp_str7.replace(',','')
		tmp_str7 = tmp_str7.split()
		if tmp_str7[0] == "LW":
			if (tmp_str7[1] in read) or (tmp_str7[1] in write):
				return_flag =  False
				continue
		elif tmp_str7[0] == "SW":
			if (tmp_str7[1] in write):
				return_flag =  False
				continue
		else:
			if (tmp_str7[1] in read) or (tmp_str7[1] in write):
				return_flag =  False
				continue
	return return_flag


def just_go():
	if not postAlu2.empty():
		handle(postAlu2.get(),1)

	if not preAlu2.empty():
		postAlu2.put(preAlu2.get())

	if not postMem.empty():
		handle(postMem.get(),1)

	if not preMem.empty():
		tmp = preMem.get()
		preMem.put(tmp)
		tmp = tmp.replace(',','')
		tmp = tmp.split()
		if tmp[0] == "SW":
			handle(preMem.get(),1)
		else:
			postMem.put(preMem.get())

	if not preAlu1.empty():
		preMem.put(preAlu1.get())

	if not preIssue.empty():
		for x in range(preIssue.qsize()):
			tmp = preIssue.get()

			if flag1234[x] == 1:
				if tmp[0:2] == "LW" or tmp[0:2] == "SW":
					preAlu1.put(tmp)
				else:
					preAlu2.put(tmp)
			else:
				preIssue.put(tmp)

def just_go2():
	if not postAlu2.empty():
		handle(postAlu2.get(),1)

	if not preAlu2.empty():
		postAlu2.put(preAlu2.get())

	if not postMem.empty():
		handle(postMem.get(),1)

	if not preMem.empty():
		tmp = preMem.get()
		preMem.put(tmp)
		tmp = tmp.replace(',','')
		tmp = tmp.split()
		if tmp[0] == "SW":
			handle(preMem.get(),1)
		else:
			postMem.put(preMem.get())

	if not preAlu1.empty():
		preMem.put(preAlu1.get())

#------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	"""
		for disassembly file
	"""
	data_all = []
	data_dict = {}  # used to print data in simulation
	content = ""
	address = 256
	instruction = []
	content = read_file()
	lines = len(content)     #lines of the input file

	for i in range(lines):
		mid = content[i]
		content[i] = mid[0:-1]

	for i in range(lines):
		if (content[i][0] == "0") & (content[i][1] == "1"):
			category1(instruction,content[i])
			address += 4
		elif (content[i][0] == "1") & (content[i][1] == "1"):
			category2(instruction,content[i])
			address += 4
		#data
		elif (content[i][0] == "1") & (content[i][1] == "0"):
			num = bintonegative(content[i])
			data_all.append(int(num))
			disassembly = content[i] + "\t" + str(address) + "\t" + num
			#print(disassembly)    #tiao shi xin xi
			disassembly  = disassembly + "\n"
			write_sample_disassembly(disassembly)
			address += 4
		elif (content[i][0] == "0") & (content[i][1] == "0"):
			num = bintopositive(content[i])
			data_all.append(int(num))
			disassembly = content[i] + "\t" + str(address) + "\t" + num
			#print(disassembly)    #tiao shi xin xi
			disassembly  = disassembly + "\n"
			write_sample_disassembly(disassembly)
			address += 4
	"""
		for new simulation file
	"""
	cycle2 = 0
	enddd = 0
	content2 = ""
	content2 = read_file_disassembly()
	lines2 = len(content2)
	dict_sim_ba = {}
	dict_sim_ai = {}
	dict_sim_ia = {}
	dict_sim_aii = {}

	preIssue = queue.Queue(4)
	preAlu1 = queue.Queue(2)
	preMem = queue.Queue(1)
	postMem = queue.Queue(1)
	preAlu2 = queue.Queue(2)
	postAlu2 = queue.Queue(1)
	waitIns = queue.Queue(1)
	eceIns = queue.Queue(1)
	register_all = [0] * 32
	data_memory = {}

	flag1234 = [0] * 4

	for i in range(lines2):
		mid2 = content2[i]
		content2[i] = mid2[0:-1]
		bin_tmp = content2[i][0:32]
		address_tmp = content2[i][33:36]
		ins_tmp = content2[i][37:]

		if len(ins_tmp) <= 2:
			data_memory[address_tmp] = ins_tmp
			continue
		dict_sim_ba[bin_tmp] = address_tmp
		dict_sim_ai[address_tmp] = ins_tmp
		dict_sim_aii[address_tmp] = i + 1

#get all the registers and data in memory
#begin to pipeline
	i = 0
	hu = 0
	while i < lines2:
		#preissue condition
		if hu == 0:
			hu = 1
			#process first instr
			if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
				waitIns.put(content2[i][37:])
				if not branch_hazardcheck():
					just_go()
					cycle2 = cycle2 + 1
					sim_print(cycle2)
					continue
				else:
					waitIns.get()
					eceIns.put(content2[i][37:])
					cycle2 = cycle2 + 1
					sim_print(cycle2)
					continue
			elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
				eceIns.put(content2[i][37:])
				cycle2 = cycle2 + 1
				sim_print(cycle2)
				continue
			elif content2[i][0:32] == "00000000000000000000000000000000":
				eceIns.put(content2[i][37:])
				i = i + 1
			else:
				preIssue.put(content2[i][37:])
				i = i + 1

			#process second instr
			if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
				waitIns.put(content2[i][37:])
			elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
				eceIns.put(content2[i][37:])
			elif content2[i][0:32] == "00000000000000000000000000000000":
				eceIns.put(content2[i][37:])
			else:
				preIssue.put(content2[i][37:])
			i = i + 1
			cycle2 = cycle2 + 1
			sim_print(cycle2)
			continue

#_---------------------------zheng shi kai shi
		#i != 0
		if waitIns.qsize() != 0:
			if not branch_hazardcheck():   #beq and has hazard
				issue_all_hazardcheck()
				just_go()
				cycle2 = cycle2 + 1
				sim_print(cycle2)		
				continue
			else:
				eceIns.put(waitIns.get())
				issue_all_hazardcheck()
				just_go()
				cycle2 = cycle2 + 1	
				sim_print(cycle2)			
				continue

		if content2[i][0:32] == "01010100000000000000000000001101":
			eceIns.put("BREAK")
			num_of_ins =  issue_all_hazardcheck()
			just_go()
			cycle2 = cycle2 + 1
			sim_print(cycle2)
			break


		if eceIns.qsize() != 0:
			tmpp = eceIns.get()
			k = handle(tmpp,0)
			tmpp = tmpp.replace(',','')
			tmpp = tmpp.split()
			if tmpp[0] == "NOP":
				i = i + 1
			if tmpp[0] == "J":
				if k >= 0:
					i = k - 1
				if k < 0:
					i = i + 1
			if tmpp[0] == "BEQ" or tmpp[0] == "BLTZ" or tmpp[0] == "BGTZ":
				if k >= 0:
					i = i + k
				if k < 0:
					i = i + 1
			if content2[i][0:32] == "01010100000000000000000000001101":
				eceIns.put("BREAK")
				num_of_ins =  issue_all_hazardcheck()
				just_go()
				cycle2 = cycle2 + 1
				sim_print(cycle2)
				break


#----------------------------------real zheng shi kai shi
		if preIssue.qsize() == 0:      #0
			#process first instr
			
			if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
				waitIns.put(content2[i][37:])
				if not branch_hazardcheck():
					just_go()
					cycle2 = cycle2 + 1
					sim_print(cycle2)
					continue
				else:
					waitIns.get()
					eceIns.put(content2[i][37:])
					just_go()
					cycle2 = cycle2 + 1
					sim_print(cycle2)
					continue
			elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
				eceIns.put(content2[i][37:])
				just_go()
				cycle2 = cycle2 + 1
				sim_print(cycle2)
				continue
			elif content2[i][0:32] == "00000000000000000000000000000000":
				eceIns.put(content2[i][37:])
				i = i + 1
			else:
				preIssue.put(content2[i][37:])
				i = i + 1


			#process second instr
			if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
				waitIns.put(content2[i][37:])
			elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
				eceIns.put(content2[i][37:])
			elif content2[i][0:32] == "00000000000000000000000000000000":
				eceIns.put(content2[i][37:])
				i = i + 1
			else:
				preIssue.put(content2[i][37:])
				i = i + 1
				just_go2()
			cycle2 = cycle2 + 1
			sim_print(cycle2)
			continue

		flag_issue = issue_all_hazardcheck()

		if preIssue.qsize() == 4:     #4
			if flag_issue == 0:
				if not postAlu2.empty():
					handle(postAlu2.get(),1)

				if not preAlu2.empty():
					postAlu2.put(preAlu2.get())

				if not postMem.empty():
					handle(postMem.get(),1)

				if not preMem.empty():
					tmp = preMem.get()
					preMem.put(tmp)
					tmp = tmp.replace(',','')
					tmp = tmp.split()
					if tmp[0] == "SW":
						handle(preMem.get(),1)
					else:
						postMem.put(preMem.get())

				if not preAlu1.empty():
					preMem.put(preAlu1.get())
				cycle2 = cycle2 + 1
				sim_print(cycle2)
				continue
			if flag_issue == 1:
				just_go()
				cycle2 = cycle2 + 1
				sim_print(cycle2)
				continue
			if flag_issue == 2:
				just_go()
				just_go()
				cycle2 = cycle2 + 1
				sim_print(cycle2)
				continue

		if preIssue.qsize() == 3:     #3
			if flag_issue == 0:
				if not postAlu2.empty():
					handle(postAlu2.get(),1)
				if not preAlu2.empty():
					postAlu2.put(preAlu2.get())
				if not postMem.empty():
					handle(postMem.get(),1)
				if not preMem.empty():
					tmp = preMem.get()
					preMem.put(tmp)
					tmp = tmp.replace(',','')
					tmp = tmp.split()
					if tmp[0] == "SW":
						handle(preMem.get(),1)
					else:
						postMem.put(preMem.get())
				if not preAlu1.empty():
					preMem.put(preAlu1.get())

				if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
					waitIns.put(content2[i][37:])
					if not branch_hazardcheck():    #has hazard
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
					else:
						waitIns.get()
						eceIns.put(content2[i][37:])
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
				elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
					eceIns.put(content2[i][37:])
					cycle2 = cycle2 + 1
					sim_print(cycle2)
					continue
				elif content2[i][0:32] == "00000000000000000000000000000000":
					eceIns.put(content2[i][37:])
					i = i + 1
				else:
					preIssue.put(content2[i][37:])
					i = i + 1

				cycle2 = cycle2 + 1
				sim_print(cycle2)
				continue

			if flag_issue == 1:
				just_go()

				if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
					waitIns.put(content2[i][37:])
					if not branch_hazardcheck():    #has hazard
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
					else:
						waitIns.get()
						eceIns.put(content2[i][37:])
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
				elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
					eceIns.put(content2[i][37:])
					cycle2 = cycle2 + 1
					sim_print(cycle2)
					continue
				elif content2[i][0:32] == "00000000000000000000000000000000":
					eceIns.put(content2[i][37:])
					i = i + 1
				else:
					preIssue.put(content2[i][37:])
					i = i + 1

				cycle2 = cycle2 + 1
				sim_print(cycle2)
				continue

			if flag_issue == 2:
				just_go()
				just_go()
				if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
					waitIns.put(content2[i][37:])
					if not branch_hazardcheck():    #has hazard
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
					else:
						waitIns.get()
						eceIns.put(content2[i][37:])
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
				elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
					eceIns.put(content2[i][37:])
					cycle2 = cycle2 + 1
					sim_print(cycle2)
					continue
				elif content2[i][0:32] == "00000000000000000000000000000000":
					eceIns.put(content2[i][37:])
					i = i + 1
				else:
					preIssue.put(content2[i][37:])
					i = i + 1

				cycle2 = cycle2 + 1
				sim_print(cycle2)
				continue

		if preIssue.qsize() == 2:       #2
			if flag_issue == 0:
				if not postAlu2.empty():
					handle(postAlu2.get(),1)
				if not preAlu2.empty():
					postAlu2.put(preAlu2.get())
				if not postMem.empty():
					handle(postMem.get(),1)
				if not preMem.empty():
					tmp = preMem.get()
					preMem.put(tmp)
					tmp = tmp.replace(',','')
					tmp = tmp.split()
					if tmp[0] == "SW":
						handle(preMem.get(),1)
					else:
						postMem.put(preMem.get())
				if not preAlu1.empty():
					preMem.put(preAlu1.get())
				#first instr
				if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
					waitIns.put(content2[i][37:])
					if not branch_hazardcheck():    #has hazard
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
					else:
						waitIns.get()
						eceIns.put(content2[i][37:])
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
				elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
					eceIns.put(content2[i][37:])
					cycle2 = cycle2 + 1
					sim_print(cycle2)
					continue
				elif content2[i][0:32] == "00000000000000000000000000000000":
					eceIns.put(content2[i][37:])
					i = i + 1
				else:
					preIssue.put(content2[i][37:])
					i = i + 1
				#second instr
				if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
					waitIns.put(content2[i][37:])
				elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
					eceIns.put(content2[i][37:])
				elif content2[i][0:32] == "00000000000000000000000000000000":
					eceIns.put(content2[i][37:])
					i = i + 1
				else:
					preIssue.put(content2[i][37:])
					i = i + 1
				cycle2 = cycle2 + 1
				sim_print(cycle2)
			if flag_issue == 1:
				just_go()
				if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
					waitIns.put(content2[i][37:])
					if not branch_hazardcheck():    #has hazard
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
					else:
						waitIns.get()
						eceIns.put(content2[i][37:])
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
				elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
					eceIns.put(content2[i][37:])
					cycle2 = cycle2 + 1
					sim_print(cycle2)
					continue
				elif content2[i][0:32] == "00000000000000000000000000000000":
					eceIns.put(content2[i][37:])
					i = i + 1
				else:
					preIssue.put(content2[i][37:])
					i = i + 1
				#second instr
				if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
					waitIns.put(content2[i][37:])
				elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
					eceIns.put(content2[i][37:])
				elif content2[i][0:32] == "00000000000000000000000000000000":
					eceIns.put(content2[i][37:])
					i = i + 1
				else:
					preIssue.put(content2[i][37:])
					i = i + 1
				cycle2 = cycle2 + 1
				sim_print(cycle2)
				continue

			if flag_issue == 2:
				just_go()
				just_go()
				if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
					waitIns.put(content2[i][37:])
					if not branch_hazardcheck():    #has hazard
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
					else:
						waitIns.get()
						eceIns.put(content2[i][37:])
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
				elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
					eceIns.put(content2[i][37:])
					cycle2 = cycle2 + 1
					sim_print(cycle2)
					continue
				elif content2[i][0:32] == "00000000000000000000000000000000":
					eceIns.put(content2[i][37:])
					i = i + 1
				else:
					preIssue.put(content2[i][37:])
					i = i + 1

				#second instr
				if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
					waitIns.put(content2[i][37:])
				elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
					eceIns.put(content2[i][37:])
				elif content2[i][0:32] == "00000000000000000000000000000000":
					eceIns.put(content2[i][37:])
					i = i + 1
				else:
					preIssue.put(content2[i][37:])
					i = i + 1
				cycle2 = cycle2 + 1
				sim_print(cycle2)
				continue

		if preIssue.qsize() == 1:
			if flag_issue == 0:
				if not postAlu2.empty():
					handle(postAlu2.get(),1)
				if not preAlu2.empty():
					postAlu2.put(preAlu2.get())
				if not postMem.empty():
					handle(postMem.get(),1)
				if not preMem.empty():
					tmp = preMem.get()
					preMem.put(tmp)
					tmp = tmp.replace(',','')
					tmp = tmp.split()
					if tmp[0] == "SW":
						handle(preMem.get(),1)
					else:
						postMem.put(preMem.get())
				if not preAlu1.empty():
					preMem.put(preAlu1.get())
				#first instr
				if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
					waitIns.put(content2[i][37:])
					if not branch_hazardcheck():    #has hazard
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
					else:
						waitIns.get()
						eceIns.put(content2[i][37:])
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
				elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
					eceIns.put(content2[i][37:])
					cycle2 = cycle2 + 1
					sim_print(cycle2)
					continue
				elif content2[i][0:32] == "00000000000000000000000000000000":
					eceIns.put(content2[i][37:])
					i = i + 1
				else:
					preIssue.put(content2[i][37:])
					i = i + 1
				#second instr
				if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
					waitIns.put(content2[i][37:])
				elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
					eceIns.put(content2[i][37:])
				elif content2[i][0:32] == "00000000000000000000000000000000":
					eceIns.put(content2[i][37:])
					i = i + 1
				else:
					preIssue.put(content2[i][37:])
					i = i + 1
				cycle2 = cycle2 + 1
				sim_print(cycle2)
			if flag_issue == 1:
				just_go()
				#first instr
				if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
					waitIns.put(content2[i][37:])
					if not branch_hazardcheck():    #has hazard
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
					else:
						waitIns.get()
						eceIns.put(content2[i][37:])
						cycle2 = cycle2 + 1
						sim_print(cycle2)
						continue
				elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
					eceIns.put(content2[i][37:])
					cycle2 = cycle2 + 1
					sim_print(cycle2)
					continue
				elif content2[i][0:32] == "00000000000000000000000000000000":
					eceIns.put(content2[i][37:])
					i = i + 1
				else:
					preIssue.put(content2[i][37:])
					i = i + 1
				#second instr
				if content2[i][0:6] == "010010" or content2[i][0:6] == "010011" or content2[i][0:6] == "010100":
					waitIns.put(content2[i][37:])
				elif content2[i][0:6] == "010000" or content2[i][0:6] == "010001":
					eceIns.put(content2[i][37:])
				elif content2[i][0:32] == "00000000000000000000000000000000":
					eceIns.put(content2[i][37:])
					i = i + 1
				else:
					preIssue.put(content2[i][37:])
					i = i + 1
				cycle2 = cycle2 + 1
				sim_print(cycle2)
		flag1234 = [0] * 4

