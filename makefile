# include build/conanbuildinfo.mak

CXX=g++
CXXFLAGS=-g -Wall -std=c++1y -march=native -mtune=native -fopenmp -O3 
LINKS=sqlite3
#CXXASSEMBLYFLAGS=-S -g -fverbose-asm
SOURCES=$(wildcard src/*.cpp)
OBJS=$(SOURCES:.cpp=.o)
EXEC=main

# conan
CFLAGS          += $(CONAN_CFLAGS)
CXXFLAGS        += $(CONAN_CXXFLAGS)
CPPFLAGS        += $(addprefix -I, $(CONAN_INCLUDE_DIRS))
CPPFLAGS        += $(addprefix -D, $(CONAN_DEFINES))

all: $(EXEC)

$(EXEC): $(OBJS)
	$(CXX) $(CXXFLAGS) $(CPPFLAGS) $(OBJS) -o $@ -l $(LINKS)

# $(OBJS): $(SOURCES)

# alternative:
%.o: %.cpp
	$(CXX) $(CXXFLAGS) $(CPPFLAGS) -c $< -o $@

clean:
	rm -f $(EXEC) $(OBJS)

test: $(EXEC)
	./$(EXEC)
