# DesignProjects.AddExisting Method

Parent Object: [DesignProjects](../DesignProjects/DesignProjects.md)

## Description

Method that adds an existing project file to the list of project files. This is equivalent of browsing to a specific ipj file on disk and choosing it in the Projects editor dialog. If the design project is already in the collection, the corresponding DesignProject object is returned.

## Syntax

DesignProjects.**AddExisting**( ***FullFileName*** As String ) As [DesignProject](../DesignProject/DesignProject.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String that specifies the full file name of an Inventor project file with an .ipj extension. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |