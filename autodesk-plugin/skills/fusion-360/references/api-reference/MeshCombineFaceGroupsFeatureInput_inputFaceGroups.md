# MeshCombineFaceGroupsFeatureInput.inputFaceGroups Property![](../images/TestTubeLarge.png)

Parent Object: [MeshCombineFaceGroupsFeatureInput](MeshCombineFaceGroupsFeatureInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshCombineFaceGroupsFeatureInput.h>

## Description

Gets and sets the input face groups, which should be combined. They need to belong to the same mesh body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshCombineFaceGroupsFeatureInput\_var" is a variable referencing a MeshCombineFaceGroupsFeatureInput object. |

"meshCombineFaceGroupsFeatureInput\_var" is a variable referencing a MeshCombineFaceGroupsFeatureInput object. ```` ``` #include <Fusion/MeshBody/MeshCombineFaceGroupsFeatureInput.h>  // Get the value of the property. std::vector<Ptr<FaceGroup>> propertyValue = meshCombineFaceGroupsFeatureInput_var->inputFaceGroups();  // Set the value of the property, where value_var is a FaceGroup. bool returnValue = meshCombineFaceGroupsFeatureInput_var->inputFaceGroups(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [FaceGroup](FaceGroup.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |