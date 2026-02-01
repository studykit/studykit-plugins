# CustomFeatureParameter.deleteMe Method![](../images/TestTubeLarge.png)

Parent Object: [CustomFeatureParameter](CustomFeatureParameter.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatureParameter.h>

## Description

Deletes this ModelParameter. As a general rule, model parameters cannot be deleted because features depend on them. However, there are uncommon workflows where a parameter no longer has any dependents and is not automatically deleted. You can use the isDeletable property to see if the parameter is in this state and can successfully be deleted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customFeatureParameter\_var" is a variable referencing a [CustomFeatureParameter](CustomFeatureParameter.htm) object.```` ``` returnValue = customFeatureParameter_var.deleteMe() ``` ```` |

"customFeatureParameter\_var" is a variable referencing a [CustomFeatureParameter](CustomFeatureParameter.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the delete was successful. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |