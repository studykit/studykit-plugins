# MeshSmoothFeatureInput.smoothness Property![](../images/TestTubeLarge.png)

Parent Object: [MeshSmoothFeatureInput](MeshSmoothFeatureInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshSmoothFeatureInput.h>

## Description

Gets and sets the smoothness value. The range is between 0 and 1. The default value is 0.02. The higher the value the stronger the smoothing.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshSmoothFeatureInput\_var" is a variable referencing a MeshSmoothFeatureInput object. |

"meshSmoothFeatureInput\_var" is a variable referencing a MeshSmoothFeatureInput object. ```` ``` #include <Fusion/MeshBody/MeshSmoothFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = meshSmoothFeatureInput_var->smoothness();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = meshSmoothFeatureInput_var->smoothness(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |