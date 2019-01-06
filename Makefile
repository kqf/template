.PHONY: all 

all: model/*.py
	@# Check endpoints and install if needed
	@which solution > /dev/null || pip install -e .
	solution --data data/
