# DirectionCommandInput.setManipulator Method

Parent Object: [DirectionCommandInput](DirectionCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DirectionCommandInput.h>

## Description

Defines a direction manipulator arrow in the graphics viewport whose direction can be flipped by the toggling the check box, clicking the button or by the user clicking and dragging on the manipulator arrow.

## Syntax

* [Python](#Python)
* [C++](#C++)

"directionCommandInput\_var" is a variable referencing a [DirectionCommandInput](DirectionCommandInput.htm) object.```` ``` returnValue = directionCommandInput_var.setManipulator(origin, direction) ``` ```` |

"directionCommandInput\_var" is a variable referencing a [DirectionCommandInput](DirectionCommandInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| origin | [Point3D](Point3D.htm) | The origin point of the direction manipulator (arrow) in the model space of the root component. |
| direction | [Vector3D](Vector3D.htm) | The direction of the manipulator (arrow) in the model space of the root component. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |