# FileManager.InstallRevitEngineVersion Method

Parent Object: [FileManager](../FileManager/FileManager.md)

## Description

Method that tries to install specified Revit engine and returns the installation status. The installation is asynchronous, and this returns kInstallationInProcessStatus if the installation is started.

## Syntax

FileManager.**InstallRevitEngineVersion**( ***RevitEngineVersion*** As String ) As [InstallationStatusEnum](../InstallationStatusEnum.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RevitEngineVersion | String | Input String value that specifies the Revit engine version(e.g. “Revit 2025”) to install. |

## Version

Introduced in version 2025
