# MeshGenerateFaceGroupsFeatureInput.meshGenerateFaceGroupsMethodType Property![](../images/TestTubeLarge.png)

Parent Object: [MeshGenerateFaceGroupsFeatureInput](MeshGenerateFaceGroupsFeatureInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshGenerateFaceGroupsFeatureInput.h>

## Description

Gets and sets the type of mesh generate face groups, default value is FastGenerateFaceGroupsType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshGenerateFaceGroupsFeatureInput\_var" is a variable referencing a MeshGenerateFaceGroupsFeatureInput object. |

"meshGenerateFaceGroupsFeatureInput\_var" is a variable referencing a MeshGenerateFaceGroupsFeatureInput object. ```` ``` #include <Fusion/MeshBody/MeshGenerateFaceGroupsFeatureInput.h>  // Get the value of the property. MeshGenerateFaceGroupsMethodTypes propertyValue = meshGenerateFaceGroupsFeatureInput_var->meshGenerateFaceGroupsMethodType();  // Set the value of the property, where value_var is a MeshGenerateFaceGroupsMethodTypes. bool returnValue = meshGenerateFaceGroupsFeatureInput_var->meshGenerateFaceGroupsMethodType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MeshGenerateFaceGroupsMethodTypes](MeshGenerateFaceGroupsMethodTypes.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |