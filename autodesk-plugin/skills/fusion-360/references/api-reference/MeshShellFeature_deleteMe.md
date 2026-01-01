# MeshShellFeature.deleteMe Method![](../images/TestTubeLarge.png)

Parent Object: [MeshShellFeature](MeshShellFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshShellFeature.h>

## Description

Deletes the feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshShellFeature\_var" is a variable referencing a [MeshShellFeature](MeshShellFeature.htm) object.```` ``` returnValue = meshShellFeature_var.deleteMe() ``` ```` |

"meshShellFeature\_var" is a variable referencing a [MeshShellFeature](MeshShellFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns a bool indicating if the delete was successful or not. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |