# CAMTemplate.setHoleSignatureXML Method![](../images/TestTubeLarge.png)

Parent Object: [CAMTemplate](CAMTemplate.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplate.h>

## Description

Provide an XML snippet to specify a hole signature. This will have no effect if this is not a hole template. This will fail if the provided snippet is not valid.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMTemplate\_var" is a variable referencing a [CAMTemplate](CAMTemplate.htm) object.```` ``` returnValue = cAMTemplate_var.setHoleSignatureXML(xmlSnippet) ``` ```` |

"cAMTemplate\_var" is a variable referencing a [CAMTemplate](CAMTemplate.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | This will return true on success, false on failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| xmlSnippet | string |  |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |