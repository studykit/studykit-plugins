# MeshReverseNormalFeatures.createInput Method![](../images/TestTubeLarge.png)

Parent Object: [MeshReverseNormalFeatures](MeshReverseNormalFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshReverseNormalFeatures.h>

## Description

Creates a MeshReverseNormalFeatureInput object. Use properties and methods on this object to define the mesh reverse normal you want to create and then use the add method, passing in the MeshReverseNormalFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshReverseNormalFeatures\_var" is a variable referencing a [MeshReverseNormalFeatures](MeshReverseNormalFeatures.htm) object.```` ``` returnValue = meshReverseNormalFeatures_var.createInput(mesh) ``` ```` |

"meshReverseNormalFeatures\_var" is a variable referencing a [MeshReverseNormalFeatures](MeshReverseNormalFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshReverseNormalFeatureInput](MeshReverseNormalFeatureInput.htm) | Returns the newly created MeshReverseNormalFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| mesh | [Base](Base.htm) | A mesh body or an object collection with face groups in either a parametric or direct modeling design. |

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |