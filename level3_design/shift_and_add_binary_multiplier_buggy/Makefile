# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/ shift_and_add_binary_multiplier_buggy.v # provide your design path

TOPLEVEL := shift_and_add_binary_multiplier_buggy # design file
MODULE   := shift_and_add_binary_multiplier_tb # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
