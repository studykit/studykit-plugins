# CAM.genericPostFolder Property

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Gets the installed post folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a CAM object. |

"cAM\_var" is a variable referencing a CAM object. ```` ``` #include <Cam/CAM/CAM.h>  // Get the value of the property. string propertyValue = cAM_var->genericPostFolder(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Post Toolpaths API Sample](PostToolpaths_Sample_Sample.htm) | Demonstrates posting toolpaths in the active document. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |