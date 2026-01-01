# Sketch.addCenterToCenterSlot Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Creates the geometry that represents a slot. Geometric constraints are automatically added to the geometry to maintain the slot shape and optionally, dimensions to control the size can be added. The created geometry and constraints are returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.  ```` ``` #include <Fusion/Sketch/Sketch.h>  // Uses no optional arguments. returnValue = sketch_var->addCenterToCenterSlot(startPoint, endPoint, width);  // Uses optional arguments. returnValue = sketch_var->addCenterToCenterSlot(startPoint, endPoint, width, createWidthDimension, length, angle); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Base](Base.htm)[] | Returns an array containing the start point arc, the end arc, the two lines that define the slot, the construction line between the two points, and optionally, the construction line the angle is measured from if an angle is specified, and the dimension constraints that were created in the order of width, length, and angle. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| startPoint | [Base](Base.htm) | The start point of the slot. It can be a SketchPoint or Point3D object. If a SketchPoint is provided a coincident constraint will be created between the start point of the slot and the provided sketch point. |
| endPoint | [Base](Base.htm) | The end point of the slot. It can be a SketchPoint or Point3D object. This point defines the length of the slot. If a SketchPoint is provided a coincident constraint is created between the end point of the slot and the provided sketch point.   If the length or angle arguments are provided, the point is not the actual end point but is used to determine the direction of the slot. |
| width | [ValueInput](ValueInput.htm) | A ValueInput object that defines the width of the slot. The ValueInput can define either a real value or an expression string. If it is a real value, it defines the width of the slot in centimeters.   When using a ValueInput created using a string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "5", "5 in", "5 in / 2", "5 + Length" that defines a length. |
| createWidthDimension | boolean | Specifies if a dimension constraint and its associated parameter is created to control the width of the slot.   This is an optional argument whose default value is False. |
| length | [ValueInput](ValueInput.htm) | Optional argument that defines the length of the slot using a ValueInput. If this is provided, it overrides the endPoint and explicitly defines the length of the slot. If the length is specified, a dimension constraint and its associated parameter is created to control the length.   The ValueInput can define either a real value or an expression string. If it is a real value, it defines the length of the slot in centimeters. When it is an expression string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "5", "5 in", "5 in / 2", "5 + Length" that defines a length.   This is an optional argument whose default value is null. |
| angle | [ValueInput](ValueInput.htm) | Optional argument that defines the angle of the slot using a ValueInput. If this is provided, it overrides the endPoint and explicitly defines the angle of the slot. If the angle is specified, a horizontal construction line, a dimension constraint, and its associated parameter is created to control the angle. The angle is measured from a horizontal line that starts at that start point and goes in the positive X direction. The angle is always less than 180 deg. and depending on the location of the end point, the angle will be clockwise or counterclockwise from the horizontal line.   The ValueInput can define either a real value or an expression string. If it is a real value, it defines the angle of the slot in radians. When it is an expression string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "45", "45 deg", "180 / 3", "Sweep \* 2" that defines an angle.   This is an optional argument whose default value is null. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |