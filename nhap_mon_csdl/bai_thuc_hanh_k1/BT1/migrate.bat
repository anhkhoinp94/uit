@echo off
SET SERVER=host.containers.internal
SET DATABASE=quanlybanhang
SET USER=sa
SET PASSWORD=Passw0rd

SET SCRIPTS_FOLDER=%CD%

podman run --rm -it -v %SCRIPTS_FOLDER%/data:/sql mcr.microsoft.com/mssql-tools /bin/bash -c "/opt/mssql-tools/bin/sqlcmd -S %SERVER% -d %DATABASE% -U %USER% -P %PASSWORD% -i /sql/*.sql"

echo All scripts executed.
