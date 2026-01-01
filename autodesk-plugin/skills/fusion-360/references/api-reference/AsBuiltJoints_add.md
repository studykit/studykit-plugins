# AsBuiltJoints.add Method

Parent Object: [AsBuiltJoints](AsBuiltJoints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJoints.h>

## Description

Creates a new as-built joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJoints\_var" is a variable referencing an [AsBuiltJoints](AsBuiltJoints.htm) object.```` ``` returnValue = asBuiltJoints_var.add(input) ``` ```` |

"asBuiltJoints\_var" is a variable referencing an [AsBuiltJoints](AsBuiltJoints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [AsBuiltJoint](AsBuiltJoint.htm) | Returns the new AsBuiltJoint object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [AsBuiltJointInput](AsBuiltJointInput.htm) | An AsBuiltJointInput object that was created using the AsBuiltJoints.createInput method and then fully defined using the properties and methods on the AsBuiltJointInput object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [As-Built Joint Sample](AsBuiltJointSample_Sample.htm) | Demonstrates creating a new As-Built Joint. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |