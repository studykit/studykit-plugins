# MeshGenerateFaceGroupsFeatures.add Method![](../images/TestTubeLarge.png)

Parent Object: [MeshGenerateFaceGroupsFeatures](MeshGenerateFaceGroupsFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshGenerateFaceGroupsFeatures.h>

## Description

Creates a mesh generate face groups feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshGenerateFaceGroupsFeatures\_var" is a variable referencing a [MeshGenerateFaceGroupsFeatures](MeshGenerateFaceGroupsFeatures.htm) object.```` ``` returnValue = meshGenerateFaceGroupsFeatures_var.add(input) ``` ```` |

"meshGenerateFaceGroupsFeatures\_var" is a variable referencing a [MeshGenerateFaceGroupsFeatures](MeshGenerateFaceGroupsFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshGenerateFaceGroupsFeature](MeshGenerateFaceGroupsFeature.htm) | Returns the newly created MeshGenerateFaceGroupsFeatureInput object or null if the creation failed. Returns nothing in the case where the feature is non-parametric. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [MeshGenerateFaceGroupsFeatureInput](MeshGenerateFaceGroupsFeatureInput.htm) | A MeshGenerateFaceGroupsFeatureInput object that defines the desired generate face groups feature. Use the createInput method to create a new MeshGenerateFaceGroupsFeatureInput object and then use methods on it (the MeshGenerateFaceGroupsFeatureInput object) to define the generate face groups feature. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |