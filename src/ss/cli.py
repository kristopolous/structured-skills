import sys
import argparse
import json
from .decoder import Decoder
from .vm import VM

def main():
    parser = argparse.ArgumentParser(description="Structured Skills VM")
    parser.add_argument("file", nargs="?", help="The .ss file to run")
    parser.add_argument("--config", default="config.toml", help="Path to config file (default: %(default)s)")
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
        
    args = parser.parse_args()

    if not args.file:
        parser.print_help()
        sys.exit(1)

    try:
        with open(args.file, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File {args.file} not found.\n")
        parser.print_help()
        sys.exit(1)

    decoder = Decoder(config_path=args.config)
    
    program = []
    imports = []
    
    # Eagerly collect imports to provide context for the decoder
    for line in lines:
        if line.strip().startswith("import "):
            # Very basic extraction for context
            imports.append(line.strip())

    imports_context = "\n".join(imports)

    for i, line in enumerate(lines):
        if not line.strip() or line.strip().startswith("#"):
            continue
            
        opcodes = decoder.decode_line(line, imports_context=imports_context)
        program.extend(opcodes)

    vm = VM(config_path=args.config)
    vm.load_program(program)
    vm.run()

    print("\nFinal State:")
    for reg, val in vm.registers.items():
        # Truncate large values for display
        display_val = str(val)
        if len(display_val) > 100:
            display_val = display_val[:97] + "..."
        print(f"{reg}: {display_val}")

if __name__ == "__main__":
    main()
