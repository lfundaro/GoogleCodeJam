
milshakes: milkshakes.o
	g++ -L /usr/local/lib -lgecodeint -lgecodesearch -lgecodekernel -lgecodesupport -lgecodedriver milkshakes.o -o milkshakes
milkshakes.o: milkshakes.cpp
	g++ -I /usr/local/include -c milkshakes.cpp