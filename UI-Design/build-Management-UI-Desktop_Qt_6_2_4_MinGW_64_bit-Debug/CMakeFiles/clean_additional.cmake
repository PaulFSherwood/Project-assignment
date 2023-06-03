# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\Management-UI_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\Management-UI_autogen.dir\\ParseCache.txt"
  "Management-UI_autogen"
  )
endif()
