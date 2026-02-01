# TSplineBody.parentFormFeature Property

Parent Object: [TSplineBody](TSplineBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/TSpline/TSplineBody.h>

## Description

Returns the owning form feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tSplineBody\_var" is a variable referencing a TSplineBody object. |

"tSplineBody\_var" is a variable referencing a TSplineBody object. ```` ``` #include <Fusion/TSpline/TSplineBody.h>  // Get the value of the property. Ptr<FormFeature> propertyValue = tSplineBody_var->parentFormFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [FormFeature](FormFeature.htm).

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |