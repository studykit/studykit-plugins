# CAMParameters.resetToSystemDefaults Method![](../images/TestTubeLarge.png)

Parent Object: [CAMParameters](CAMParameters.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CAMParameters.h>

## Description

Resets each parameter to its system default.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMParameters\_var" is a variable referencing a [CAMParameters](CAMParameters.htm) object.```` ``` returnValue = cAMParameters_var.resetToSystemDefaults() ``` ```` |

"cAMParameters\_var" is a variable referencing a [CAMParameters](CAMParameters.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the reset was successful. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |