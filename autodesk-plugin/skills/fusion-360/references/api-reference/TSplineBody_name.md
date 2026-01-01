# TSplineBody.name Property

Parent Object: [TSplineBody](TSplineBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/TSpline/TSplineBody.h>

## Description

Gets and sets the name of the body. If setting this property, there is the side-effect that the B-Rep body created from this T-Spline body is also renamed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tSplineBody\_var" is a variable referencing a TSplineBody object. |

"tSplineBody\_var" is a variable referencing a TSplineBody object. ```` ``` #include <Fusion/TSpline/TSplineBody.h>  // Get the value of the property. string propertyValue = tSplineBody_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = tSplineBody_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |