import os
from pathlib import Path

def concatenate_css_files(directory, output_file, custom_order=None):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    css_files = os.listdir(directory)
    
    # Sort the files based on the custom order
    if custom_order:
        css_files.sort(key=lambda x: custom_order.index(x) if x in custom_order else float('inf'))
    
    with open(output_file, 'w') as outfile:
        for css_file in css_files:
            with open(os.path.join(directory, css_file), 'r') as infile:
                outfile.write(infile.read())

if __name__ == '__main__':
	os.chdir(Path(__file__).parent)
	concatenate_css_files("../core", "../recommended.css", custom_order=["base.css"])