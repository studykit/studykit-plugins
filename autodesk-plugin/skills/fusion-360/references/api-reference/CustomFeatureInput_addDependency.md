# CustomFeatureInput.addDependency Method![](../images/TestTubeLarge.png)

Parent Object: [CustomFeatureInput](CustomFeatureInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatureInput.h>

## Description

Adds an entity or parameter this feature is dependent on. This is used by Fusion to know when to recompute this feature and to control the behavior of the feature's node in the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customFeatureInput\_var" is a variable referencing a [CustomFeatureInput](CustomFeatureInput.htm) object.```` ``` returnValue = customFeatureInput_var.addDependency(id, entity) ``` ```` |

"customFeatureInput\_var" is a variable referencing a [CustomFeatureInput](CustomFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the dependency was successfully added. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | An ID for this dependency. This is used to allow you to identify which dependency is which in the future. The ID must be unique with respect to the other dependencies of this custom feature. |
| entity | [Base](Base.htm) | The entity or parameter you want to add as a dependency. This can be a BRepBody, BRepFace, BrepEdge, BRepVertex, a sketch, any sketch entities, a profile, any construction geometry, or any parameter. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |