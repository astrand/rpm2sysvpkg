
.PHONY: dist default all install rpm

default: all

all: 
	./setup.py build

install: 
	./setup.py install

rpm: 
	./setup.py bdist_rpm --release=1

dist:
# We distribute a .spec file, so that it's possible to run "rpm -ta rpm2sysvpkg.tgz"
	./setup.py bdist_rpm --spec-only 
	mv dist/rpm2sysvpkg.spec .
	./setup.py sdist
