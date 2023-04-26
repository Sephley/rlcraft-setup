import os
import requests
import shutil
import subprocess
import sys

# Set the download paths
launcher_url = "https://download.overwolf.com/install/Download?&PartnerId=4047"
rlcraft_url = "https://www.curseforge.com/minecraft/modpacks/rlcraft/download/4487646/file"
optifine_url = "https://optifine.net/downloadx?f=OptiFine_1.12.2_HD_U_G5.jar&x=ebada85b6c24f6e8c738ab7e4720fe78"
sildurs_url = "https://www.curseforge.com/minecraft/customization/sildurs-vibrant-shaders/download/4278029"

# Set the download and install paths
download_path = os.path.join(os.getcwd(), "downloads")
launcher_path = os.path.join(download_path, "CurseforgeLauncher.exe")
rlcraft_path = os.path.join(download_path, "rlcraft.zip")
optifine_path = os.path.join(download_path, "OptiFine_1.12.2_HD_U_G5.jar")
sildurs_path = os.path.join(download_path, "sildurs.zip")

minecraft_path = os.path.join(os.environ["APPDATA"], ".minecraft")
mods_path = os.path.join(minecraft_path, "mods")
shaderpacks_path = os.path.join(minecraft_path, "shaderpacks")

# Create the download directory if it doesn't exist
if not os.path.exists(download_path):
    os.makedirs(download_path)

# Download the Curseforge Launcher
print("Downloading Curseforge Launcher...")
response = requests.get(launcher_url)
with open(launcher_path, "wb") as file:
    file.write(response.content)

# Install the Curseforge Launcher
print("Installing Curseforge Launcher...")
subprocess.run([launcher_path, "-s", "-d", os.getcwd()])

# Download the RLcraft modpack
print("Downloading RLcraft...")
response = requests.get(rlcraft_url)
with open(rlcraft_path, "wb") as file:
    file.write(response.content)

# Install the RLcraft modpack
print("Installing RLcraft...")
shutil.unpack_archive(rlcraft_path, minecraft_path)

# Download Optifine
print("Downloading Optifine...")
response = requests.get(optifine_url)
with open(optifine_path, "wb") as file:
    file.write(response.content)

# Install Optifine
print("Installing Optifine...")
shutil.move(optifine_path, mods_path)

# Download Sildurs shaders
print("Downloading Sildurs shaders...")
response = requests.get(sildurs_url)
with open(sildurs_path, "wb") as file:
    file.write(response.content)

# Install Sildurs shaders
print("Installing Sildurs shaders...")
shutil.unpack_archive(sildurs_path, shaderpacks_path)

# Cleanup
print("Cleaning up...")
shutil.rmtree(download_path)

print("Installation complete.")
