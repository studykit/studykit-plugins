# TSplineBody.entityToken Property

Parent Object: [TSplineBody](TSplineBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/TSpline/TSplineBody.h>

## Description

Returns a token for the TSplineBody object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same T-Spline body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tSplineBody\_var" is a variable referencing a TSplineBody object.  ```` ``` # Get the value of the property. propertyValue = tSplineBody_var.entityToken ``` ```` |

"tSplineBody\_var" is a variable referencing a TSplineBody object. ```` ``` #include <Fusion/TSpline/TSplineBody.h>  // Get the value of the property. string propertyValue = tSplineBody_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |