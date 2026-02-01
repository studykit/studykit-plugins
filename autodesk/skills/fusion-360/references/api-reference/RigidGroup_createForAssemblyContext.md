# RigidGroup.createForAssemblyContext Method

Parent Object: [RigidGroup](RigidGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroup.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidGroup\_var" is a variable referencing a [RigidGroup](RigidGroup.htm) object.```` ``` returnValue = rigidGroup_var.createForAssemblyContext(occurrence) ``` ```` |

"rigidGroup\_var" is a variable referencing a [RigidGroup](RigidGroup.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RigidGroup](RigidGroup.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |