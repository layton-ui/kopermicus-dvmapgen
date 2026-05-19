
print("Welcome to Monopoco's DV Map Generator!")

# === ask user for system (list presets) ===

presets = ["KSP", "RSS", "KSP + OPM", "KSP + OPM + K + PW + SV", "Custom"]

print("Available presets:")
for i, preset in enumerate(presets):
    print(f"{i + 1}. {preset}")

preset_choice = len(presets)  # default to custom

# TODO: refactor until !marker1

while True:
    try:
        preset_choice = input(f"Choose a preset (1-{len(presets)}), press enter for custom): ")
        if not preset_choice or preset_choice == 0:
            preset_choice = len(presets)
            break
        preset_choice = int(preset_choice)
        break
    except ValueError:
        print(f"Invalid input, please enter a number from 1 to {len(presets)}.")
    
if preset_choice < 1 or preset_choice > len(presets):
    print("Invalid choice, defaulting to custom.")
    preset_choice = len(presets)
    
# !marker1
    
"""
if custom is chosen:
    scan steam directory for KSP installations
    if none found, ask user to input path to KSP installation
    if still none found, continue with default values (KSP)
    if several found, ask user to choose which one to use
"""

class Installation:
    def __init__(self, name, path, origin):
        self.name = name
        self.path = path
        self.origin = origin # e.g. "steamscanner", "user"

installation_directories = []

if preset_choice == len(presets):
    print("Scanning for KSP installations...")
    
    # TODO: Implement code to scan steam directory for KSP installations
    
    steamscanner_implemented = False
    if steamscanner_implemented:        
        
        
        if not installation_directories:
            print("No KSP installations found in steam directory.")
    
    
    
    
    
    
    if not installation_directories:
        print(f"No KSP installations found.\nPlease enter the path to your KSP GameData directory.")
        ksp_path_input = input("Path to KSP GameData directory: ")
        if ksp_path_input:
            
            # TODO: test if path is valid
            ksp_path_valid = False # placeholder 
            
            if ksp_path_valid:
                print("Path is valid.")
            else:
                print("Path is invalid, defaulting to KSP preset.")
                preset_choice = 1
                installation_directories = []
            
            ksp_path_name_input = input("Name for this KSP installation: ")
            if not ksp_path_name_input:
                # count existing installations named "Custom KSP Installation" and append number to name
                existing_custom_installations = [inst for inst in installation_directories if inst.name.startswith("Custom KSP Installation")]
                ksp_path_name_input = f"Custom KSP Installation {len(existing_custom_installations) + 1}"
            
            installation_directories.append(Installation(ksp_path_name_input, ksp_path_input, "steamscanner"))
            
        else:
            print("No path entered, defaulting to KSP preset.")
            preset_choice = 1

    if len(installation_directories) > 1:
        print("Multiple KSP installations found:")
        for i, directory in enumerate(installation_directories):
            print(f"{i + 1}. {directory}")
        installation_choice = int(input(f"Choose an installation (1-{len(installation_directories)}): "))
        if installation_choice < 1 or installation_choice > len(installation_directories):
            print("Invalid choice, defaulting to first installation.")
            installation_choice = 1
        selected_installation = installation_directories[installation_choice - 1]
    


# === see if we can find a config file with the same name as the installation or preset, if so, load it and skip to map generation ===

import os
import json



# === read and parse system data from installation ===



# === generate dv map ===



# === save map to file ===



# === generate map in window ===



# === done - do not end program until user kills terminal ===

while True:
    pass