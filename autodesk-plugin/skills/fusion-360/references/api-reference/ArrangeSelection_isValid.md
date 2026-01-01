# ArrangeSelection.isValid Property

Parent Object: [ArrangeSelection](ArrangeSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ArrangeSelection.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeSelection\_var" is a variable referencing an ArrangeSelection object. |

"arrangeSelection\_var" is a variable referencing an ArrangeSelection object. ```` ``` #include <Cam/GeometrySelections/ArrangeSelection.h>  // Get the value of the property. boolean propertyValue = arrangeSelection_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |