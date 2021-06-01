TEXOPTIONS=--lualatex --halt-on-error --interaction=nonstopmode --shell-escape --output-directory=build

all: build/testing.pdf


build/testing.pdf: FORCE | build
	max_print_line=1048576 \
	TEXINPUTS=../../.tex:../../.tex/beamertheme-vertex: \
	latexmk $(TEXOPTIONS) testing.tex


preview: FORCE | build
	max_print_line=1048576 \
	TEXINPUTS=../../.tex:../../.tex/beamertheme-vertex: \
	latexmk -pvc $(TEXOPTIONS) testing.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:


.PHONY: all clean FORCE
