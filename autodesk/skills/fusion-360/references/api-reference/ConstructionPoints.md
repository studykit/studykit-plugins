# ConstructionPoints Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPoints.h>

## Description

Provides access to the construction points within a component and provides methods to create new construction points.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ConstructionPoints_add.htm) | Creates a new construction point. |
| [classType](ConstructionPoints_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](ConstructionPoints_createInput.htm) | Create a ConstructionPointInput object that is in turn used to create a ConstructionPoint. |
| [item](ConstructionPoints_item.htm) | Function that returns the specified construction point using an index into the collection. |
| [itemByName](ConstructionPoints_itemByName.htm) | Returns the specified construction point using the name of the construction point as it is displayed in the browser. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [component](ConstructionPoints_component.htm) | The component that owns this collection. |
| [count](ConstructionPoints_count.htm) | The number of construction points in the collection. |
| [isValid](ConstructionPoints_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConstructionPoints_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[BaseComponent.constructionPoints](BaseComponent_constructionPoints.htm), [Component.constructionPoints](Component_constructionPoints.htm), [FlatPatternComponent.constructionPoints](FlatPatternComponent_constructionPoints.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Point API Sample](ConstructionPointSample_Sample.htm) | Demonstrates creating construction point by different ways |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |