SOURCE_FILES := $(shell find lessons -type f)
TARGET_FILES := $(SOURCE_FILES:lessons/%=dist/%)

.PHONY: all
all: dist/index.md $(TARGET_FILES)


dist/index.md: create-index-md.py $(TARGET_FILES) 
	python3 "$<"

$(TARGET_FILES): dist/%: lessons/%
	@mkdir -p "$$(dirname "$@")"
	@cp "$<" "$@"
