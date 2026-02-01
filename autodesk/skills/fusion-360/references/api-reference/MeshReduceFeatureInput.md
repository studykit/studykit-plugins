# MeshReduceFeatureInput Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshReduceFeatureInput.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

This class defines the methods and properties that pertain to the definition of a mesh reduce feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MeshReduceFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [facecount](MeshReduceFeatureInput_facecount.htm) | Gets and sets the target face count for the reduced mesh as a target for the reduction. Only valid if meshReduceTargetType is FaceCountMeshReduceTargetType. |
| [isValid](MeshReduceFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [maximumDeviation](MeshReduceFeatureInput_maximumDeviation.htm) | Controls the maximum deviation of the reduced mesh to the original mesh. The default value is 0. Only valid if meshReduceTargetType is MaximumDeviationMeshReduceTargetType. |
| [mesh](MeshReduceFeatureInput_mesh.htm) | Gets and sets the input mesh body. |
| [meshReduceMethodType](MeshReduceFeatureInput_meshReduceMethodType.htm) | Gets and sets the type of mesh reduce, default value is AdaptiveReduceType. |
| [meshReduceTargetType](MeshReduceFeatureInput_meshReduceTargetType.htm) | Gets and sets the target criteria for the reduction, default value is MaximumDeviationMeshReduceTargetType. |
| [objectType](MeshReduceFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [proportion](MeshReduceFeatureInput_proportion.htm) | Gets and sets the proportion of number of faces of the reduced mesh to the number of faces of original mesh as a target for the reduction. The value can range between 0 and 100 percent. Only valid if meshReduceTargetType is ProportionMeshReduceTargetType. |
| [targetBaseFeature](MeshReduceFeatureInput_targetBaseFeature.htm) | When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature. |

## Accessed From

[MeshReduceFeatures.createInput](MeshReduceFeatures_createInput.htm)

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |