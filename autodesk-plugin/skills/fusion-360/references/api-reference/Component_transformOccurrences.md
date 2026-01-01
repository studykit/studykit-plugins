# Component.transformOccurrences Method

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Transforms a set of occurrences in one step. This provides better performance than transforming them one at a time. This method is only valid when called on the root component because Fusion flattens the entire assembly structure when manipulating the assembly so all transforms are relative to the root component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a [Component](Component.htm) object.```` ``` returnValue = component_var.transformOccurrences(occurrences, transforms, ignoreJoints) ``` ```` |

"component\_var" is a variable referencing a [Component](Component.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the transform was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrences | Occurrence[] | An array of Occurrence objects that you want to transform. These must all be in the context of the root component which means proxies must be used for occurrences that are in sub-components. |
| transforms | Matrix3D[] | An array of Matrix3D objects that defines the transform to apply to each occurrence. This array must be the same size as the array provided for the occurrences argument and the transform will be applied to the occurrence at the same index in the occurrences array. |
| ignoreJoints | boolean | Specifies if the joints are to be ignored and the occurrences are to be positioned based on then specified transform or if the joints should be used and the occurrence is transformed the best it can while still honoring the joints. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |