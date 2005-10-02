# Makefile for source rpm: xorg-x11-drv-evdev
# $Id$
NAME := xorg-x11-drv-evdev
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
