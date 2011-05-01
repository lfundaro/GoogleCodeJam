import sys

# calculates the size of the rope loop given the two lists
# of ropes by color
def size_of_loop(list1,list2):
	
	#if any of the list is empty there is no loop
	if ((not list1) or (not list2)):
		return 0
	
	#order from greater to lower
	list1.sort(reverse=True)
	list2.sort(reverse=True)
	
	#calculate the maximum set of best sizes
	min_length = min(len(list1),len(list2))
	small_list_1 = list1[:min_length]
	small_list_2 = list2[:min_length]
	
	loop_size = sum(small_list_1) + sum(small_list_2) - (len(small_list_1)+len(small_list_2))
	return loop_size
	
def parse_file(in_file):
	num_cases = int(in_file.readline())
	cases = [num_cases,[],[]]
	for c in range(num_cases):
		num_values = int(in_file.readline())
		rope_list = in_file.readline().strip('\n').split()
		blue_list, red_list = parse_list(rope_list)
		cases[1].append(blue_list)
		cases[2].append(red_list)
		
	return cases
					
def parse_list(rope_list):
	blue_list = []
	red_list = []
	for e in rope_list:
		if e[-1]=='R':
			red_list.append(int(e[:-1]))
		else:
			blue_list.append(int(e[:-1]))			
	return [blue_list,red_list]
	
out_file = open('output.out','w+')
in_file = sys.stdin
num_cases, blue_list, red_list = parse_file(in_file)

for c in range(1,num_cases+1):
	case = 'Case #'+str(c)+': '
	result= case+ str(size_of_loop(blue_list[c-1],red_list[c-1]))+'\n'
	out_file.write(result)

