CC=g++
EXE=print_gci_name.o
object=print_gci_name.cpp

main: $(EXE)S
	@$(CC)  $< -o $@
	@./main
EXE: $(object)
	$(CC)  $< -o $@
	
.PHONY: clean main EXE
clean:
	@Secho "clean....."
	-rm *.o main