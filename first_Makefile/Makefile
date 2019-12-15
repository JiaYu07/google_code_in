CC=g++
EXE=print_gci_name.o
object=print_gci_name.cpp

main: $(EXE)
	$(CC)  $< -o $@
EXE: $(object)
	$(CC)  $< -o $@
	
.PHONY: clean main EXE
clean:
	@echo "clean....."
	-rm *.o