# ConstructionAxes Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxes.h>

## Description

Provides access to the construction axes within a component and provides methods to create new construction axes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ConstructionAxes_add.htm) | Creates and adds a new ConstructionAxis using the creation parameters in the ConstructionAxisInput. |
| [classType](ConstructionAxes_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](ConstructionAxes_createInput.htm) | Create a ConstructionAxisInput object that is in turn used to create a ConstructionAxis. |
| [item](ConstructionAxes_item.htm) | Function that returns the specified construction axis using an index into the collection. |
| [itemByName](ConstructionAxes_itemByName.htm) | Returns the specified construction axis using the name of the construction axis as it is displayed in the browser. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [component](ConstructionAxes_component.htm) | The component that owns this collection. |
| [count](ConstructionAxes_count.htm) | The number of construction axes in the collection. |
| [isValid](ConstructionAxes_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConstructionAxes_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[BaseComponent.constructionAxes](BaseComponent_constructionAxes.htm), [Component.constructionAxes](Component_constructionAxes.htm), [FlatPatternComponent.constructionAxes](FlatPatternComponent_constructionAxes.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Axis API Sample](ConstructionAxisSample_Sample.htm) | Demonstrates creating construction axis in various ways. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |