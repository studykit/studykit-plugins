# CAM.generateAllSetupSheets Method

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Generates all of the setup sheets for all of the operations in the document

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object.  ```` ``` #include <Cam/CAM/CAM.h>  // Uses no optional arguments. returnValue = cAM_var->generateAllSetupSheets(format, folder);  // Uses optional arguments. returnValue = cAM_var->generateAllSetupSheets(format, folder, openDocument); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| format | [SetupSheetFormats](SetupSheetFormats.htm) | The document format for the setup sheet. Valid options are HTMLFormat and ExcelFormat. Limitation: "ExcelFormat" can be used in windows OS only. |
| folder | string | The destination folder to locate the setup sheet documents in. |
| openDocument | boolean | An option to allow to open the document instantly after the generation. By default, the document is opened.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Generate Setup Sheets API Sample](GenerateSetupSheets_Sample_Sample.htm) | Demonstrates generating the setup sheets for an existing toolpath.. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |