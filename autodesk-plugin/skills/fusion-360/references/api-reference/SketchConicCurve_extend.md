# SketchConicCurve.extend Method

Parent Object: [SketchConicCurve](SketchConicCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConicCurve.h>

## Description

Extend a curve by specifying a point that determines the end of the curve to extend

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchConicCurve\_var" is a variable referencing a [SketchConicCurve](SketchConicCurve.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketchConicCurve\_var" is a variable referencing a [SketchConicCurve](SketchConicCurve.htm) object.  ```` ``` #include <Fusion/Sketch/SketchConicCurve.h>  // Uses no optional arguments. returnValue = sketchConicCurve_var->extend(endPoint);  // Uses optional arguments. returnValue = sketchConicCurve_var->extend(endPoint, createConstraints); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | Returns the modified original curve if the start or end of the curve is extended If the extend joins a curve to another, the two original curves are deleted and a new curve is returned If an arc is extended so as to become a circle, the original arc is deleted and a new circle is returned |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| endPoint | [Point3D](Point3D.htm) | A point (transient Point3D) on or closest to the end of the curve to extend. (start or end) The end of the curve closest to the endPoint gets extended |
| createConstraints | boolean | Constraints are created by default. Specify false to not create constraints.   This is an optional argument whose default value is True. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |