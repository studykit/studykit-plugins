# ConstructionPlanes Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlanes.h>

## Description

Provides access to the construction planes within a component and provides methods to create new construction planes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ConstructionPlanes_add.htm) | Creates and adds a new ConstructionPlane using the creation parameters in the ConstructionPlaneInput. |
| [classType](ConstructionPlanes_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](ConstructionPlanes_createInput.htm) | Create a ConstructionPlaneInput object that is in turn used to create a ConstructionPlane. |
| [item](ConstructionPlanes_item.htm) | Function that returns the specified construction plane using an index into the collection. |
| [itemByName](ConstructionPlanes_itemByName.htm) | Returns the specified construction plane using the name of the construction plane as it is displayed in the browser. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [component](ConstructionPlanes_component.htm) | Returns the component that owns this collection. |
| [count](ConstructionPlanes_count.htm) | Returns the number of construction planes in the collection. |
| [isValid](ConstructionPlanes_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConstructionPlanes_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[BaseComponent.constructionPlanes](BaseComponent_constructionPlanes.htm), [Component.constructionPlanes](Component_constructionPlanes.htm), [FlatPatternComponent.constructionPlanes](FlatPatternComponent_constructionPlanes.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Plane API Sample](ConstructionPlaneSample_Sample.htm) | Demonstrates creating construction plane by different ways. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |