# EmbossFeature.createForAssemblyContext Method![](../images/TestTubeLarge.png)

Parent Object: [EmbossFeature](EmbossFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/EmbossFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"embossFeature\_var" is a variable referencing an [EmbossFeature](EmbossFeature.htm) object.```` ``` returnValue = embossFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"embossFeature\_var" is a variable referencing an [EmbossFeature](EmbossFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [EmbossFeature](EmbossFeature.htm) | Returns the proxy object or null if this is not the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |