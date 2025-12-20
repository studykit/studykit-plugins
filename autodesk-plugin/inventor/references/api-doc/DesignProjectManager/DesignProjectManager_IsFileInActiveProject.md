# DesignProjectManager.IsFileInActiveProject Method

Parent Object: [DesignProjectManager](../DesignProjectManager/DesignProjectManager.md)

## Description

Method that returns whether the given file is located within the active project using the resolution rules of the project, and additionally returns the path type (library, workspace, workgroup) and its name.

## Syntax

DesignProjectManager.**IsFileInActiveProject**( ***FileName*** As String, ***ProjectPathType*** As [LocationTypeEnum](../LocationTypeEnum.md), ***ProjectPathName*** As String ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileName | String | Input String that specifies the name of a file. This can either be a full file name (recommended), a relative file name or a file name with no path. |
| ProjectPathType | [LocationTypeEnum](../LocationTypeEnum.md) | Output LocationTypeEnum that returns where the input file was found. Possible returns values are: kLibraryLocation, kWorkspaceLocation, kWorkgroupLocation, kUnknownLocation (if none of the above or if the file is not found within the project). |
| ProjectPathName | String | Output String that returns the name of the library, workspace or workgroup that the file was found in. Returns a null string if none of the above. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |