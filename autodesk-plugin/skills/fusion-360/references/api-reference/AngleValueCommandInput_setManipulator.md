# AngleValueCommandInput.setManipulator Method

Parent Object: [AngleValueCommandInput](AngleValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/AngleValueCommandInput.h>

## Description

Defines the position and orientation of the manipulator. The manipulator is only visible when both the isVisible and isEnabled properties are true. If those properties are true and the setManipulator has not been called, the manipulator will be displayed in a default location (0,0,0) using default directions; x direction (1,0,0) and y direction (0,1,0). Because of that the input is typically set to be invisible and/or disabled and then enabled once enough input has been specified that you can display the manipulator in the desired location.

## Syntax

* [Python](#Python)
* [C++](#C++)

"angleValueCommandInput\_var" is a variable referencing an [AngleValueCommandInput](AngleValueCommandInput.htm) object.```` ``` returnValue = angleValueCommandInput_var.setManipulator(origin, xDirection, yDirection) ``` ```` |

"angleValueCommandInput\_var" is a variable referencing an [AngleValueCommandInput](AngleValueCommandInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| origin | [Point3D](Point3D.htm) | Defines the center position of the manipulator in root component space. |
| xDirection | [Vector3D](Vector3D.htm) | Defines the X direction of the manipulator in root component space. The X direction is the 0 angle direction. This direction, along with the Y direction vector define the plane that the manipulator is displayed on. |
| yDirection | [Vector3D](Vector3D.htm) | Defines the Y direction of the manipulator in root component space. The X and Y direction vectors define the plane the manipulator is displayed one. When the manipulator is rotated from the xDirection vector towards the yDirection vector that is the positive direction. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |