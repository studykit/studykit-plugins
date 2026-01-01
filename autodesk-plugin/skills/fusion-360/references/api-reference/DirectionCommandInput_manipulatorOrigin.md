# DirectionCommandInput.manipulatorOrigin Property

Parent Object: [DirectionCommandInput](DirectionCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DirectionCommandInput.h>

## Description

Gets the origin point of the direction manipulator (arrow) in the model space of the root component. To set the origin use the setManipulator method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"directionCommandInput\_var" is a variable referencing a DirectionCommandInput object. |

"directionCommandInput\_var" is a variable referencing a DirectionCommandInput object. ```` ``` #include <Core/UserInterface/DirectionCommandInput.h>  // Get the value of the property. Ptr<Point3D> propertyValue = directionCommandInput_var->manipulatorOrigin(); ``` ```` |

## Property Value

This is a read only property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |