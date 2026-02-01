# MeshCombineFeature.toolBodies Property![](../images/TestTubeLarge.png)

Parent Object: [MeshCombineFeature](MeshCombineFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshCombineFeature.h>

## Description

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshCombineFeature\_var" is a variable referencing a MeshCombineFeature object. |

"meshCombineFeature\_var" is a variable referencing a MeshCombineFeature object. ```` ``` #include <Fusion/MeshBody/MeshCombineFeature.h>  // Get the value of the property. std::vector<Ptr<MeshBody>> propertyValue = meshCombineFeature_var->toolBodies();  // Set the value of the property, where value_var is a MeshBody. bool returnValue = meshCombineFeature_var->toolBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [MeshBody](MeshBody.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |