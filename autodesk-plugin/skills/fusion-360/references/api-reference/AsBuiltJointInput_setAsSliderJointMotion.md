# AsBuiltJointInput.setAsSliderJointMotion Method

Parent Object: [AsBuiltJointInput](AsBuiltJointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJointInput.h>

## Description

Defines the relationship between the two joint geometries as a slider joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJointInput\_var" is a variable referencing an [AsBuiltJointInput](AsBuiltJointInput.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"asBuiltJointInput\_var" is a variable referencing an [AsBuiltJointInput](AsBuiltJointInput.htm) object.  ```` ``` #include <Fusion/Components/AsBuiltJointInput.h>  // Uses no optional arguments. returnValue = asBuiltJointInput_var->setAsSliderJointMotion(sliderDirection);  // Uses optional arguments. returnValue = asBuiltJointInput_var->setAsSliderJointMotion(sliderDirection, customSliderDirectionEntity); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sliderDirection | [JointDirections](JointDirections.htm) | Specifies which axis the slide direction is along. If this is set to CustomJointDirection then the customSliderDirectionEntity argument must also be provided. |
| customSliderDirectionEntity | [Base](Base.htm) | If the sliderDirection is CustomJointDirection this argument is used to specify the entity that defines the custom slider direction. This can be several types of entities that can define a direction.   This is an optional argument whose default value is null. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |