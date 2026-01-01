# Sketch.arePointsShown Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Indicates if the sketch points in the sketch are displayed. Points that are not connected to any other geometry will continue to be shown.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object. |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. boolean propertyValue = sketch_var->arePointsShown();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketch_var->arePointsShown(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |