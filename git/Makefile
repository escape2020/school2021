TEXOPTIONS=--lualatex --output-directory=build --halt-on-error --interaction=nonstopmode --shell-escape
TEXINPUTS=build:../.tex:../.tex/beamertheme-vertex:

all: build/git.pdf


build/git.pdf: FORCE
	TEXINPUTS=$(TEXINPUTS) latexmk $(TEXOPTIONS) git.tex

preview: FORCE
	TEXINPUTS=$(TEXINPUTS) latexmk $(TEXOPTIONS) -pvc git.tex

build/git.pdf: $(addprefix build/figures/, github.png bitbucket.png gitlab.png xkcd_git.png)


build/figures/github.png: | build/figures
	wget https://github-media-downloads.s3.amazonaws.com/GitHub-Logos.zip -O build/figures/GitHub-Logos.zip --no-use-server-timestamps
	cd build/figures && unzip GitHub-Logos.zip
	cp build/figures/GitHub-Logos/GitHub_Logo.png $@

build/figures/bitbucket.png: | build/figures
	wget https://www.atlassian.com/dam/jcr:e2a6f06f-b3d5-4002-aed3-73539c56a2eb/Bitbucket@2x-blue.png -O $@ --no-use-server-timestamps

build/figures/gitlab.png: | build/figures
	wget https://gitlab.com/gitlab-com/gitlab-artwork/raw/master/wordmark/wm_no_bg.png -O $@ --no-use-server-timestamps


build/figures/xkcd_git.png: | build/figures
	wget https://imgs.xkcd.com/comics/git_2x.png -O $@ --no-use-server-timestamps


build/figures:
	mkdir -p build/figures

clean:
	rm -rf build

FORCE:

.PHONY: all FORCE clean
