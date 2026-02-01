# DXF2DImportOptions.isCreateControlPointSplines Property

Parent Object: [DXF2DImportOptions](DXF2DImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DXF2DImportOptions.h>

## Description

When set to true, if there are any splines in the DXF they will be created as control point splines. Otherwise they will be created as fixed splines that cannot be edited. The default for this property is false, to create fixed splines.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dXF2DImportOptions\_var" is a variable referencing a DXF2DImportOptions object. |

"dXF2DImportOptions\_var" is a variable referencing a DXF2DImportOptions object. ```` ``` #include <Core/Application/DXF2DImportOptions.h>  // Get the value of the property. boolean propertyValue = dXF2DImportOptions_var->isCreateControlPointSplines();  // Set the value of the property, where value_var is a boolean. bool returnValue = dXF2DImportOptions_var->isCreateControlPointSplines(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |