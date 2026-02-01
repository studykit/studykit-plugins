# MeshRepairFeatureInput Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshRepairFeatureInput.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

This class defines the methods and properties that pertain to the definition of a mesh repair feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MeshRepairFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [density](MeshRepairFeatureInput_density.htm) | Controls the density of the newly created triangles in RebuildMeshRepairType, default value is 128. The values can range between 8 and 256. Only valid if meshRepairType is RebuildMeshRepairType. |
| [isValid](MeshRepairFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [mesh](MeshRepairFeatureInput_mesh.htm) | Gets and sets the input mesh body. |
| [meshRepairRebuildType](MeshRepairFeatureInput_meshRepairRebuildType.htm) | Gets and sets the type of mesh repair rebuild mode, default value is FastMeshRepairRebuildType. Only valid if meshRepairType is RebuildMeshRepairType. |
| [meshRepairType](MeshRepairFeatureInput_meshRepairType.htm) | Gets and sets the type of mesh repair, default value is StitchAndRemoveMeshRepairType. |
| [objectType](MeshRepairFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [offset](MeshRepairFeatureInput_offset.htm) | Gets and sets the offset from the original mesh to the newly created mesh, default value is zero. Only valid if meshRepairType is RebuildMeshRepairType and meshRepairRebuildType is AccurateMeshRepairRebuildType. |
| [targetBaseFeature](MeshRepairFeatureInput_targetBaseFeature.htm) | When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature. |

## Accessed From

[MeshRepairFeatures.createInput](MeshRepairFeatures_createInput.htm)

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |