# CAMTemplateLibrary.doesPathExist Method![](../images/TestTubeLarge.png)

Parent Object: [CAMTemplateLibrary](CAMTemplateLibrary.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplateLibrary.h>

## Description

Checks if the given URL points to an existing folder or asset in the library.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMTemplateLibrary\_var" is a variable referencing a [CAMTemplateLibrary](CAMTemplateLibrary.htm) object.```` ``` returnValue = cAMTemplateLibrary_var.doesPathExist(url) ``` ```` |

"cAMTemplateLibrary\_var" is a variable referencing a [CAMTemplateLibrary](CAMTemplateLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the URL points to an existing folder or asset, false otherwise. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL to be checked. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |