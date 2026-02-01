# Ellipse2D.majorRadius Property

Parent Object: [Ellipse2D](Ellipse2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Ellipse2D.h>

## Description

Gets and sets the major radius of the ellipse.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipse2D\_var" is a variable referencing an Ellipse2D object. |

"ellipse2D\_var" is a variable referencing an Ellipse2D object. ```` ``` #include <Core/Geometry/Ellipse2D.h>  // Get the value of the property. double propertyValue = ellipse2D_var->majorRadius();  // Set the value of the property, where value_var is a double. bool returnValue = ellipse2D_var->majorRadius(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |