@ECHO OFF

REM A file declaring commands for working with the Sphinx based documentation.
REM
REM Used on windows computers from a terminal like
REM
REM   make.bat <buildername>
REM
REM <buildername> should be recognized by "sphinx-build -M <buildername>" or via
REM manually added commands in this file.
REM
REM ref: https://www.sphinx-doc.org/en/master/man/sphinx-build.html#options
REM

pushd %~dp0

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=_build

if "%1" == "" goto help
if "%1" == "devenv" goto devenv
goto default


:help
%SPHINXBUILD% -M help "%SOURCEDIR%" "%BUILDDIR%" %SPHINXOPTS%
goto end


:default
%SPHINXBUILD% -M %1 "%SOURCEDIR%" "%BUILDDIR%" %SPHINXOPTS%
goto end


:devenv
sphinx-autobuild -b html --open-browser "%SOURCEDIR%" "%BUILDDIR%/html" %SPHINXOPTS%
goto end


:end
popd
