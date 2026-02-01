# MoveFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatures.h>

## Description

Collection that provides access to all of the existing move features in a component and supports the ability to create new move features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](MoveFeatures_add.htm) | Creates a new move feature. |
| [classType](MoveFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](MoveFeatures_createInput.htm) | \*\*RETIRED\*\* Creates a MoveFeatureInput object. Use properties and methods on this object to define the move feature you want to create and then use the Add method, passing in the MoveFeatureInput object. |
| [createInput2](MoveFeatures_createInput2.htm) | Creates a MoveFeatureInput object. Use properties and methods on this object to define how the move is defined and then use the MoveFeatues.add method, passing in the MoveFeatureInput object to create a move feature. |
| [item](MoveFeatures_item.htm) | Function that returns the specified move feature using an index into the collection. |
| [itemByName](MoveFeatures_itemByName.htm) | Function that returns the specified move feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](MoveFeatures_count.htm) | The number of move features in the collection. |
| [isValid](MoveFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MoveFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.moveFeatures](Features_moveFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Move Feature API Sample](MoveFeatureSample_Sample.htm) | Demonstrates creating a new move feature. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |