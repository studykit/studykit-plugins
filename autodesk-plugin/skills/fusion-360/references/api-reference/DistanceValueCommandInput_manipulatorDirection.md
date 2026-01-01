# DistanceValueCommandInput.manipulatorDirection Property

Parent Object: [DistanceValueCommandInput](DistanceValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DistanceValueCommandInput.h>

## Description

Gets the positive direction of the manipulator in the model space or the root component. To set the direction use the setManipulator method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceValueCommandInput\_var" is a variable referencing a DistanceValueCommandInput object. |

"distanceValueCommandInput\_var" is a variable referencing a DistanceValueCommandInput object. ```` ``` #include <Core/UserInterface/DistanceValueCommandInput.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = distanceValueCommandInput_var->manipulatorDirection(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |