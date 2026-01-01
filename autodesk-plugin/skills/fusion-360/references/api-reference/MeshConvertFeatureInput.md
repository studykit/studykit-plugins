# MeshConvertFeatureInput Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshConvertFeatureInput.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

This class defines the methods and properties that pertain to the definition of a mesh convert feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MeshConvertFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [inputBodies](MeshConvertFeatureInput_inputBodies.htm) | Gets and sets the input meshes. |
| [isPreprocessHoles](MeshConvertFeatureInput_isPreprocessHoles.htm) | Smooths the boundaries of open holes in the mesh body. Improves the chance of successful conversion by refining the shape of holes that will remain open. Default value is false. Only valid if meshConvertMethodType is OrganicMeshConvertType. |
| [isValid](MeshConvertFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [meshConvertAccuracyType](MeshConvertFeatureInput_meshConvertAccuracyType.htm) | Gets and sets the accuracy of organic mesh convert, default value is MediumMeshConvertResolutionType. Only valid if meshConvertResolutionType is ByAccuracyMeshConvertResolutionType. |
| [meshConvertMethodType](MeshConvertFeatureInput_meshConvertMethodType.htm) | Gets and sets the convert type of mesh convert, default value is FacetedMeshConvertMethodType. |
| [meshConvertOperationType](MeshConvertFeatureInput_meshConvertOperationType.htm) | Gets and sets the operation type of mesh convert, default value is ParametricFeatureMeshConvertOperationType. |
| [meshConvertResolutionType](MeshConvertFeatureInput_meshConvertResolutionType.htm) | Gets and sets the resolution method of mesh convert, default value is ByAccuracyMeshConvertResolutionType. Only valid if meshConvertMethodType is OrganicMeshConvertMethodType. |
| [numberOfFaces](MeshConvertFeatureInput_numberOfFaces.htm) | Specify the number of faces to generate for the converted body. Only valid if meshConvertResolutionType is ByFacetNumberMeshConvertResolutionType. |
| [objectType](MeshConvertFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [targetBaseFeature](MeshConvertFeatureInput_targetBaseFeature.htm) | When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature. |

## Accessed From

[MeshConvertFeatures.createInput](MeshConvertFeatures_createInput.htm)

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |