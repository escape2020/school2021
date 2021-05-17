all: build/packaging.pdf


build/packaging.pdf: FORCE | build
	TEXINPUTS=beamertheme-vertex: latexmk \
		--lualatex \
		--halt-on-error \
		--interaction=nonstopmode \
		--shell-escape \
		--output-directory=build \
		packaging.tex


build:
	mkdir -p build

clean:
	rm -rf build

FORCE:


.PHONY: all clean FORCE
