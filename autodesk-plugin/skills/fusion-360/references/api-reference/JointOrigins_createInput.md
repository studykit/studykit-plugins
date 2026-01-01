# JointOrigins.createInput Method

Parent Object: [JointOrigins](JointOrigins.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigins.h>

## Description

Creates a JointOriginInput object which is used to collect all of the information needed to create a simple joint origin. The creation of the input object takes the required input as the geometry argument and you can optionally use methods and properties on the created JointOriginInput to set other optional settings. The JointOrigin is created by calling the add method of the JointOrigins object and passing it the JointOriginInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOrigins\_var" is a variable referencing a [JointOrigins](JointOrigins.htm) object.```` ``` returnValue = jointOrigins_var.createInput(geometry) ``` ```` |

"jointOrigins\_var" is a variable referencing a [JointOrigins](JointOrigins.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [JointOriginInput](JointOriginInput.htm) | Returns a JointOriginInput object if successfully created and null if it fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| geometry | [JointGeometry](JointGeometry.htm) | A JointGeometry object that defines the geometry the joint origin will be created on. |

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