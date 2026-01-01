# MeshRemeshFeatureInput.targetBaseFeature Property![](../images/TestTubeLarge.png)

Parent Object: [MeshRemeshFeatureInput](MeshRemeshFeatureInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshRemeshFeatureInput.h>

## Description

When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshRemeshFeatureInput\_var" is a variable referencing a MeshRemeshFeatureInput object. |

"meshRemeshFeatureInput\_var" is a variable referencing a MeshRemeshFeatureInput object. ```` ``` #include <Fusion/MeshBody/MeshRemeshFeatureInput.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = meshRemeshFeatureInput_var->targetBaseFeature();  // Set the value of the property, where value_var is a BaseFeature. bool returnValue = meshRemeshFeatureInput_var->targetBaseFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |