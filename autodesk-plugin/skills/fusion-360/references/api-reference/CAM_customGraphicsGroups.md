# CAM.customGraphicsGroups Property

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Returns the customGraphicsGroups object associated with the CAM product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a CAM object. |

"cAM\_var" is a variable referencing a CAM object. ```` ``` #include <Cam/CAM/CAM.h>  // Get the value of the property. Ptr<CustomGraphicsGroups> propertyValue = cAM_var->customGraphicsGroups(); ``` ```` |

## Property Value

This is a read only property whose value is a [CustomGraphicsGroups](CustomGraphicsGroups.htm).

## Version

Introduced in version May 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |