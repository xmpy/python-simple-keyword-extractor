# 
# Makefile to help automate tasks 
# This makefile imitate the makefile of (bookie https://github.com/bookieio/Bookie). Thx Bookie team :)
#

WD := $(shell pwd)
PY := bin/python
PIP := $(PY) bin/pip

BOOKIE_INI = bookie.ini
SAURL = $(shell grep sqlalchemy.url $(BOOKIE_INI) | cut -d "=" -f 2 | tr -d " ")

DEMOURL = http://127.0.0.1:9876

SYSDEPS_UBUNTU = build-essential python-dev libpq-dev git\
	       python-virtualenv unzip

SYSDEPS_MAC = python27 py27-virtualenv

.PHONY: clean_all
clean_all: clean_venv clean_archive


# install python and virtualenv
# Now only support UBUNTU and MAC
.PHONY: sysdeps
sysdeps:
	if which apt-get &> /dev/null; then \
		if [ $(NONINTERACTIVE) ]; then \
			sudo apt-get install -y $(SYSDEPS_UBUNTU); \
		else \
			sudo apt-get install $(SYSDEPS_UBUNTU); \
		fi \
	elif which port &> /dev/null; then \
		if [ $(NONINTERACTIVE) ]; then \
			sudo port install $(SYSDEPS_MAC); \
		else \
			sudo port install $(SYSDEPS_MAC); \
		fi; \
	fi

# DEPS
#
# Install the packages we need.

.PHONY: deps
deps: venv
	@echo "Installing the python package dependencies"
	$(PIP) install -f file:///archive -r requirements.txt

.PHONY: clean_archive
clean_archive:
	rm -rf archive

# install python and virtualenv

.PHONY: install
install: deps server


.PHONY: server
server: 
	@echo Starting the server, you can see the demo on: $(DEMOURL)
	$(PY) server.py



# INSTALL
#
# Crap to help us install and setup Bookie
# We need a virtualenv
.PHONY: venv
venv: bin/python
bin/python:
	virtualenv -p python2 .

.PHONY: clean_venv
clean_venv:
	rm -rf lib include local bin
