# MeshSmoothFeatures Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshSmoothFeatures.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Collection that provides access to all of the existing MeshSmooth features in a component and supports the ability to create new MeshSmooth features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](MeshSmoothFeatures_add.htm) | Creates a mesh smooth feature. |
| [classType](MeshSmoothFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](MeshSmoothFeatures_createInput.htm) | Creates a MeshSmoothFeatureInput object. Use properties and methods on this object to define the mesh smooth you want to create and then use the add method, passing in the MeshSmoothFeatureInput object. |
| [item](MeshSmoothFeatures_item.htm) | Function that returns the specified mesh smooth feature using an index into the collection. |
| [itemByName](MeshSmoothFeatures_itemByName.htm) | Function that returns the specified MeshSmooth feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](MeshSmoothFeatures_count.htm) | The number of mesh smooth features in the collection. |
| [isValid](MeshSmoothFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MeshSmoothFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.meshSmoothFeatures](Features_meshSmoothFeatures.htm)

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |