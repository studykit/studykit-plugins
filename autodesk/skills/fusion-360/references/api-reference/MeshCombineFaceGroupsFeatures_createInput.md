# MeshCombineFaceGroupsFeatures.createInput Method![](../images/TestTubeLarge.png)

Parent Object: [MeshCombineFaceGroupsFeatures](MeshCombineFaceGroupsFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshCombineFaceGroupsFeatures.h>

## Description

Creates a MeshCombineFaceGroupsFeatureInput object. Use properties and methods on this object to define the mesh combine face groups feature you want to create and then use the add method, passing in the MeshCombineFaceGroupsFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshCombineFaceGroupsFeatures\_var" is a variable referencing a [MeshCombineFaceGroupsFeatures](MeshCombineFaceGroupsFeatures.htm) object.```` ``` returnValue = meshCombineFaceGroupsFeatures_var.createInput(inputFaceGroups) ``` ```` |

"meshCombineFaceGroupsFeatures\_var" is a variable referencing a [MeshCombineFaceGroupsFeatures](MeshCombineFaceGroupsFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshCombineFaceGroupsFeatureInput](MeshCombineFaceGroupsFeatureInput.htm) | Returns the newly created MeshCombineFaceGroupsFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputFaceGroups | FaceGroup[] | A array with face groups belonging to the same mesh. The mesh can be in either a parametric or direct modeling design. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |