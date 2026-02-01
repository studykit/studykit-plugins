# JointOrigin.createForAssemblyContext Method

Parent Object: [JointOrigin](JointOrigin.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigin.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOrigin\_var" is a variable referencing a [JointOrigin](JointOrigin.htm) object.```` ``` returnValue = jointOrigin_var.createForAssemblyContext(occurrence) ``` ```` |

"jointOrigin\_var" is a variable referencing a [JointOrigin](JointOrigin.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [JointOrigin](JointOrigin.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |