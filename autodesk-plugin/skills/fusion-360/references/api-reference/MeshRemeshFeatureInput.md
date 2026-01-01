# MeshRemeshFeatureInput Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshRemeshFeatureInput.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

This class defines the methods and properties that pertain to the definition of a mesh re-mesh feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MeshRemeshFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [density](MeshRemeshFeatureInput_density.htm) | Controls the density of the newly created faces of the re-meshed mesh. The values can range between 0 and 1. The default value is 0.25 |
| [isPreserveBoundariesEnabled](MeshRemeshFeatureInput_isPreserveBoundariesEnabled.htm) | Gets and sets if open boundary edges are preserved during the re-mesh process. Default value is false. |
| [isPreserveSharpEdgesEnabled](MeshRemeshFeatureInput_isPreserveSharpEdgesEnabled.htm) | Gets and sets if sharp edges are preserved during the re-mesh process. Default value is false. |
| [isValid](MeshRemeshFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [mesh](MeshRemeshFeatureInput_mesh.htm) | Gets and sets the input mesh body. |
| [meshRemeshMethodType](MeshRemeshFeatureInput_meshRemeshMethodType.htm) | Gets and sets the type of mesh re-mesh, default value is AdaptiveType. |
| [objectType](MeshRemeshFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [shapePreservation](MeshRemeshFeatureInput_shapePreservation.htm) | Gets and sets how much of the original shape needs to preserved. The value can range between 0 and 1. The default value is 0.5. Only valid if meshRemeshMethodType is AdaptiveType. |
| [targetBaseFeature](MeshRemeshFeatureInput_targetBaseFeature.htm) | When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature. |

## Accessed From

[MeshRemeshFeatures.createInput](MeshRemeshFeatures_createInput.htm)

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |