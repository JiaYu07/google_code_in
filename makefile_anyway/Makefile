GCC=g++
Objects=grade.o line_chart.py

.PHONY: clean

main: $(Objects)
	$(GCC) -c $< -o $@
	python3 line_chart.py

grade.o: grade.cpp
	$(GCC) -c $< -o $@

clean: 
	@echo "clean..."
	-rm *.o

