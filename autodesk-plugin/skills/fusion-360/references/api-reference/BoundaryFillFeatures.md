# BoundaryFillFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeatures.h>

## Description

Collection that provides access to all of the existing boundary fill features in a component and supports the ability to create new boundary fill features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](BoundaryFillFeatures_add.htm) | Creates a new boundary fill feature. |
| [classType](BoundaryFillFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](BoundaryFillFeatures_createInput.htm) | Creates a BoundaryFillFeatureInput object. Use properties and methods on this object to define the boundary fill you want to create and then use the Add method, passing in the BoundaryFillFeatureInput object. |
| [item](BoundaryFillFeatures_item.htm) | Function that returns the specified boundary fill feature using an index into the collection. |
| [itemByName](BoundaryFillFeatures_itemByName.htm) | Function that returns the specified boundary fill feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BoundaryFillFeatures_count.htm) | The number of boundary fill features in the collection. |
| [isValid](BoundaryFillFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BoundaryFillFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[Features.boundaryFillFeatures](Features_boundaryFillFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Boundary Fill Feature API Sample](BoundaryFillFeatureSample_Sample.htm) | Demonstrates creating a new boundary fill feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |