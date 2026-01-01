# Joints.addInferredJoint Method![](../images/TestTubeLarge.png)

Parent Object: [Joints](Joints.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joints.h>

## Description

Creates a new inferred joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joints\_var" is a variable referencing a [Joints](Joints.htm) object.```` ``` returnValue = joints_var.addInferredJoint(input) ``` ```` |

"joints\_var" is a variable referencing a [Joints](Joints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Joint](Joint.htm) | Returns the newly created Joint or fails if there is bad input. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [InferredJointInput](InferredJointInput.htm) | The InferredJointInput object that defines the pairs of geometry and other settings that Fusion will use to infer a joint from. An InferredJointInput object is created using the Joints.createInferredJointInput method. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |