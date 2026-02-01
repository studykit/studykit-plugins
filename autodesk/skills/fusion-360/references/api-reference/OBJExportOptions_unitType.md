# OBJExportOptions.unitType Property

Parent Object: [OBJExportOptions](OBJExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/OBJExportOptions.h>

## Description

Gets and sets the units to use for the created OBJ file. The default is Centimeters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"oBJExportOptions\_var" is a variable referencing an OBJExportOptions object. |

"oBJExportOptions\_var" is a variable referencing an OBJExportOptions object. ```` ``` #include <Fusion/Fusion/OBJExportOptions.h>  // Get the value of the property. DistanceUnits propertyValue = oBJExportOptions_var->unitType();  // Set the value of the property, where value_var is a DistanceUnits. bool returnValue = oBJExportOptions_var->unitType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DistanceUnits](DistanceUnits.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |