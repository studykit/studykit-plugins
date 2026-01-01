# FormFeature.tSplineBodies Property

Parent Object: [FormFeature](FormFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FormFeature.h>

## Description

Returns a TSplineBodies collection where you can access any existing T-Spline bodies and through it create new T-Spline bodies.

## Syntax

* [Python](#Python)
* [C++](#C++)

"formFeature\_var" is a variable referencing a FormFeature object. |

"formFeature\_var" is a variable referencing a FormFeature object. ```` ``` #include <Fusion/Features/FormFeature.h>  // Get the value of the property. Ptr<TSplineBodies> propertyValue = formFeature_var->tSplineBodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [TSplineBodies](TSplineBodies.htm).

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |