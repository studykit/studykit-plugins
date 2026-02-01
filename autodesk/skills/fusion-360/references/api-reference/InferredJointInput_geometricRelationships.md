# InferredJointInput.geometricRelationships Property![](../images/TestTubeLarge.png)

Parent Object: [InferredJointInput](InferredJointInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/InferredJointInput.h>

## Description

Returns the collection object used to define the geometric relationships from which the joint will be inferred. A geometric relationship defines several things: the pair of entities, if the relationship is flipped, if it defines a mating alignment or an angle, and the value of the offset or angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inferredJointInput\_var" is a variable referencing an InferredJointInput object. |

"inferredJointInput\_var" is a variable referencing an InferredJointInput object. ```` ``` #include <Fusion/Components/InferredJointInput.h>  // Get the value of the property. Ptr<GeometricRelationships> propertyValue = inferredJointInput_var->geometricRelationships(); ``` ```` |

## Property Value

This is a read only property whose value is a [GeometricRelationships](GeometricRelationships.htm).

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |