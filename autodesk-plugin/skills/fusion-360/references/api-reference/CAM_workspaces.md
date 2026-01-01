# CAM.workspaces Property

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Returns the workspaces associated with this product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a CAM object. |

"cAM\_var" is a variable referencing a CAM object. ```` ``` #include <Cam/CAM/CAM.h>  // Get the value of the property. Ptr<WorkspaceList> propertyValue = cAM_var->workspaces(); ``` ```` |

## Property Value

This is a read only property whose value is a [WorkspaceList](WorkspaceList.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |