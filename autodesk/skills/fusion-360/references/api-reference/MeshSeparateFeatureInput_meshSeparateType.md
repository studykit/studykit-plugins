# MeshSeparateFeatureInput.meshSeparateType Property![](../images/TestTubeLarge.png)

Parent Object: [MeshSeparateFeatureInput](MeshSeparateFeatureInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshSeparateFeatureInput.h>

## Description

Gets and sets the output type of mesh separation, default value is ShellMeshSeparateType. Only valid if the input is a mesh body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshSeparateFeatureInput\_var" is a variable referencing a MeshSeparateFeatureInput object. |

"meshSeparateFeatureInput\_var" is a variable referencing a MeshSeparateFeatureInput object. ```` ``` #include <Fusion/MeshBody/MeshSeparateFeatureInput.h>  // Get the value of the property. MeshSeparateTypes propertyValue = meshSeparateFeatureInput_var->meshSeparateType();  // Set the value of the property, where value_var is a MeshSeparateTypes. bool returnValue = meshSeparateFeatureInput_var->meshSeparateType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MeshSeparateTypes](MeshSeparateTypes.htm).

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |