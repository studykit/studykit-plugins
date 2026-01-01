# TessellateFeatureInput Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/TessellateFeatureInput.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

This class defines the methods and properties that pertain to the definition of a tessellate feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](TessellateFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [aspectRatio](TessellateFeatureInput_aspectRatio.htm) | Specify ratio between the height and width of each face on the mesh body. Only valid if tessellateRefinementType is CustomTessellateRefinementType. |
| [createQuads](TessellateFeatureInput_createQuads.htm) | Creates quad faces on the mesh body where possible. |
| [inputBodies](TessellateFeatureInput_inputBodies.htm) | Gets and sets the input list of BReb bodies. |
| [isValid](TessellateFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [maximumEdgeLength](TessellateFeatureInput_maximumEdgeLength.htm) | Specify maximum length of any face edge on the mesh body. Only valid if tessellateRefinementType is CustomTessellateRefinementType. |
| [normalDeviation](TessellateFeatureInput_normalDeviation.htm) | Specify maximum angle between the normal vectors of each face on the mesh body. Only valid if tessellateRefinementType is CustomTessellateRefinementType. |
| [objectType](TessellateFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [surfaceDeviation](TessellateFeatureInput_surfaceDeviation.htm) | Specify maximum distance between the surface of the original body and the surface of the mesh body. Only valid if tessellateRefinementType is CustomTessellateRefinementType. |
| [targetBaseFeature](TessellateFeatureInput_targetBaseFeature.htm) | When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature. |
| [tessellateRefinementType](TessellateFeatureInput_tessellateRefinementType.htm) | Gets and sets the type of refinement, default value is MediumTessellateRefinementType. |

## Accessed From

[TessellateFeatures.createInput](TessellateFeatures_createInput.htm)

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |