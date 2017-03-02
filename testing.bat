
SET "LOGS=logs\"
SET "TESTS=tests\"
SET "ERRORS=logs\errors\"
SET "LOG_MASTER=logs\LOG.txt"

SET /A "CANT_TESTS = 10"
SET /A "TESTS_FAILED = 0"


IF EXIST %LOGS%		RMDIR /Q /S %LOGS%
MD %LOGS%
MD %ERRORS%

python Yoyo.py

for /l %%i in (1, 1, %CANT_TESTS%) do (
	python Yoyo.py %TESTS%test%%i.jojo 2> %ERRORS%error%%i.txt > %LOGS%output%%i.txt
)


COPY nul %LOGS%LOG.txt > nul
ECHO. >> %LOG_MASTER%
for /l %%i in (1, 1, %CANT_TESTS%) do (
	for %%a in (%ERRORS%%error%%%i.txt) do (
		IF %%~za NEQ  0 (
			ECHO *************** Test %%i *************** >> %LOG_MASTER%
			COPY /b %LOG_MASTER% + %ERRORS%error%%i.txt  %LOG_MASTER%
			ECHO **************************************** >> %LOG_MASTER%
			ECHO. >> %LOG_MASTER%
			ECHO. >> %LOG_MASTER%

			SET /A "TESTS_FAILED += 1"
		)
	)
)


IF EXIST %ERRORS% 	RMDIR /Q /S %ERRORS%

SET /A "TESTS_PASSED = %CANT_TESTS% - %TESTS_FAILED%"
ECHO. >> %LOG_MASTER%
ECHO Tests: %CANT_TESTS% >> %LOG_MASTER%
ECHO Tests passed: %TESTS_PASSED% >> %LOG_MASTER%
ECHO Tests failed: %TESTS_FAILED% >> %LOG_MASTER%

MORE %LOG_MASTER%