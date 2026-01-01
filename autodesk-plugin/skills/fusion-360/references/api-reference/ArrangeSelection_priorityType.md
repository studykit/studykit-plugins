# ArrangeSelection.priorityType Property

Parent Object: [ArrangeSelection](ArrangeSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ArrangeSelection.h>

## Description

Gets and sets the priority value for each element in the selection list. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. The default value for this property is MediumArrangePriorityType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeSelection\_var" is a variable referencing an ArrangeSelection object. |

"arrangeSelection\_var" is a variable referencing an ArrangeSelection object. ```` ``` #include <Cam/GeometrySelections/ArrangeSelection.h>  // Get the value of the property. ArrangePriorityTypes propertyValue = arrangeSelection_var->priorityType();  // Set the value of the property, where value_var is an ArrangePriorityTypes. bool returnValue = arrangeSelection_var->priorityType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ArrangePriorityTypes](ArrangePriorityTypes.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |