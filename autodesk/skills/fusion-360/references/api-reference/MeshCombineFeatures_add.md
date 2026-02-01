# MeshCombineFeatures.add Method![](../images/TestTubeLarge.png)

Parent Object: [MeshCombineFeatures](MeshCombineFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshCombineFeatures.h>

## Description

Creates a mesh combine feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshCombineFeatures\_var" is a variable referencing a [MeshCombineFeatures](MeshCombineFeatures.htm) object.```` ``` returnValue = meshCombineFeatures_var.add(input) ``` ```` |

"meshCombineFeatures\_var" is a variable referencing a [MeshCombineFeatures](MeshCombineFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshCombineFeature](MeshCombineFeature.htm) | Returns the newly created MeshCombineFeatureInput object or null if the creation failed. Returns nothing in the case where the feature is non-parametric. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [MeshCombineFeatureInput](MeshCombineFeatureInput.htm) | A MeshCombineFeatureInput object that defines the desired combine feature. Use the createInput method to create a new MeshCombineFeatureInput object and then use methods on it (the MeshCombineFeatureInput object) to define the combine. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |