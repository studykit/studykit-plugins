# ChainSelection.extensionType Property

Parent Object: [ChainSelection](ChainSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ChainSelection.h>

## Description

Property that gets and sets the desired extension type method. The default is DistanceCap. This is only applicable to open contours.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chainSelection\_var" is a variable referencing a ChainSelection object. |

"chainSelection\_var" is a variable referencing a ChainSelection object. ```` ``` #include <Cam/GeometrySelections/ChainSelection.h>  // Get the value of the property. ExtensionTypes propertyValue = chainSelection_var->extensionType();  // Set the value of the property, where value_var is an ExtensionTypes. bool returnValue = chainSelection_var->extensionType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ExtensionTypes](ExtensionTypes.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |