# AsBuiltJoint.createForAssemblyContext Method

Parent Object: [AsBuiltJoint](AsBuiltJoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJoint.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJoint\_var" is a variable referencing an [AsBuiltJoint](AsBuiltJoint.htm) object.```` ``` returnValue = asBuiltJoint_var.createForAssemblyContext(occurrence) ``` ```` |

"asBuiltJoint\_var" is a variable referencing an [AsBuiltJoint](AsBuiltJoint.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [AsBuiltJoint](AsBuiltJoint.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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