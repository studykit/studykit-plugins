# MeshConvertFeature.isPreprocessHoles Property![](../images/TestTubeLarge.png)

Parent Object: [MeshConvertFeature](MeshConvertFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshConvertFeature.h>

## Description

Smooths the boundaries of open holes in the mesh body. Improves the chance of successful conversion by refining the shape of holes that will remain open. Only valid if meshConvertMethodType is OrganicMeshConvertMethodType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshConvertFeature\_var" is a variable referencing a MeshConvertFeature object. |

"meshConvertFeature\_var" is a variable referencing a MeshConvertFeature object. ```` ``` #include <Fusion/MeshBody/MeshConvertFeature.h>  // Get the value of the property. boolean propertyValue = meshConvertFeature_var->isPreprocessHoles();  // Set the value of the property, where value_var is a boolean. bool returnValue = meshConvertFeature_var->isPreprocessHoles(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |