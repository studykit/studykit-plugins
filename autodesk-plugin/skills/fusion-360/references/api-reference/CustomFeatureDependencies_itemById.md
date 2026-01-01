# CustomFeatureDependencies.itemById Method![](../images/TestTubeLarge.png)

Parent Object: [CustomFeatureDependencies](CustomFeatureDependencies.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatureDependencies.h>

## Description

Function that returns the specified custom dependency given its ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customFeatureDependencies\_var" is a variable referencing a [CustomFeatureDependencies](CustomFeatureDependencies.htm) object.```` ``` returnValue = customFeatureDependencies_var.itemById(id) ``` ```` |

"customFeatureDependencies\_var" is a variable referencing a [CustomFeatureDependencies](CustomFeatureDependencies.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CustomFeatureDependency](CustomFeatureDependency.htm) | Returns the specified item or null if the specified ID was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the dependency, which was assigned when the dependency was defined. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |