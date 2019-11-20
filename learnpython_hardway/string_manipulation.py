
def make_version(version, release="maintenance"):
    version_list = version.split(".")
    if release == "major":       
        next_version_num = int(version_list[0])+1
        new_version = f"{str(next_version_num)}.0.0"
    elif release == "minor":
        next_version_num = int(version_list[1])+1
        new_version = f"{version_list[0]}.{str(next_version_num)}.0"
    else:
        next_version_num = int(version_list[2])+1
        new_version = f"{version_list[0]}.{version_list[1]}.{str(next_version_num)}"
    print(new_version)

make_version("4.145.145", "minor")