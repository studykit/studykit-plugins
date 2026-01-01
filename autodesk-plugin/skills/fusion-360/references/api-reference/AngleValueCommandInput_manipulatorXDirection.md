# AngleValueCommandInput.manipulatorXDirection Property

Parent Object: [AngleValueCommandInput](AngleValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/AngleValueCommandInput.h>

## Description

Gets the X direction of the manipulator in the model space of the root component. The X direction is the 0 angle direction. This direction, along with the Y direction vector define the plane that the manipulator is displayed on.

## Syntax

* [Python](#Python)
* [C++](#C++)

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object.  ```` ``` # Get the value of the property. propertyValue = angleValueCommandInput_var.manipulatorXDirection ``` ```` |

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object. ```` ``` #include <Core/UserInterface/AngleValueCommandInput.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = angleValueCommandInput_var->manipulatorXDirection(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |