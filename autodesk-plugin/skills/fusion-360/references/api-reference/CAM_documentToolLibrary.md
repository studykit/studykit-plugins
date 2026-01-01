# CAM.documentToolLibrary Property

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Gets the document ToolLibrary. The ToolLibrary contains all tools used by any operation inside the document. Changes to the original ToolLibrary will not affect any operation because the document ToolLibrary is an independent copy.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a CAM object. |

"cAM\_var" is a variable referencing a CAM object. ```` ``` #include <Cam/CAM/CAM.h>  // Get the value of the property. Ptr<DocumentToolLibrary> propertyValue = cAM_var->documentToolLibrary(); ``` ```` |

## Property Value

This is a read only property whose value is a [DocumentToolLibrary](DocumentToolLibrary.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |