import platform

# Get a readable version of platform details
full_platform_info = platform.platform()
print("Full platform info:", full_platform_info)

# Get the machine type (e.g., 'i386', 'x86_64')
machine_type = platform.machine()
print("Machine type:", machine_type)

# Get the real processor name
processor_name = platform.processor()
print("Processor name:", processor_name)

# Get the system/OS name (e.g., 'Linux', 'Windows')
system_name = platform.system()
print("System name:", system_name)

# Get the system’s release version
system_version = platform.version()
print("System version:", system_version)

# Get the Python implementation (e.g., 'CPython', 'PyPy')
python_impl = platform.python_implementation()
print("Python implementation:", python_impl)

# Get Python version as a tuple
python_version = platform.python_version_tuple()
print("Python version tuple:", python_version)

# Practical uses of platform module:
# - Writing cross-platform applications
# - System monitoring and logging
# - Debugging and performance optimization
# - Conditional imports or functionality based on platform

