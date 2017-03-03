
SET "LOGS=logs\"
SET "LOGS_OUTPUT=logs\output"
SET "TESTS=tests\"
SET "TESTS_FILE=tests\test"
SET "ERRORS=logs\errors\"
SET "ERRORS_FILE=logs\errors\error"
SET "LOG_MASTER=logs\LOG.txt"

SET "PYCACHE=__pycache__\"
SET "PARSER=parser.out"
SET "PARSERTAB=parsetab.py"

SET /A "CANT_TESTS = 10"
SET /A "TESTS_FAILED = 0"


IF EXIST %LOGS%		RMDIR /Q /S %LOGS%
MD %LOGS%
MD %ERRORS%


COPY nul %LOGS%LOG.txt > nul



IF EXIST %PYCACHE%		RMDIR /Q /S %PYCACHE%
IF EXIST %PARSER%		del %PARSER%
IF EXIST %PARSERTAB%	del %PARSERTAB%


ECHO. >> %LOG_MASTER%
ECHO ************ Generar tablas ************ >> %LOG_MASTER%
python Yoyo.py 2>> %LOGS%LOG.txt
ECHO **************************************** >> %LOG_MASTER%
ECHO. >> %LOG_MASTER%
ECHO. >> %LOG_MASTER%

for /l %%i in (1, 1, %CANT_TESTS%) do (
	python Yoyo.py %TESTS_FILE%%%i.jojo 2> %ERRORS_FILE%%%i.txt > %LOGS_OUTPUT%%%i.txt
)

ECHO. >> %LOG_MASTER%
for /l %%i in (1, 1, %CANT_TESTS%) do (
	for /f %%a in ("%ERRORS_FILE%%%i.txt") do (
		IF %%~za NEQ  0 (
			ECHO *************** Test %%i *************** >> %LOG_MASTER%
			COPY /b %LOG_MASTER% + %ERRORS_FILE%%%i.txt  %LOG_MASTER%
			ECHO **************************************** >> %LOG_MASTER%
			ECHO. >> %LOG_MASTER%
			ECHO. >> %LOG_MASTER%

			SET /A "TESTS_FAILED += 1"
		)
	)
)

python Yoyo.py %TESTS_FILE%Final.jojo 2> %ERRORS_FILE%_Final.txt > %LOGS%outputFinal.txt

for /f %%a in ("%ERRORS_FILE%_Final.txt") do (
	IF %%~za NEQ  0 (
		ECHO *************** Test Final *************** >> %LOG_MASTER%
		COPY /b %LOG_MASTER% + %ERRORS_FILE%_Final.txt  %LOG_MASTER%
		ECHO ****************************************** >> %LOG_MASTER%
		ECHO. >> %LOG_MASTER%
		ECHO. >> %LOG_MASTER%

		SET /A "TESTS_FAILED += 1"
	)
)


IF EXIST %ERRORS% 	RMDIR /Q /S %ERRORS%

SET /A "TESTS_PASSED = (%CANT_TESTS% + 1) - %TESTS_FAILED%"
ECHO. >> %LOG_MASTER%
ECHO Tests: (%CANT_TESTS%+1) >> %LOG_MASTER%
ECHO Tests passed: %TESTS_PASSED% >> %LOG_MASTER%
ECHO Tests failed: %TESTS_FAILED% >> %LOG_MASTER%

MORE %LOG_MASTER%