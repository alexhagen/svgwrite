@ECHO OFF
ECHO Running Python 2.7 tests
CALL test27.bat
ECHO Running Python 3.4 tests
CALL test34.bat
ECHO Running pypy tests
CALL testpypy.bat
