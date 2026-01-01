# DXF2DImportOptions.planarEntity Property

Parent Object: [DXF2DImportOptions](DXF2DImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DXF2DImportOptions.h>

## Description

Gets and sets the construction plane or planar face that defines the plane that the resulting sketches will be created on.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dXF2DImportOptions\_var" is a variable referencing a DXF2DImportOptions object. |

"dXF2DImportOptions\_var" is a variable referencing a DXF2DImportOptions object. ```` ``` #include <Core/Application/DXF2DImportOptions.h>  // Get the value of the property. Ptr<Base> propertyValue = dXF2DImportOptions_var->planarEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = dXF2DImportOptions_var->planarEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |