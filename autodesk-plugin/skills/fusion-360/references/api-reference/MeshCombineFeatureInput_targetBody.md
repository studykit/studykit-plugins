# MeshCombineFeatureInput.targetBody Property![](../images/TestTubeLarge.png)

Parent Object: [MeshCombineFeatureInput](MeshCombineFeatureInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshCombineFeatureInput.h>

## Description

Gets and sets the input targetBody.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshCombineFeatureInput\_var" is a variable referencing a MeshCombineFeatureInput object. |

"meshCombineFeatureInput\_var" is a variable referencing a MeshCombineFeatureInput object. ```` ``` #include <Fusion/MeshBody/MeshCombineFeatureInput.h>  // Get the value of the property. Ptr<MeshBody> propertyValue = meshCombineFeatureInput_var->targetBody();  // Set the value of the property, where value_var is a MeshBody. bool returnValue = meshCombineFeatureInput_var->targetBody(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MeshBody](MeshBody.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |