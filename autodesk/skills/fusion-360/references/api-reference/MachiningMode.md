# MachiningMode Enumerator

## Description

Specifies how to treat a surface group
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

## Methods

|  |  |  |
| --- | --- | --- |
| Name | Value | Description |
| Avoid\_MachiningMode | 0 | The tool avoids these surfaces while it machines nearby surfaces. The tool stays clear from the avoid surfaces by the specified clearances. |
| Fixture\_MachiningMode | 3 | The tool avoids these surfaces by the specified clearances. |
| Gouge\_MachiningMode | 2 | The tool does not actively avoid or machine these surfaces. However, if these surfaces are on the path of the tool then it may gouge and cut through them. |
| Machine\_MachiningMode | 1 | The tool machines the selected surfaces leaving stock on them according to the stock to leave value. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |