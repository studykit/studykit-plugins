# MeshCombineFaceGroupsFeatures.add Method![](../images/TestTubeLarge.png)

Parent Object: [MeshCombineFaceGroupsFeatures](MeshCombineFaceGroupsFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshCombineFaceGroupsFeatures.h>

## Description

Creates a mesh combine face groups feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshCombineFaceGroupsFeatures\_var" is a variable referencing a [MeshCombineFaceGroupsFeatures](MeshCombineFaceGroupsFeatures.htm) object.```` ``` returnValue = meshCombineFaceGroupsFeatures_var.add(input) ``` ```` |

"meshCombineFaceGroupsFeatures\_var" is a variable referencing a [MeshCombineFaceGroupsFeatures](MeshCombineFaceGroupsFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshCombineFaceGroupsFeature](MeshCombineFaceGroupsFeature.htm) | Returns the newly created MeshCombineFaceGroupsFeatureInput object or null if the creation failed. Returns nothing in the case where the feature is non-parametric. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [MeshCombineFaceGroupsFeatureInput](MeshCombineFaceGroupsFeatureInput.htm) | A MeshCombineFaceGroupsFeatureInput object that defines the desired mesh combine face groups feature. Use the createInput method to create a new MeshCombineFaceGroupsFeatureInput object and then use methods on it (the MeshCombineFaceGroupsFeatureInput object) to define the mesh combine face groups feature. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |