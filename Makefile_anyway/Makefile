GCC=g++
Objects1=grade.o
Objects2= line_chart.py

.PHONY: clean test 

test: $(Objects1) $(Objects2)
	$(GCC)  $< -o $@  
	./test
	python3 $(Objects2)

grade.o: grade.cpp
	$(GCC) -c $< -o $@

clean: 
	rm -f *.o test

