# VolumetricModelToMeshFeature.volumetricModel Property![](../images/TestTubeLarge.png)

Parent Object: [VolumetricModelToMeshFeature](VolumetricModelToMeshFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/VolumetricModelToMeshFeature.h>

## Description

Gets and sets the volumetric model to be converted to a mesh. The volumetric model must have the same parent component as the VolumetricModelToMeshFeature.This property is typed as core.Base because the adsk.fusion library does not reference the volume library where the VolumetricModel object is defined. At runtime, this property will return a VolumetricModel object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"volumetricModelToMeshFeature\_var" is a variable referencing a VolumetricModelToMeshFeature object. |

"volumetricModelToMeshFeature\_var" is a variable referencing a VolumetricModelToMeshFeature object. ```` ``` #include <Fusion/Features/VolumetricModelToMeshFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = volumetricModelToMeshFeature_var->volumetricModel();  // Set the value of the property, where value_var is a Base. bool returnValue = volumetricModelToMeshFeature_var->volumetricModel(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |