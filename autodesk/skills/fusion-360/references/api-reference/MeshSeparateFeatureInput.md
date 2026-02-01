# MeshSeparateFeatureInput Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshSeparateFeatureInput.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

This class defines the methods and properties that pertain to the definition of a MeshSeparate feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MeshSeparateFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isKeepBody](MeshSeparateFeatureInput_isKeepBody.htm) | Preserves a copy of the original mesh body. Default value is false. |
| [isMultipleBodies](MeshSeparateFeatureInput_isMultipleBodies.htm) |  |
| [isValid](MeshSeparateFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [mesh](MeshSeparateFeatureInput_mesh.htm) | Gets and sets the input mesh body. This can either be a mesh body or an object collection with face groups. |
| [meshSeparateType](MeshSeparateFeatureInput_meshSeparateType.htm) | Gets and sets the output type of mesh separation, default value is ShellMeshSeparateType. Only valid if the input is a mesh body. |
| [objectType](MeshSeparateFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [targetBaseFeature](MeshSeparateFeatureInput_targetBaseFeature.htm) | When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature. |

## Accessed From

[MeshSeparateFeatures.createInput](MeshSeparateFeatures_createInput.htm)

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |