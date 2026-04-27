# Test script for deterministic extraction
# Usage: python3 -m ss.cli tests/test_extraction.ss

for each $file in %list_files tests/data:
    $document = %read $file
    $location = infer the location from $document in a single line
    append $location to ./tests/locations.list using %write_file
end
