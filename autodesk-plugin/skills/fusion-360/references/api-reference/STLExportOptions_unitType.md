# STLExportOptions.unitType Property

Parent Object: [STLExportOptions](STLExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/STLExportOptions.h>

## Description

Gets and sets the units to use for the created STL file. When the STLExportOptions object is created, this property is initialized with the default units specified for the Design.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object. |

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object. ```` ``` #include <Fusion/Fusion/STLExportOptions.h>  // Get the value of the property. DistanceUnits propertyValue = sTLExportOptions_var->unitType();  // Set the value of the property, where value_var is a DistanceUnits. bool returnValue = sTLExportOptions_var->unitType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DistanceUnits](DistanceUnits.htm).

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |