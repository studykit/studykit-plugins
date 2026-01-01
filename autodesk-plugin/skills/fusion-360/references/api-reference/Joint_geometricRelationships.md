# Joint.geometricRelationships Property![](../images/TestTubeLarge.png)

Parent Object: [Joint](Joint.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joint.h>

## Description

Returns the set of geometric relationships that were used to infer this joint. This property is only valid when the jointType property returns InferredJointType. Otherwise, it returns null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joint\_var" is a variable referencing a Joint object. |

"joint\_var" is a variable referencing a Joint object. ```` ``` #include <Fusion/Components/Joint.h>  // Get the value of the property. Ptr<GeometricRelationships> propertyValue = joint_var->geometricRelationships(); ``` ```` |

## Property Value

This is a read only property whose value is a [GeometricRelationships](GeometricRelationships.htm).

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |