# LoftFeature.createForAssemblyContext Method

Parent Object: [LoftFeature](LoftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeature\_var" is a variable referencing a [LoftFeature](LoftFeature.htm) object.```` ``` returnValue = loftFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"loftFeature\_var" is a variable referencing a [LoftFeature](LoftFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [LoftFeature](LoftFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |