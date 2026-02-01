# JointOrigins.add Method

Parent Object: [JointOrigins](JointOrigins.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigins.h>

## Description

Create a new joint origin.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOrigins\_var" is a variable referencing a [JointOrigins](JointOrigins.htm) object.```` ``` returnValue = jointOrigins_var.add(input) ``` ```` |

"jointOrigins\_var" is a variable referencing a [JointOrigins](JointOrigins.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [JointOrigin](JointOrigin.htm) | Returns a JointOrigin object if successfully created and null if it fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [JointOriginInput](JointOriginInput.htm) | A JointOriginInput object that full defines all of the information needed to create a joint origin. You create a JointOriginInput by using the createInput method of the JointOrigins object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Joint Origin Between Two Faces Sample](JointOrigin2Planes_Sample.htm) | Demonstrates creating a new Joint Origin between two planes. |
| [Joint Origin Sample](JointOriginSample_Sample.htm) | Demonstrates creating a new Joint Origin. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |