# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/custombot/my_robot/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/custombot/my_robot/build

# Utility rule file for run_tests_joy.

# Include the progress variables for this target.
include joy/CMakeFiles/run_tests_joy.dir/progress.make

run_tests_joy: joy/CMakeFiles/run_tests_joy.dir/build.make

.PHONY : run_tests_joy

# Rule to build all files generated by this target.
joy/CMakeFiles/run_tests_joy.dir/build: run_tests_joy

.PHONY : joy/CMakeFiles/run_tests_joy.dir/build

joy/CMakeFiles/run_tests_joy.dir/clean:
	cd /home/custombot/my_robot/build/joy && $(CMAKE_COMMAND) -P CMakeFiles/run_tests_joy.dir/cmake_clean.cmake
.PHONY : joy/CMakeFiles/run_tests_joy.dir/clean

joy/CMakeFiles/run_tests_joy.dir/depend:
	cd /home/custombot/my_robot/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/custombot/my_robot/src /home/custombot/my_robot/src/joy /home/custombot/my_robot/build /home/custombot/my_robot/build/joy /home/custombot/my_robot/build/joy/CMakeFiles/run_tests_joy.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : joy/CMakeFiles/run_tests_joy.dir/depend
