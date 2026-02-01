# ChainSelection.startExtensionLength Property

Parent Object: [ChainSelection](ChainSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ChainSelection.h>

## Description

Property that gets and sets the length of the extension of an open curve at the start of the chain. This is only applicable to open contours and when DistanceCap is chosen as the extension cap.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chainSelection\_var" is a variable referencing a ChainSelection object. |

"chainSelection\_var" is a variable referencing a ChainSelection object. ```` ``` #include <Cam/GeometrySelections/ChainSelection.h>  // Get the value of the property. double propertyValue = chainSelection_var->startExtensionLength();  // Set the value of the property, where value_var is a double. bool returnValue = chainSelection_var->startExtensionLength(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |