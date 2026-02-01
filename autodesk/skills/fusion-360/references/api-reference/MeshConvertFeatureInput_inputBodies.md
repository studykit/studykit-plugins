# MeshConvertFeatureInput.inputBodies Property![](../images/TestTubeLarge.png)

Parent Object: [MeshConvertFeatureInput](MeshConvertFeatureInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshConvertFeatureInput.h>

## Description

Gets and sets the input meshes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshConvertFeatureInput\_var" is a variable referencing a MeshConvertFeatureInput object. |

"meshConvertFeatureInput\_var" is a variable referencing a MeshConvertFeatureInput object. ```` ``` #include <Fusion/MeshBody/MeshConvertFeatureInput.h>  // Get the value of the property. std::vector<Ptr<MeshBody>> propertyValue = meshConvertFeatureInput_var->inputBodies();  // Set the value of the property, where value_var is a MeshBody. bool returnValue = meshConvertFeatureInput_var->inputBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [MeshBody](MeshBody.htm).

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |