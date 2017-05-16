# Usage Guide

## Description

## Options
For option parameters, pass in '-h': 

    $ mssql-scripter -h
    usage: mssql-scripter [-h] [--connection-string  | -S ] [-d] [-U] [-P] [-f]
                      [--data-only | --schema-and-data]
                      [--script-create | --script-drop | --script-drop-create]
                      [--target-server-version {2005,2008,2008R2,2012,2014,2016,vNext,AzureDB,AzureDW}]
                      [--target-server-edition {Standard,PersonalExpress,Enterprise,Stretch}]
                      [--include-objects [[...]]] [--exclude-objects [[...]]]
                      [--ansi-padding] [--append] [--check-for-existence] [-r]
                      [--convert-uddts] [--include-dependencies] [--headers]
                      [--constraint-names] [--unsupported-statements]
                      [--object-schema] [--bindings] [--collation]
                      [--defaults] [--extended-properties] [--logins]
                      [--object-permissions] [--owner] [--use-database]
                      [--statistics] [--change-tracking] [--check-constraints]
                      [--data-compressions] [--foreign-keys]
                      [--full-text-indexes] [--indexes] [--primary-keys]
                      [--triggers] [--unique-keys] [--display-progress]
                      [--enable-toolsservice-logging] [--version]

    Microsoft SQL Server Scripter Command Line Tool. Version 1.0.0a1

    optional arguments:
      -h, --help            show this help message and exit
      --connection-string   Connection string of database to script. If connection
                            string and server are not supplied, defaults to value
                            in Environment Variable
                            MSSQL_SCRIPTER_CONNECTION_STRING.
      -S , --server         Server name.
      -d , --database       Database name.
      -U , --user           Login ID for server.
      -P , --password       Password.
      -f , --file           Output file name.
      --data-only           Generate scripts that contains data only.
      --schema-and-data     Generate scripts that contain schema and data.
      --script-create       Script object CREATE statements.
      --script-drop         Script object DROP statements
      --script-drop-create  Script object CREATE and DROP statements.
      --target-server-version {2005,2008,2008R2,2012,2014,2016,vNext,AzureDB,AzureDW}
                            Script only features compatible with the specified SQL
                            Version.
      --target-server-edition {Standard,PersonalExpress,Enterprise,Stretch}
                            Script only features compatible with the specified SQL
                            Server database edition.
      --include-objects [ [ ...]]
                            Database objects to include in script.
      --exclude-objects [ [ ...]]
                            Database objects to exclude from script.
      --ansi-padding        Generates ANSI Padding statements.
      --append              Append script to file.
      --check-for-existence
                            Check for database object existence.
      -r, --continue-on-error
                            Continue scripting on error.
      --convert-uddts       Convert user-defined data types to base types.
      --include-dependencies
                            Generate script for the dependent objects for each
                            object scripted.
      --headers             Include descriptive headers for each object scripted.
      --constraint-names    Include system constraint names to enforce declarative
                            referential integrity.
      --unsupported-statements
                            Include statements in the script that are not
                            supported on the target SQL Server Version.
      --object-schema       Prefix object names with the object schema.
      --bindings            Script options to set binding options.
      --collation           Script the objects that use collation.
      --defaults            Script the default values.
      --extended-properties
                            Script the extended properties for each object
                            scripted.
      --logins              Script all logins available on the server, passwords
                            will not be scripted.
      --object-permissions  Generate object-level permissions.
      --owner               Script owner for the objects.
      --use-database        Generate USE DATABASE statement.
      --statistics          Script all statistics.
      --change-tracking     Script the change tracking information.
      --check-constraints   Script the check constraints for each table or view
                            scripted.
      --data-compressions   Script the data compression information.
      --foreign-keys        Script the foreign keys for each table scripted.
      --full-text-indexes   Script the full-text indexes for each table or indexed
                            view scripted.
      --indexes             Script the indexes (XML and clustered) for each table
                            or indexed view scripted.
      --primary-keys        Script the primary keys for each table or view
                            scripted.
      --triggers            Script the triggers for each table or view scripted.
      --unique-keys         Script the unique keys for each table or view
                            scripted.
      --display-progress    Display scripting progress.
      --enable-toolsservice-logging
                            Enable verbose logging.
      --version             show program's version number and exit

## Environment Variables
You can set environment variables for your connection string through the following steps:


    # set environment variable MSSQL_SCRIPTER_CONNECTION_STRING with a connection string.
    $ export MSSQL_SCRIPTER_CONNECTION_STRING='Server=myserver;Database=mydb;User Id=myuser;Password=mypassword;'
    $ mssql-scripter

    # set environment variable MSSQL_SCRIPTER_PASSWORD so no password input is required.
    $ export MSSQL_SCRIPTER_PASSWORD='ABC123'
    $ mssql-scripter -S localhost -d AdventureWorks -U sa

## Examples
Here are example commands that run against the AdventureWorks database:



    # generate DDL scripts for all objects in the Adventureworks database and save the script to a file
    $ mssql-scripter -S localhost -d AdventureWorks -U sa 

    # script the database schema and data to a file.
    $ mssql-scripter -S localhost -d AdventureWorks -U sa --schema-and-data  > ./adventureworks.sql

    # execute the generated above script with sqlcmd
    $ sqlcmd -S mytestserver -U sa -i ./adventureworks.sql
    
    # generate DDL scripts for objects that contain 'Employee' in their name to stdout
    $ mssql-scripter -S localhost -d AdventureWorks -U sa --include-objects Employee

    # generate DDL scripts for the dbo schema and pipe the output to a file
    $ mssql-scripter -S localhost -d AdventureWorks -U sa --include-objects dbo. > ./dboschema.sql
    
    # change a schema name in the generated DDL script
    # 1) generate DDL scripts for all objects in the Adventureworks database
    # 2) pipe generated script to sed and change all occurrences of SalesLT to SalesLT_test and save the script to a file
    $ mssql-scripter scripter -S localhost -d Adventureworks -U sa | sed -e "s/SalesLT./SalesLT_test./g" > adventureworks_SalesLT_test.sql 

    # script the all data to a file.
    $ mssql-scripter -S localhost -d AdventureWorks -U sa --data-only > ./adventureworks-data.sql 

   