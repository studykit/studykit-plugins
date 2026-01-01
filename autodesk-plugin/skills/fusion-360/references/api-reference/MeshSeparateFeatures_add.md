# MeshSeparateFeatures.add Method![](../images/TestTubeLarge.png)

Parent Object: [MeshSeparateFeatures](MeshSeparateFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshSeparateFeatures.h>

## Description

Creates a mesh separate feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshSeparateFeatures\_var" is a variable referencing a [MeshSeparateFeatures](MeshSeparateFeatures.htm) object.```` ``` returnValue = meshSeparateFeatures_var.add(input) ``` ```` |

"meshSeparateFeatures\_var" is a variable referencing a [MeshSeparateFeatures](MeshSeparateFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshSeparateFeature](MeshSeparateFeature.htm) | Returns the newly created MeshSeparateFeature object or null if the creation failed. Returns nothing in the case where the feature is non-parametric. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [MeshSeparateFeatureInput](MeshSeparateFeatureInput.htm) | A MeshSeparateFeatureInput object that defines the desired MeshSeparate feature. Use the createInput method to create a new MeshSeparateFeatureInput object and then use methods on it (the MeshSeparateFeatureInput object) to define the separation. |

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |