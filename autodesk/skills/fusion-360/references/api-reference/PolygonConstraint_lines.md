# PolygonConstraint.lines Property

Parent Object: [PolygonConstraint](PolygonConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PolygonConstraint.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polygonConstraint\_var" is a variable referencing a PolygonConstraint object.  ```` ``` # Get the value of the property. propertyValue = polygonConstraint_var.lines ``` ```` |

"polygonConstraint\_var" is a variable referencing a PolygonConstraint object. ```` ``` #include <Fusion/Sketch/PolygonConstraint.h>  // Get the value of the property. std::vector<Ptr<SketchLine>> propertyValue = polygonConstraint_var->lines(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [SketchLine](SketchLine.htm).

## Version

Introduced in version August 2016
Retired in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |