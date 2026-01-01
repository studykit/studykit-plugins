# CAM.allOperations Property

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Gets a collection containing all of the operations in the document. This includes all operations nested in folders and patterns.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a CAM object. |

"cAM\_var" is a variable referencing a CAM object. ```` ``` #include <Cam/CAM/CAM.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = cAM_var->allOperations(); ``` ```` |

## Property Value

This is a read only property whose value is an [ObjectCollection](ObjectCollection.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Generate Setup Sheets API Sample](GenerateSetupSheets_Sample_Sample.htm) | Demonstrates generating the setup sheets for an existing toolpath.. |
| [Generate Toolpaths API Sample](GenerateToolpaths_Sample_Sample.htm) | Demonstrates generating the toolpaths in the active document. |
| [Create CAM Operation From Template API Sample](New_Operation_Sample_Sample.htm) | Demonstrates adding a new toolpath into the document using an existing CAM template. You can view the template [here](../ExtraFiles/face.f3dhsm-template), although it will be loaded automatically. Run the sample script within any Fusion project containing at least one setup. A new facing operation will be created at the end of each setup discovered. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |