from .target import Target
from ..assemblers.keystone_arm import KeystoneArm
from ..disassemblers.capstone_arm import CapstoneArm
from ..compilers.clang_arm import ClangArm
from ..binfmt_tools.elf import ELF
from ..binary_analyzers.angr import Angr
from ..utils.utils import Utils
from ..allocation_management.allocation_management import AllocationManager


class ElfArmLinux(Target):
    NOP_BYTES = b"\x00\xF0\x20\xE3"  # TODO: thumb
    NOP_SIZE = 4
    JMP_ASM = "b {dst}"
    JMP_SIZE = 4

    @staticmethod
    def detect_target(binary_path):
        with open(binary_path, "rb") as f:
            magic = f.read(0x14)
            if magic.startswith(b"\x7fELF") and magic.startswith(
                b"\x28\x00", 0x12
            ):  # EM_ARM
                return True
        return False

    def get_assembler(self, assembler="keystone"):
        if assembler == "keystone":
            return KeystoneArm(self.p)
        raise NotImplementedError()

    def get_allocation_manager(self, allocation_manager="default"):
        if allocation_manager == "default":
            return AllocationManager(self.p)
        raise NotImplementedError()

    def get_compiler(self, compiler="clang"):
        if compiler == "clang":
            return ClangArm(self.p, compiler_flags=["-target", "arm-linux-gnueabihf"])
        raise NotImplementedError()

    def get_disassembler(self, disassembler="capstone"):
        if disassembler == "capstone":
            return CapstoneArm(self.p)
        raise NotImplementedError()

    def get_binfmt_tool(self, binfmt_tool="pyelftools"):
        if binfmt_tool == "pyelftools":
            return ELF(self.p, self.binary_path)
        raise NotImplementedError()

    def get_binary_analyzer(self, binary_analyzer="angr"):
        if binary_analyzer == "angr":
            return Angr(self.binary_path)
        raise NotImplementedError()

    def get_utils(self):
        return Utils(self.p, self.binary_path)