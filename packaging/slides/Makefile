TEXOPTIONS=--lualatex --halt-on-error --interaction=nonstopmode --shell-escape --output-directory=build

all: build/packaging.pdf


build/packaging.pdf: FORCE | build
	TEXINPUTS=../../.tex/beamertheme-vertex: latexmk $(TEXOPTIONS) packaging.tex


preview: FORCE | build
	TEXINPUTS=../../.tex/beamertheme-vertex: latexmk -pvc $(TEXOPTIONS) packaging.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:


.PHONY: all clean FORCE
