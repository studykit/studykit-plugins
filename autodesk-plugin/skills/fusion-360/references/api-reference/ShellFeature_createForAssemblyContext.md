# ShellFeature.createForAssemblyContext Method

Parent Object: [ShellFeature](ShellFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeature\_var" is a variable referencing a [ShellFeature](ShellFeature.htm) object.```` ``` returnValue = shellFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"shellFeature\_var" is a variable referencing a [ShellFeature](ShellFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ShellFeature](ShellFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |