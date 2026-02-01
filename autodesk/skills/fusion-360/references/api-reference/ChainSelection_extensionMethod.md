# ChainSelection.extensionMethod Property

Parent Object: [ChainSelection](ChainSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ChainSelection.h>

## Description

Property that gets and sets extension method to use. The default is TangentExtension. Only applicable to open contours.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chainSelection\_var" is a variable referencing a ChainSelection object. |

"chainSelection\_var" is a variable referencing a ChainSelection object. ```` ``` #include <Cam/GeometrySelections/ChainSelection.h>  // Get the value of the property. ExtensionMethods propertyValue = chainSelection_var->extensionMethod();  // Set the value of the property, where value_var is an ExtensionMethods. bool returnValue = chainSelection_var->extensionMethod(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ExtensionMethods](ExtensionMethods.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |