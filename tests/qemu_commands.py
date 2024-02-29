X86_32_LIB = "/lib32"
X64_64_LIB = "/lib64"
CROSS_DIR = "/usr"


AARCH64_COMMAND = ["qemu-aarch64", "-L", f"{CROSS_DIR}/aarch64-linux-gnu"]
ARM_COMMAND = ["qemu-arm", "-L", f"{CROSS_DIR}/arm-linux-gnueabihf"]
I386_COMMAND = [
    "qemu-i386",
    f"{X86_32_LIB}/ld-linux.so.2",
    "--library-path",
    X86_32_LIB
]
MIPS_COMMAND = ["qemu-mips", "-L", f"{CROSS_DIR}/mips-linux-gnu"]
MIPS64_COMMAND = ["qemu-mips64", "-L", f"{CROSS_DIR}/mips64-linux-gnuabi64"]
MIPS64EL_COMMAND = ["qemu-mips64el", "-L", f"{CROSS_DIR}/mips64el-linux-gnuabi64"]
MIPSEL_COMMAND = ["qemu-mipsel", "-L", f"{CROSS_DIR}/mipsel-linux-gnu"]
PPC_COMMAND = ["qemu-ppc", "-L", f"{CROSS_DIR}/powerpc-linux-gnu"]
PPC64_COMMAND = ["qemu-ppc64", "-L", f"{CROSS_DIR}/powerpc64-linux-gnu"]
PPC64_LE_COMMAND = ["qemu-ppc64le", "-L", f"{CROSS_DIR}/powerpc64le-linux-gnu"]
X86_64_COMMAND = ["qemu-x86_64",
    f"{X64_64_LIB}/ld-linux-x86-64.so.2",
    "--library-path",
    X64_64_LIB
]