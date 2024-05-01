NAME="vmaf-grapher"
MAIN_SCRIPT="$(NAME).py"

SOURCE_DIR="src/"
OUTPUT_DIR="bin/"
BUILD_DIR="build/"
SPECS_DIR="build/specs/"

INSTALL_GLOBAL=false

build:
	@# Create the output directory if it doesn't exist
	@mkdir -p "$(OUTPUT_DIR)"
	@mkdir -p "$(BUILD_DIR)"
	@mkdir -p "$(SPECS_DIR)"

	@# Compile to executable using PyInstaller
	@pyinstaller --onefile "$(SOURCE_DIR)/$(MAIN_SCRIPT)" --distpath="$(OUTPUT_DIR)" --workpath="$(BUILD_DIR)" --specpath="$(SPECS_DIR)" --name="$(NAME)"

	@# Ensure it can be executed
	@chmod +x "$(OUTPUT_DIR)$(NAME)"

	@# Conditional installation to /usr/local/bin based on INSTALL_GLOBAL
	@if [ "$(INSTALL_GLOBAL)" = "true" ]; then \
		if sudo -n true 2>/dev/null; then \
			sudo cp "$(OUTPUT_DIR)$(NAME)" /usr/local/bin && echo "Moving $(NAME) to /usr/local/bin"; \
		else \
			echo "sudo password required to install $(NAME) globally."; \
			sudo cp "$(OUTPUT_DIR)$(NAME)" /usr/local/bin && echo "Moving $(NAME) to /usr/local/bin"; \
		fi \
	else \
		echo "Global installation declined. Use 'make build INSTALL_GLOBAL=true' to install globally or manually edit the makefile."; \
	fi

run: build
	@./$(OUTPUT_DIR)$(NAME)

clean:
	@# Remove the build and specs directories
	@rm -rf "$(BUILD_DIR)" "$(SPECS_DIR)"

	@echo "Removed build directory."
	@echo "Removed specs directory."

cleanall: clean
	@# Remove the build, specs, and output directories
	@rm -rf "$(OUTPUT_DIR)"

	@echo "Removed output directory."

.PHONY: build run clean cleanall
