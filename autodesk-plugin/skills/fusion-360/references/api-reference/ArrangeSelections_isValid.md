# ArrangeSelections.isValid Property

Parent Object: [ArrangeSelections](ArrangeSelections.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ArrangeSelections.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeSelections\_var" is a variable referencing an ArrangeSelections object. |

"arrangeSelections\_var" is a variable referencing an ArrangeSelections object. ```` ``` #include <Cam/GeometrySelections/ArrangeSelections.h>  // Get the value of the property. boolean propertyValue = arrangeSelections_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |