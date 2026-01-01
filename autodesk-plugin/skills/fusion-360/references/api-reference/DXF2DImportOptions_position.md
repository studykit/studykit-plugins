# DXF2DImportOptions.position Property

Parent Object: [DXF2DImportOptions](DXF2DImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DXF2DImportOptions.h>

## Description

Gets and sets the X,Y offset position for the origin of the imported DXF data relative to the sketch origin. This defaults to (0,0) in a newly created DXF2DImportOptions object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dXF2DImportOptions\_var" is a variable referencing a DXF2DImportOptions object. |

"dXF2DImportOptions\_var" is a variable referencing a DXF2DImportOptions object. ```` ``` #include <Core/Application/DXF2DImportOptions.h>  // Get the value of the property. Ptr<Point2D> propertyValue = dXF2DImportOptions_var->position();  // Set the value of the property, where value_var is a Point2D. bool returnValue = dXF2DImportOptions_var->position(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point2D](Point2D.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |