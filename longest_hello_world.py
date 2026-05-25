"""
Enterprise-Grade, Massively Scalable, Asynchronous, Object-Oriented, 
Virtual-Machine-Driven Text Rendering Pipeline.
Target Output Architecture: 'Hello, World!'
"""

import sys
import time
import abc
import queue
import threading
from typing import List, Dict, Any, Optional

# ==============================================================================
# 1. EXCEPTION HIERARCHY
# ==============================================================================
class EnterpriseException(Exception):
    """Base exception class for the enterprise ecosystem."""
    pass

class VirtualMachineException(EnterpriseException):
    """Base exception for virtual machine runtime faults."""
    pass

class SegmentationFaultException(VirtualMachineException):
    """Thrown when memory access boundary conditions are breached."""
    pass

class InvalidOpcodeException(VirtualMachineException):
    """Thrown when the CPU encounters an unmapped instruction byte."""
    pass

class SystemInitializationException(EnterpriseException):
    """Thrown if the architectural factory fails to construct requirements."""
    pass

# ==============================================================================
# 2. ABSTRACT INTERFACES (BUSINESS LOGIC COUPLING)
# ==============================================================================
class ILogger(abc.ABC):
    @abc.abstractmethod
    def log_info(self, message: str) -> None: pass
    @abc.abstractmethod
    def log_debug(self, message: str) -> None: pass
    @abc.abstractmethod
    def log_error(self, message: str) -> None: pass

class IMemoryManagementUnit(abc.ABC):
    @abc.abstractmethod
    def allocate(self, size: int) -> None: pass
    @abc.abstractmethod
    def write(self, address: int, value: int) -> None: pass
    @abc.abstractmethod
    def read(self, address: int) -> int: pass

class IOutputDevice(abc.ABC):
    @abc.abstractmethod
    def write_byte(self, data: int) -> None: pass
    @abc.abstractmethod
    def flush(self) -> None: pass
    @abc.abstractmethod
    def shutdown(self) -> None: pass

class IInstructionDecoder(abc.ABC):
    @abc.abstractmethod
    def decode(self, opcode: int) -> str: pass

# ==============================================================================
# 3. CONCRETE INFRASTRUCTURE IMPLEMENTATIONS
# ==============================================================================
class EnterpriseStandardLogger(ILogger):
    def __init__(self, verbose: bool = False):
        self._verbose = verbose

    def log_info(self, message: str) -> None:
        if self._verbose:
            sys.stderr.write(f"[INFO] [{time.time()}] {message}\n")

    def log_debug(self, message: str) -> None:
        if self._verbose:
            sys.stderr.write(f"[DEBUG] [{time.time()}] {message}\n")

    def log_error(self, message: str) -> None:
        sys.stderr.write(f"[ERROR] [{time.time()}] {message}\n")

class MemoryManagementUnit(IMemoryManagementUnit):
    def __init__(self, logger: ILogger):
        self._logger = logger
        self._memory: List[int] = []
        self._is_allocated = False

    def allocate(self, size: int) -> None:
        self._logger.log_debug(f"Allocating {size} bytes of virtual system hardware memory.")
        self._memory = [0] * size
        self._is_allocated = True

    def write(self, address: int, value: int) -> None:
        if not self._is_allocated or address < 0 or address >= len(self._memory):
            raise SegmentationFaultException(f"Memory write violation at address location: {hex(address)}")
        self._memory[address] = value & 0xFF

    def read(self, address: int) -> int:
        if not self._is_allocated or address < 0 or address >= len(self._memory):
            raise SegmentationFaultException(f"Memory read violation at address location: {hex(address)}")
        return self._memory[address]

class AsynchronousOutputDevice(IOutputDevice):
    def __init__(self, logger: ILogger):
        self._logger = logger
        self._queue: queue.Queue[Optional[int]] = queue.Queue()
        self._buffer: List[int] = []
        self._thread = threading.Thread(target=self._consume_queue, daemon=True)
        self._thread.start()

    def write_byte(self, data: int) -> None:
        self._logger.log_debug(f"Asynchronous queue ingestion for byte: {data}")
        self._queue.put(data)

    def flush(self) -> None:
        self._logger.log_debug("Flushing asynchronous underlying stream buffer.")
        # Block until queue is processed
        while not self._queue.empty():
            time.sleep(0.001)

    def shutdown(self) -> None:
        self._queue.put(None)  # Sentinel value to terminate thread loop
        self._thread.join()

    def _consume_queue(self) -> None:
        while True:
            item = self._queue.get()
            if item is None:
                break
            self._buffer.append(item)
            # Instantly pipe to native stdout write stream
            sys.stdout.write(chr(item))
            sys.stdout.flush()
            self._queue.task_done()

class InstructionDecoder(IInstructionDecoder):
    def __init__(self):
        self._map = {
            0x01: "PUSH",
            0x02: "ADD",
            0x03: "SUB",
            0x04: "MUL",
            0x05: "OUT",
            0x06: "HALT"
        }

    def decode(self, opcode: int) -> str:
        if opcode in self._map:
            return self._map[opcode]
        raise InvalidOpcodeException(f"Opcode system fault: {hex(opcode)} cannot be mapped.")

# ==============================================================================
# 4. CENTRAL PROCESSING UNIT (CPU) RUNTIME ENGINE
# ==============================================================================
class CentralProcessingUnit:
    def __init__(self, mmu: IMemoryManagementUnit, decoder: IInstructionDecoder, device: IOutputDevice, logger: ILogger):
        self._mmu = mmu
        self._decoder = decoder
        self._device = device
        self._logger = logger
        self._stack: List[int] = []
        self._program_counter = 0
        self._execution_active = False

    def flash_bios_bytecode(self, executable_stream: List[int]) -> None:
        self._logger.log_info(f"Flashing executable binary stream ({len(executable_stream)} bytes) into stack memory.")
        for address, bytecode in enumerate(executable_stream):
            self._mmu.write(address, bytecode)

    def execute_lifecycle(self) -> None:
        self._execution_active = True
        self._program_counter = 0
        self._logger.log_info("CPU Lifecycle runtime execution sequence started.")

        while self._execution_active:
            opcode = self._mmu.read(self._program_counter)
            instruction = self._decoder.decode(opcode)
            self._logger.log_debug(f"FETCH-DECODE: PC {hex(self._program_counter)} -> Opcode {hex(opcode)} ({instruction})")

            if instruction == "PUSH":
                self._program_counter += 1
                data_value = self._mmu.read(self._program_counter)
                self._stack.append(data_value)
            elif instruction == "ADD":
                operand_b = self._stack.pop()
                operand_a = self._stack.pop()
                self._stack.append((operand_a + operand_b) & 0xFF)
            elif instruction == "SUB":
                operand_b = self._stack.pop()
                operand_a = self._stack.pop()
                self._stack.append((operand_a - operand_b) & 0xFF)
            elif instruction == "MUL":
                operand_b = self._stack.pop()
                operand_a = self._stack.pop()
                self._stack.append((operand_a * operand_b) & 0xFF)
            elif instruction == "OUT":
                target_byte = self._stack.pop()
                self._device.write_byte(target_byte)
            elif instruction == "HALT":
                self._execution_active = False
                self._logger.log_info("HALT instruction encountered. Breaking processing loops.")

            self._program_counter += 1

        self._device.flush()

# ==============================================================================
# 5. DEPENDENCY INJECTION ARCHITECTURE LAYER (FACTORY)
# ==============================================================================
class SystemArchitectureFactory:
    @staticmethod
    def construct_environment(verbose_logging: bool) -> tuple[CentralProcessingUnit, IOutputDevice]:
        logger = EnterpriseStandardLogger(verbose_logging)
        mmu = MemoryManagementUnit(logger)
        mmu.allocate(2048)  # Allocate 2KB memory layout
        decoder = InstructionDecoder()
        device = AsynchronousOutputDevice(logger)
        
        cpu = CentralProcessingUnit(mmu, decoder, device, logger)
        return cpu, device

# ==============================================================================
# 6. APPLICATION RUNTIME ENTRYPOINT
# ==============================================================================
def main() -> None:
    # Change verbose_logging to True if you want a massive stream of operational logs
    cpu, device = SystemArchitectureFactory.construct_environment(verbose_logging=False)

    # Virtual Machine ISA Definitions
    PUSH = 0x01
    ADD  = 0x02
    SUB  = 0x03
    MUL  = 0x04
    OUT  = 0x05
    HALT = 0x06

    # Highly complex mathematical bytecode representations to evaluate ASCII equivalents
    bytecode_binary_payload = [
        # Character: 'H' (ASCII 72) -> Evaluation: 8 * 9
        PUSH, 8, PUSH, 9, MUL, OUT,
        
        # Character: 'e' (ASCII 101) -> Evaluation: (10 * 10) + 1
        PUSH, 10, PUSH, 10, MUL, PUSH, 1, ADD, OUT,
        
        # Character: 'l' (ASCII 108) -> Evaluation: (10 * 10) + 8
        PUSH, 10, PUSH, 10, MUL, PUSH, 8, ADD, OUT,
        
        # Character: 'l' (ASCII 108) -> Evaluation: (10 * 10) + 8
        PUSH, 10, PUSH, 10, MUL, PUSH, 8, ADD, OUT,
        
        # Character: 'o' (ASCII 111) -> Evaluation: (11 * 10) + 1
        PUSH, 11, PUSH, 10, MUL, PUSH, 1, ADD, OUT,
        
        # Character: ',' (ASCII 44)  -> Evaluation: (4 * 10) + 4
        PUSH, 4, PUSH, 10, MUL, PUSH, 4, ADD, OUT,
        
        # Character: ' ' (ASCII 32)  -> Evaluation: 8 * 4
        PUSH, 8, PUSH, 4, MUL, OUT,
        
        # Character: 'W' (ASCII 87)  -> Evaluation: (8 * 10) + 7
        PUSH, 8, PUSH, 10, MUL, PUSH, 7, ADD, OUT,
        
        # Character: 'o' (ASCII 111) -> Evaluation: (11 * 10) + 1
        PUSH, 11, PUSH, 10, MUL, PUSH, 1, ADD, OUT,
        
        # Character: 'r' (ASCII 114) -> Evaluation: (11 * 10) + 4
        PUSH, 11, PUSH, 10, MUL, PUSH, 4, ADD, OUT,
        
        # Character: 'l' (ASCII 108) -> Evaluation: (10 * 10) + 8
        PUSH, 10, PUSH, 10, MUL, PUSH, 8, ADD, OUT,
        
        # Character: 'd' (ASCII 100) -> Evaluation: 10 * 10
        PUSH, 10, PUSH, 10, MUL, OUT,
        
        # Character: '!' (ASCII 33)  -> Evaluation: 11 * 3
        PUSH, 11, PUSH, 3, MUL, OUT,
        
        # Character: '\n' (ASCII 10) -> Evaluation: Direct 10
        PUSH, 10, OUT,
        
        # Structural Runtime Termination Sequence
        HALT
    ]

    try:
        cpu.flash_bios_bytecode(bytecode_binary_payload)
        cpu.execute_lifecycle()
    except EnterpriseException as runtime_error:
        sys.stderr.write(f"A critical fatal ecosystem error occurred: {runtime_error}\n")
    finally:
        device.shutdown()

if __name__ == "__main__":
    main()
