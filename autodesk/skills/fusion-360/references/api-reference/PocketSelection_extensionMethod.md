# PocketSelection.extensionMethod Property

Parent Object: [PocketSelection](PocketSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/PocketSelection.h>

## Description

The desired extension method. TangentExtension by default.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pocketSelection\_var" is a variable referencing a PocketSelection object. |

"pocketSelection\_var" is a variable referencing a PocketSelection object. ```` ``` #include <Cam/GeometrySelections/PocketSelection.h>  // Get the value of the property. ExtensionMethods propertyValue = pocketSelection_var->extensionMethod();  // Set the value of the property, where value_var is an ExtensionMethods. bool returnValue = pocketSelection_var->extensionMethod(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ExtensionMethods](ExtensionMethods.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |