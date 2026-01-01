# Sketch.offset Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

To access the full capabilities supported by offset, you should use the createOffsetInput and addOffset2 methods.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` # Uses no optional arguments. returnValue = sketch_var.offset(curves, directionPoint)  # Uses optional arguments. returnValue = sketch_var.offset(curves, directionPoint, offset) ``` ```` |

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.  ```` ``` #include <Fusion/Sketch/Sketch.h>  // Uses no optional arguments. returnValue = sketch_var->offset(curves, directionPoint);  // Uses optional arguments. returnValue = sketch_var->offset(curves, directionPoint, offset); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | A collection of the new offset sketch curves created |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| curves | [ObjectCollection](ObjectCollection.htm) | A set of end connected curves. The Sketch.FindConnectedCurves method is a convenient way to get this set of curves. |
| directionPoint | [Point3D](Point3D.htm) | Defines which side of the input curves to create the offset on |
| offset | double | The distance to offset the curves in centimeters.   This is an optional argument whose default value is 0.0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch fillet and offset API Sample](SketchFilletAndOffset_Sample.htm) | Demonstrates the creation of a fillet in a sketch and offset a set of curves. |

## Version

Introduced in version August 2014
Retired in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |